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

--------------------------------------------------------------------------------------------------------------------------------------
<img width="1086" height="809" alt="Screenshot 2026-03-22 150942" src="https://github.com/user-attachments/assets/3fcf60c7-2765-4e25-91f8-df191e0b5edf" />


-------------------------------------------------------------------------------------------------------------------------------------
<img width="1357" height="116" alt="Screenshot 2026-03-22 151738" src="https://github.com/user-attachments/assets/43aa9b26-4755-4b2a-8468-1a850f17bc66" />

--------------------------------------------------------------------------------------------------------------------------------------
<img width="1434" height="100" alt="Screenshot 2026-03-22 152427" src="https://github.com/user-attachments/assets/39b86d20-a755-40eb-a09d-d7154496a37f" />

-------------------------------------------------------------------------------------------------------------------------------------
<img width="1051" height="890" alt="Screenshot 2026-03-22 152530" src="https://github.com/user-attachments/assets/d263d4e5-0e7f-40ca-aec6-666129283936" />

-------------------------------------------------------------------------------------------------------------------------------------
<img width="1425" height="117" alt="Screenshot 2026-03-22 152540" src="https://github.com/user-attachments/assets/67f7ff4b-800f-4a6c-94ca-8a55eb008436" />

------------------------------------------------------------------------------------------------------------------------------------
<img width="658" height="706" alt="Screenshot 2026-03-22 153937" src="https://github.com/user-attachments/assets/35227c48-83d6-4153-ad7b-bcb450382ea3" />

-------------------------------------------------------------------------------------------------------------------------------------
<img width="430" height="570" alt="Screenshot 2026-03-22 162242" src="https://github.com/user-attachments/assets/5f4c2adc-23f8-4359-a90b-b051bb9e90ac" />

--------------------------------------------------------------------------------------------------------------------------------------

<img width="1894" height="814" alt="Screenshot 2026-03-22 163244" src="https://github.com/user-attachments/assets/ae829134-c5c9-440f-aed5-a16c21f533ba" />





