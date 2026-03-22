import json
import os
from web3 import Web3

# 1️⃣ Connect to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
if w3.is_connected():
    print("✅ Connected to Ganache")
else:
    print("❌ Failed to connect. Check Ganache is running.")

# 2️⃣ Load the Contract Address and ABI
with open("blockchain/contract_info.json", "r") as f:
    contract_info = json.load(f)

contract_address = contract_info["address"]
abi = contract_info["abi"]

# Create the contract object
contract = w3.eth.contract(address=contract_address, abi=abi)

# 3️⃣ Get the folder where your JSON audit logs are
log_folder = "C:/Users/kriti/Desktop/adversarial-project/audit_logs"

# Pick the first Ganache account to pay for transactions
account = w3.eth.accounts[0]
print(f"📡 Sending audit hashes to Smart Contract at: {contract_address}")
print(f"🏦 Using Account: {account}\n")

# 4️⃣ Loop through JSON logs and store hashes on-chain
for file in sorted(os.listdir(log_folder)):
    if file.endswith(".json"):
        with open(os.path.join(log_folder, file), "r") as f:
            log = json.load(f)
            hash_to_store = log["content_hash"]
            
            print(f"⏳ Storing Hash: {hash_to_store[:15]}...")

            try:
                # Call the smart contract function
                tx_hash = contract.functions.storeHash(hash_to_store).transact({'from': account})
                # Wait for confirmation
                w3.eth.wait_for_transaction_receipt(tx_hash)
                print("✅ Stored successfully")
            except Exception as e:
                print(f"❌ Failed to store: {e}")

# 5️⃣ Verify total stored audits
try:
    count = contract.functions.getAuditCount().call()
    print(f"\n✅ SUCCESS! {count} audit hashes are now permanently locked in the Blockchain.")
except Exception as e:
    print(f"❌ Failed to fetch audit count: {e}")