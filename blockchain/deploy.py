import json
from web3 import Web3
from solcx import compile_standard, install_solc

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
if w3.is_connected():  # ✅ use is_connected() instead of isConnected()
    print("✅ Connected to Ganache")
else:
    print("❌ Failed to connect")

# 2️⃣ Install Solidity Compiler
print("⏳ Installing Solidity compiler...")
install_solc("0.8.0")

# 3️⃣ Read the Contract File
with open("blockchain/AuditNotary.sol", "r") as file:
    contract_source = file.read()

# 4️⃣ Compile the Contract
print("⚙️ Compiling contract...")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"AuditNotary.sol": {"content": contract_source}},
        "settings": {
            "outputSelection": {"*": {"*": ["abi", "evm.bytecode"]}}
        },
    },
    solc_version="0.8.0",
)

# 5️⃣ Extract ABI and Bytecode
abi = compiled_sol["contracts"]["AuditNotary.sol"]["AuditNotary"]["abi"]
bytecode = compiled_sol["contracts"]["AuditNotary.sol"]["AuditNotary"]["evm"]["bytecode"]["object"]

# 6️⃣ Deploy to Ganache
all_accounts = w3.eth.accounts
account = all_accounts[0]  # ✅ Pick the first account only

print(f"🏦 Using Account: {account}")
print("🚀 Deploying contract...")

# Initialize contract
AuditNotary = w3.eth.contract(abi=abi, bytecode=bytecode)

# Send transaction to deploy
tx_hash = AuditNotary.constructor().transact({'from': account})

# Wait for confirmation
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"✅ Contract deployed at: {tx_receipt.contractAddress}")

# 7️⃣ Save contract info
with open("blockchain/contract_info.json", "w") as f:
    json.dump({"address": tx_receipt.contractAddress, "abi": abi}, f)

print("💾 Contract info saved to contract_info.json")