import os
import sqlite3
import hashlib
import pickle
import threading

# Vulnerable Code with Multiple Security Issues

# 1. SQL Injection
def vulnerable_sql_injection(query):
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{query}'")  # SQL Injection Risk
    return cursor.fetchall()

# 2. Insecure Password Storage (Plaintext)
def insecure_password_storage(username, password):
    with open('users.txt', 'a') as file:
        file.write(f"{username},{password}\n")  # Storing passwords in plaintext

# 3. Insecure Deserialization (Pickle vulnerability)
def insecure_deserialization():
    with open('user_data.pkl', 'rb') as f:
        user_data = pickle.load(f)  # Loading untrusted data using pickle
    print(f"User Data: {user_data}")

# 4. Hardcoded Secrets (Sensitive Information)
API_KEY = "12345myhardcodedsecretkey"  # Sensitive data hardcoded

def use_api_key():
    print(f"Using API Key: {API_KEY}")

# 5. Race Condition
account_balance = 1000

def deposit(amount):
    global account_balance
    balance = account_balance
    balance += amount
    account_balance = balance  # Vulnerable to race conditions

def withdraw(amount):
    global account_balance
    balance = account_balance
    balance -= amount
    account_balance = balance  # Vulnerable to race conditions

# Simulating a race condition
def simulate_transactions():
    threading.Thread(target=deposit, args=(100,)).start()
    threading.Thread(target=withdraw, args=(50,)).start()

# 6. Insecure File Upload (No File Type Validation)
def upload_file(file):
    file_path = f'/uploads/{file.filename}'  # Potential for malicious file upload
    with open(file_path, 'wb') as f:
        f.write(file.read())
    print(f"File uploaded: {file_path}")

# 7. XSS (Cross-Site Scripting Vulnerability)
def display_user_profile(user_input):
    print(f"User Profile: {user_input}")  # No sanitization, susceptible to XSS attacks

# Example: Run vulnerabilities
simulate_transactions()  # Demonstrates a race condition
vulnerable_sql_injection("' OR 1=1 --")  # SQL Injection
insecure_password_storage("admin", "admin123")  # Storing password in plaintext
insecure_deserialization()  # Potential pickle-based vulnerability
use_api_key()  # API Key is hardcoded
display_user_profile("<script>alert('XSS Attack');</script>")  # Potential XSS