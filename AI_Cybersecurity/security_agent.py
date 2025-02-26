import langgraph
from langchain.tools import Tool
import subprocess
import re

# Function to run Nmap and extract open ports
def run_nmap(target):
    command = f"nmap -p- --open {target}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    open_ports = re.findall(r"(\d+)/tcp\s+open", result.stdout)
    return open_ports if open_ports else ["No open ports found"]

# Function to check SMB vulnerabilities using enum4linux
def check_smb(target):
    print("[+] Checking SMB vulnerabilities...")
    command = f"enum4linux -a {target}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Save results to a file
    with open("smb_scan_results.txt", "w") as f:
        f.write(result.stdout)

    return result.stdout if result.stdout else "No SMB vulnerabilities found."

# Function to check MySQL anonymous login
def check_mysql(target):
    print("[+] Checking MySQL for anonymous access...")
    command = f"mysql -h {target} -u root -e 'SHOW DATABASES;'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Save results to a file
    with open("mysql_scan_results.txt", "w") as f:
        f.write(result.stdout)

    return result.stdout if result.stdout else "No MySQL issues detected."

# Define workflow
def security_workflow(target):
    print(f"Scanning target: {target}")

    # Step 1: Run Nmap
    open_ports = run_nmap(target)
    print(f"Open ports: {open_ports}")

    # Step 2: Run SMB check if port 445 is found
    if "445" in open_ports:
        print("Running SMB vulnerability check...")
        smb_results = check_smb(target)
        print(smb_results)

    # Step 3: Run MySQL check if port 3306 is found
    if "3306" in open_ports:
        print("Running MySQL security check...")
        mysql_results = check_mysql(target)
        print(mysql_results)

if __name__ == "__main__":
    target_ip = "127.0.0.1"  # Change this to your target
    security_workflow(target_ip)
