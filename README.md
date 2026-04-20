# 🔍 Network Recon & Vulnerability Scanner

A Python-based tool designed to perform basic network reconnaissance by scanning a target system, identifying open TCP ports, detecting running services, and highlighting potential security risks.

This project simulates an initial phase of penetration testing and cybersecurity analysis.


## 🧠 Description

This tool scans a target (IP or domain) to discover open ports and identify associated services such as HTTP, SSH, and FTP.

It also highlights potentially insecure services that may expose systems to common attacks, helping understand real-world security risks.


## 🚀 Features

- TCP port scanning
- Service identification (HTTP, SSH, FTP, etc.)
- Detection of insecure services
- Timeout handling for efficient scanning
- Clean and readable output


## 🛠 Technologies

- Python 3
- Socket library


## ▶️ Usage

```bash
python scanner.py
````

## 📊 Example Output

````
[+] Scanning target: scanme.nmap.org

[OPEN] Port 22 (SSH)
[OPEN] Port 80 (HTTP)

[+] Open ports found: 2
[+] Scan complete
````

## 🔐 Security Insights

The scanner highlights common insecure services:

 - FTP (21) → Unencrypted credentials
 - Telnet (23) → Plaintext communication
 - SMB (445) → Lateral movement risk
 - RDP (3389) → Brute-force attack exposure

## 🎯 Learning Outcome

Through this project, I developed:

 - Understanding of TCP port scanning
 - Basic network reconnaissance techniques
 - Practical use of Python sockets
 - Identification of exposed services and risks
 - Error handling and timeout management

## ⚠️ Ethical Use
This tool is intended for educational purposes only.

Do not scan systems without proper authorization.

## 👤 Author

Victor Carrera
