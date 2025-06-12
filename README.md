# 🛡️ Log File Analyzer

A Python script to parse system logs and identify suspicious activity, such as repeated failed login attempts.

## 🔧 How It Works
- Scans logs (e.g., `/var/log/auth.log`)
- Detects:
  - Failed SSH login attempts
  - Authentication failures

## 🛠️ Usage

```bash
python3 analyzer.py
