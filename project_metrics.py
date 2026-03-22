import os
import json
import matplotlib.pyplot as plt
import numpy as np
import hashlib

# -------------------------------
# 1. SETTINGS
# -------------------------------
audit_folder = "audit_logs"  # where FGSM logs are
blockchain_file = "blockchain/blockchain.json"  # blockchain file
classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

# -------------------------------
# 2. LOAD ALL AUDIT LOGS
# -------------------------------
logs = []
for file in sorted(os.listdir(audit_folder)):
    if file.endswith(".json"):
        with open(os.path.join(audit_folder, file)) as f:
            logs.append(json.load(f))

print(f"✅ Loaded {len(logs)} attack logs")

# -------------------------------
# 3. OVERALL ATTACK SUCCESS METRICS
# -------------------------------
success_count = sum(1 for log in logs if log["status"] == "SUCCESS")
fail_count = len(logs) - success_count
total = len(logs)

print(f"Total Attacks: {total}")
print(f"Successful Attacks: {success_count}")
print(f"Failed Attacks: {fail_count}")
print(f"Attack Success Rate: {(success_count/total)*100:.2f}%")

# Pie chart: success vs fail
plt.figure(figsize=(6,6))
plt.pie([success_count, fail_count], labels=["Success","Fail"], autopct="%1.1f%%", colors=["#ff6666","#66b3ff"])
plt.title("FGSM Attack Success vs Fail")
plt.savefig("attack_success_pie.png")
plt.close()
print("📊 Saved pie chart: attack_success_pie.png")

# -------------------------------
# 4. PER-CLASS ATTACK SUCCESS
# -------------------------------
class_success = {cls: 0 for cls in classes}
class_total = {cls: 0 for cls in classes}

for log in logs:
    cls = log["original_label"]
    class_total[cls] += 1
    if log["status"] == "SUCCESS":
        class_success[cls] += 1

# Bar chart per class
plt.figure(figsize=(10,5))
success_rates = [class_success[c]/class_total[c]*100 if class_total[c] > 0 else 0 for c in classes]
plt.bar(classes, success_rates, color="#66c2a5")
plt.ylabel("Attack Success Rate (%)")
plt.xlabel("Class")
plt.title("FGSM Attack Success Rate per Class")
plt.savefig("attack_success_per_class.png")
plt.close()
print("📊 Saved bar chart: attack_success_per_class.png")

# -------------------------------
# 5. BLOCKCHAIN INTEGRITY CHECK
# -------------------------------
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

# -------------------------------
# 6. SAVE METRICS SUMMARY
# -------------------------------
metrics_summary = {
    "total_attacks": total,
    "success_count": success_count,
    "fail_count": fail_count,
    "attack_success_rate": (success_count/total)*100,
    "per_class_success_rate": {cls: success_rates[i] for i, cls in enumerate(classes)}
}

with open("metrics_summary.json", "w") as f:
    json.dump(metrics_summary, f, indent=4)
print("📦 Metrics summary saved as metrics_summary.json")

print("\n🏁 All metrics & figures generated successfully!")