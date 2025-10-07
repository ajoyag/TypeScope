# TypeScope

**TypeScope** is a local **keystroke analysis and monitoring tool** built for cybersecurity research, input behavior analysis, and ethical demonstration of keylogging concepts.  
It allows users to understand how keystroke events can be captured, logged, and analyzed — all within a controlled, visible, and user-consented environment.

---

## 🔍 Overview

TypeScope demonstrates **how keystroke data flows through a system**, and how security professionals can study or detect such behaviors safely.  
This project focuses on transparency, ethical use, and learning — not stealth or misuse.

**Key Features**
- Real-time keystroke capture within the application window  
- Logs each keystroke with timestamp and key code  
- Simple console visualization of input streams  
- Encrypted local storage of logs (`AES-256` optional)  
- Start / Stop control for safe operation  
- CLI flags for quick usage:  
  - `--start` to begin logging  
  - `--stop` to end session  
  - `--view` to view stored logs  

---

## ⚙️ Project Structure

TypeScope/
│
├── typescope.py              # Main script (core application)
├── logger_utils.py           # Encryption, file handling, helper utilities
├── requirements.txt          # Required Python libraries
├── README.md                 # Project documentation
└── logs/
└── keystrokes_<date>.log # Encrypted keystroke logs

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or above
- Works on Windows, macOS, and Linux (tested on Ubuntu 22.04)

### Setup
```bash
git clone https://github.com/<your-username>/TypeScope.git
cd TypeScope
pip install -r requirements.txt
````

---

## ▶️ Usage

### Start logging

```bash
python3 typescope.py --start
```

### Stop logging

```bash
python3 typescope.py --stop
```

### View stored logs

```bash
python3 typescope.py --view
```

During active logging, every keystroke you type in the console will appear along with the time captured.
Example output:

```
[12:30:21] Key pressed: h
[12:30:21] Key pressed: e
[12:30:22] Key pressed: l
[12:30:22] Key pressed: l
[12:30:23] Key pressed: o
```

---

## 📊 Example Log File (Decrypted View)

```
Timestamp           | Key
--------------------|-----
2025-10-07 12:30:21 | h
2025-10-07 12:30:21 | e
2025-10-07 12:30:22 | l
2025-10-07 12:30:22 | l
2025-10-07 12:30:23 | o
```

If encryption is enabled, the saved file will contain cipher text instead of plain text.

---

## 🔒 Ethical Limitations and Security Notice

TypeScope **does not** record inputs globally or silently.
It only logs keystrokes **within its own terminal window** and **requires the user to start and stop it manually**.

This design ensures:

* No background recording
* No remote data transfer
* Fully auditable local storage
* Safe for demonstration, internship, and classroom use

**Why we implemented it this way:**

> The purpose is to show how keylogging *can be built and detected*, not to create or distribute malicious tools.
> This keeps the project educational, legally compliant, and professionally acceptable to show on GitHub or in portfolios.

---

## 🧩 requirements.txt

```
pynput
cryptography
```

---

## 🧠 Learning Objectives

By working on this project, you’ll learn:

* How input events are captured at system level
* Secure logging and encryption practices
* Ethical boundaries of keylogging research
* Forensics and detection of similar behaviors

---

## 🧾 License

This project is licensed under the **MIT License**.
You may use and modify this code for research, learning, or authorized audits.
Unauthorized use for monitoring others without consent is strictly prohibited.

---

## 💼 Author

**Ajoy A G**
Cybersecurity Research Intern | Offensive Security Enthusiast
Mahindra University, Hyderabad
Project under guidance of [Cybersecurity Internship Team / Your Mentor Name]

---

## 🧠 Future Enhancements

* Add visual analytics (key heatmap, typing speed graph)
* Integrate with dashboard for consent-based analysis
* Extend encryption with public-key storage
* Cross-platform GUI (Tkinter or Qt)

---

### ✅ Summary

**TypeScope** bridges cybersecurity education and ethical software design.
It’s a safe, research-grade example of how keylogging works — built with transparency, security, and professional presentation in mind.
