# 🔍 Network Recon & Vulnerability Scanner

A Python-based tool designed to perform network reconnaissance by scanning a target system and identifying open TCP ports.

This version includes dynamic port range scanning, making it more flexible and closer to real-world usage.



## 🧠 Description

This tool allows users to scan a target (IP or domain) across a custom range of ports to identify open services.

It simulates a basic reconnaissance phase used in cybersecurity and penetration testing.


## 🚀 Features

- Scan custom port ranges
- Identify open TCP ports
- Fast scanning using timeout control
- Clean add readable output


## 🛠 Technologies

- Python 3
- Socket library


## ▶️ Usage

```bash
python scanner.py
````

## 📊 Example

````
[+] Enter target: scanme.nmap.org

[+] Enter start port: 20
[+] Enter end port: 100

````

## 📊 Example Output
````
[OPEN] Port 22 (SSH)
[OPEN] Port 80 (HTTP)

[+] Open ports found: 2
[+] Scan complete
````

## 🎯 Learning Outcome

Through this project, I developed:

 - TCP port scanning techniques
 - BNetwork reconnaissance basics
 - Using Python sockets
 - Handling user input and validation
 - Improving scripts with dynamic functionality

## ⚠️ Ethical Use
This tool is intended for educational purposes only.

Do not scan systems without proper authorization.

## 👤 Author

Victor Carrera