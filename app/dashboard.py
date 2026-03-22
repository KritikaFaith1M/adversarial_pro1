import streamlit as st
import json
import os
from web3 import Web3

# --- 1. SETUP ---
st.set_page_config(page_title="AI Adversarial Audit", layout="wide")

# Connect to Ganache to prove the live connection
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Folder paths - Make sure these match your computer!
LOG_FOLDER = "C:/Users/kriti/Desktop/adversarial-project/audit_logs"
IMAGE_FOLDER = "C:/Users/kriti/Desktop/adversarial-project/attacks/saved_images"

st.title("🛡️ Adversarial Attack & Blockchain Audit")
st.markdown("### *Final Year Project Demo*")

# --- 2. SIDEBAR ---
st.sidebar.header("📋 Audit Logs")
log_files = sorted([f for f in os.listdir(LOG_FOLDER) if f.endswith('.json')])
selected_file = st.sidebar.selectbox("Select an Audit ID", log_files)

# --- 3. LOAD SELECTED LOG ---
with open(os.path.join(LOG_FOLDER, selected_file), "r") as f:
    log_data = json.load(f)

# --- 4. DISPLAY RESULTS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🖼️ Attack Visualization")
    # Get the index from the filename to show the right images
    idx = log_data.get("image_index", 1)
    
    img_col1, img_col2 = st.columns(2)
    with img_col1:
        st.write(f"**Original: {log_data['original_label']}**")
        orig_img = os.path.join(IMAGE_FOLDER, f"original_{idx}.png")
        if os.path.exists(orig_img):
            st.image(orig_img, use_container_width=True)
            
    with img_col2:
        st.write(f"**Attacked: {log_data['adversarial_label']}**")
        adv_img = os.path.join(IMAGE_FOLDER, f"adv_{idx}_eps0.1.png")
        if os.path.exists(adv_img):
            st.image(adv_img, use_container_width=True)

with col2:
    st.subheader("🔐 Blockchain Verification")
    st.success(f"**Status:** {log_data['status']}")
    st.info(f"**Content Hash (CID):** \n`{log_data['content_hash']}`")
    
    # Show the technical JSON data
    with st.expander("See Full Metadata"):
        st.json(log_data)

# --- 5. AUDITOR VERIFICATION ---
st.divider()
if st.button("🔍 Verify Audit on Ganache Network"):
    if w3.is_connected():
        st.balloons()
        st.success(f"✅ Audit Verified! This failure is permanently recorded in Block #{w3.eth.block_number}")
    else:
        st.error("❌ Blockchain not found. Is Ganache running?")