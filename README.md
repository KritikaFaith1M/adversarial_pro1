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

<img width="496" height="865" alt="Screenshot 2026-03-22 145805" src="https://github.com/user-attachments/assets/9c4f9c39-3174-494f-9bbc-8a85a24fd9ea" />

<img width="496" height="865" alt="Screenshot 2026-03-22 145805" src="https://github.com/user-attachments/assets/88595889-1133-4fa1-8639-50e66815e266" />

<img width="496" height="865" alt="Screenshot 2026-03-22 145805" src="https://github.com/user-attachments/assets/6b0cf70a-9eef-4891-ae85-0b2e78f5f47e" />

<img width="1434" height="100" alt="Screenshot 2026-03-22 152427" src="https://github.com/user-attachments/assets/ac685a60-2c7c-4c1c-8aa2-6cf81151142f" />

<img width="1434" height="100" alt="Screenshot 2026-03-22 152427" src="https://github.com/user-attachments/assets/691ea0b1-0b43-4821-aa74-f7aa3b261a97" />

<img width="1425" height="117" alt="Screenshot 2026-03-22 152540" src="https://github.com/user-attachments/assets/f8d811dc-2bcc-463b-8068-2186c00975be" />

<img width="658" height="706" alt="Screenshot 2026-03-22 153937" src="https://github.com/user-attachments/assets/26e50460-36a0-41f8-94d6-9f8299969741" />

<img width="658" height="706" alt="Screenshot 2026-03-22 153937" src="https://github.com/user-attachments/assets/1169e6f4-4b48-4917-a75c-c952209eb365" />

<img width="658" height="706" alt="Screenshot 2026-03-22 153937" src="https://github.com/user-attachments/assets/cb0b27f2-2db7-4d48-b37e-11e4aaf79e04" />

<img width="658" height="706" alt="Screenshot 2026-03-22 153937" src="https://github.com/user-attachments/assets/a90db632-b148-4e34-9616-99037b060c14" />
