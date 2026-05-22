# Vultrex-AI-Scanner (Burp Suite Extension) ⚡

[![Security Status](https://img.shields.io/badge/Security-Verified-brightgreen.svg)]()
[![Powered By](https://img.shields.io/badge/AI-Claude%203.7%20Sonnet-blue.svg)]()
[![Company](https://img.shields.io/badge/Developed%20By-Vultrex%20Sec-orange.svg)]()

**Vultrex-AI-Scanner** is a powerful, context-aware Jython extension for Burp Suite designed to supercharge your manual and automated VAPT (Vulnerability Assessment and Penetration Testing) workflows. Backed by **Claude 3.7**, this extension goes beyond basic fuzzing to analyze complex HTTP requests/responses and discover advanced security flaws.

---

## 🔥 Key Features

* 🧠 **Context-Aware Scanning:** Doesn't just match regex patterns. It understands the application logic (ASP.NET ViewStates, custom API structures, multi-step parameters).
* 🛡️ **WAF & Filter Bypass:** When standard payloads get blocked (e.g., 500 Internal Server Errors), the AI dynamically suggests advanced bypass vectors (SVG events, double encoding, tag variations).
* 🔴 **Critical Flaw Identification:** High-accuracy detection for SQL Injection, SSRF (Cloud Metadata probing), IDOR/OTP logic flaws, and LFI.
* 📊 **Instant VAPT Reporting:** Automatically categories findings into Critical, High, Medium, and Low with ready-to-test Proof of Concept (PoC) payloads.
* 📉 **90% Less Noise:** Eliminates time-wasting false positives by acting as an intelligent second-reviewer.

---


## 🛠️ Installation & Architecture Setup

This extension runs on a secure **Client-Server Architecture**. To protect the core logic and ensure smooth execution, you need to run the local backend server (`osint.py`) and load the client extension into Burp Suite.

### Step 1: Run the Local Backend Server (`ocean.py`)
The `ocean.py` file handles the core processing and data formatting locally on your system.

1. Open your terminal or command prompt.
2. Navigate to the directory containing `osint.py`.
3. Install dependencies (if any) and run the script using Python 3:
   ```bash
   python osint.py


   

## 🚀 How it Works

Unlike traditional scanners that dump thousands of noisy payloads, Vultrex AI Scanner operates via a secure architecture:

1. **Capture:** It intercepts raw traffic inside Burp Suite.
2. **Analyze:** The extension forwards structured telemetry to the Vultrex core engine.
3. **Exploit/Verify:** The AI reviews server behavior (headers, encoding, status codes) to generate pinpoint bypass attacks.

---

## 🛠️ Installation & Setup

### Prerequisites
* Burp Suite (Community or Professional)
* Jython Standalone (Environment configured in Burp)

### Steps
1. Download the latest compiled version (`vultrex_scanner.py` or `.pyc`) from the Releases section.
2. Open Burp Suite -> Go to **Extensions** tab -> Click **Add**.
3. Select Extension Type as **Python** and browse to the downloaded file.
4. Boom! Look at your output console for the Vultrex welcome banner.

---

## ⚠️ Legal Disclaimer

This tool is developed for educational and authorized penetration testing purposes only. Testing targets without explicit written permission is illegal. The developers at Vultrex Sec are not responsible for any misuse or damage caused by this program.

---

## 🤝 Connect with Us

Developed with ❤️ by **Vultrex Sec**. We are building the future of offensive AI security solutions.

* **Website:** vultrexsec.com
* **Founder/CEO:** Deepak Kumar
