import json
import os
import hashlib

# -------------------------------
# 1. SETUP
# -------------------------------
# Absolute path to your audit_logs folder
log_folder = "C:/Users/kriti/Desktop/adversarial-project/audit_logs"

blockchain = []

# -------------------------------
# 2. CREATE BLOCKCHAIN
# -------------------------------
# Sort files by name to keep order
for file in sorted(os.listdir(log_folder)):
    if file.endswith(".json"):
        with open(os.path.join(log_folder, file)) as f:
            log = json.load(f)

            # Each block has previous hash + current data
            block = {
                "previous_hash": blockchain[-1]["hash"] if blockchain else "0",
                "data": log,
            }

            # Compute current block hash
            block_string = json.dumps(block, sort_keys=True).encode()
            block_hash = hashlib.sha256(block_string).hexdigest()
            block["hash"] = block_hash

            blockchain.append(block)

print(f"✅ Blockchain created with {len(blockchain)} blocks")

# -------------------------------
# 3. SAVE BLOCKCHAIN
# -------------------------------
output_path = "C:/Users/kriti/Desktop/adversarial-project/blockchain/blockchain.json"
with open(output_path, "w") as f:
    json.dump(blockchain, f, indent=4)

print(f"📦 Blockchain saved as {output_path}")