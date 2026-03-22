import os
import json

log_folder = "audit_logs"

total = 0
success = 0

for file in os.listdir(log_folder):
    if file.endswith(".json"):
        total += 1
        with open(os.path.join(log_folder, file)) as f:
            data = json.load(f)
            if data["status"] == "SUCCESS":
                success += 1

print(f"Total Attacks Logged: {total}")
print(f"Successful Attacks: {success}")
print(f"Attack Success Rate: {(success/total)*100:.2f}%")