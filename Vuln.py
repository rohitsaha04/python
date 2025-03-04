import requests
import subprocess
import nmap

# Scanning for SQL Injection
def check_sql_injection(url):
    payload = {"username": "' OR '1'='1' -- ", "password": "password"}
    response = requests.post(url, data=payload)
    if "Welcome" in response.text:
        print("Potential SQL Injection vulnerability detected!")
    else:
        print("No SQL Injection vulnerability detected.")

# Checking for XSS (Cross-Site Scripting) Vulnerabilities
def check_xss(url, payload):
    response = requests.get(url + payload)
    if payload in response.text:
        print("Potential XSS vulnerability detected!")
    else:
        print("No XSS vulnerability detected.")

# Analyzing Python Dependencies for Known Vulnerabilities
def check_dependencies():
    subprocess.run(["pip", "install", "safety"])
    subprocess.run(["safety", "check"])

# Checking for Open Ports and Services
def scan_open_ports(target):
    nm = nmap.PortScanner()
    nm.scan(target, '1-1024')
    for host in nm.all_hosts():
        print(f"Host: {host}")
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in ports:
                print(f"Port: {port} - State: {nm[host][proto][port]['state']}")

# Example Usage
if __name__ == "__main__":
    url = "http://example.com/login"
    check_sql_injection(url)
    
    url = "http://example.com/search?q="
    payload = "<script>alert('XSS')</script>"
    check_xss(url, payload)
    
    check_dependencies()
    
    target = "127.0.0.1"
    scan_open_ports(target)
