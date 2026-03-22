import json
import os
import matplotlib.pyplot as plt

# -------------------------------
# 1. LOAD ALL AUDIT LOGS
# -------------------------------
log_folder = "audit_logs"
logs = []

for file in os.listdir(log_folder):
    if file.endswith(".json"):
        with open(os.path.join(log_folder, file)) as f:
            logs.append(json.load(f))

# -------------------------------
# 2. CALCULATE SUCCESS / FAIL
# -------------------------------
success_count = sum(1 for log in logs if log["status"] == "SUCCESS")
fail_count = len(logs) - success_count
total = len(logs)

print(f"Total Attacks: {total}")
print(f"Successful Attacks: {success_count}")
print(f"Failed Attacks: {fail_count}")
print(f"Attack Success Rate: {(success_count/total)*100:.2f}%")

# -------------------------------
# 3. PLOT PIE CHART
# -------------------------------
labels = ["Success", "Fail"]
sizes = [success_count, fail_count]
colors = ["#ff6666", "#66b3ff"]

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors)
plt.title("FGSM Attack Success vs Fail (CIFAR-10)")
plt.show()

# -------------------------------
# 4. OPTIONAL: VERIFY BLOCKCHAIN INTEGRITY
# -------------------------------
blockchain_file = "blockchain/blockchain.json"
if os.path.exists(blockchain_file):
    with open(blockchain_file) as f:
        blockchain = json.load(f)

    valid = True
    for i, block in enumerate(blockchain):
        data = block["data"]
        prev_hash = blockchain[i-1]["hash"] if i > 0 else "0"
        block_check = {"previous_hash": prev_hash, "data": data}
        block_string = json.dumps(block_check, sort_keys=True).encode()
        hash_check = hashlib.sha256(block_string).hexdigest()
        if hash_check != block["hash"]:
            print(f"❌ Blockchain tampered at block {i+1}")
            valid = False
            break

    if valid:
        print("✅ Blockchain integrity verified!")
else:
    print("⚠️ Blockchain file not found. Skipping integrity check.")