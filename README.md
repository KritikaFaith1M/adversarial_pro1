# Adversarial Attack & Blockchain Audit 🛡️

### **How to setup for Team Members:**
1. **Clone the repo:** `git clone https://github.com/KritikaFaith1M/adversarial_pro1.git`
2. **Install Libraries:** `pip install -r requirements.txt`
3. **Open Ganache:** Ensure Ganache is running on `http://127.0.0.1:7545`.
4. **Deploy Contract:** Run `python blockchain/deploy.py`.
5. **Sync Audits:** Run `python blockchain/record_audits.py`.
6. **Launch Dashboard:** Run `streamlit run app/dashboard.py`.

# Part 2: What your team needs to do to run it
When your team members download (clone) your code, they need to follow these 3 steps to make it work on their laptops:

# 1. Install the "Tools" (Libraries)
They need the same libraries you installed. You should create a file called requirements.txt to make this easy for them.

Run this command in your terminal: pip freeze > requirements.txt

They will run: pip install -r requirements.txt

# 2. Start their own Blockchain
They must install and open Ganache on their own laptops.

Because their Ganache will be empty, they must run your deployment scripts in order:

python blockchain/deploy.py (To create their own Smart Contract).

python blockchain/record_audits.py (To upload the logs to their Ganache).

# 3. Update the Folder Paths
This is the most important part. Your code currently uses:
C:/Users/kriti/Desktop/adversarial-project/...

Their Problem: Their username isn't "Kriti."

The Fix: You should change your code to use Relative Paths instead of absolute ones.

Example: Instead of C:/Users/kriti/.../audit_logs, use ./audit_logs.
