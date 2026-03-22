import json
import hashlib

# 1. LOAD THE SAVED BLOCKCHAIN
blockchain_path = "C:/Users/kriti/Desktop/adversarial-project/blockchain/blockchain.json"

with open(blockchain_path, "r") as f:
    chain = json.load(f)

def calculate_hash(block):
    # We remove the 'hash' key to calculate what the hash SHOULD be
    block_for_hashing = {k: v for k, v in block.items() if k != "hash"}
    block_string = json.dumps(block_for_hashing, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

# 2. THE VERIFICATION ENGINE
print(f"🔍 Starting Audit of {len(chain)} blocks...\n")
is_valid = True

for i in range(len(chain)):
    current_block = chain[i]
    
    # Check 1: Does the current block's data match its hash?
    expected_hash = calculate_hash(current_block)
    if current_block["hash"] != expected_hash:
        print(f"❌ TAMPERING DETECTED at Block {i}!")
        is_valid = False
        break

    # Check 2: Does this block correctly point to the previous block's hash?
    if i > 0:
        previous_block = chain[i-1]
        if current_block["previous_hash"] != previous_block["hash"]:
            print(f"❌ CHAIN BROKEN at Block {i}: Previous hash mismatch!")
            is_valid = False
            break

    print(f"✅ Block {i} Verified. [Hash: {current_block['hash'][:10]}...]")

# 3. FINAL RESULT
if is_valid:
    print("\n🛡️ AUDIT SUCCESSFUL: The Blockchain Ledger is intact and untampered.")
else:
    print("\n🚨 AUDIT FAILED: The security of the audit trail has been compromised.")