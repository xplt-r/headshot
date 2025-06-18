# HeadShot 🔍📸

A minimal, fast, headless screenshot tool using Chromium — built for bug bounty hunters and CLI users.

## Features
- ⚡ Lightweight and fast
- 📄 Accepts both single URL (`-u`) and list (`-l`)
- 🖼️ Output saved in `screenshots/` folder
- 🔒 Sanitized file names for clean storage
- 🐧 Works on Kali, ParrotOS, and most Debian-based distros

## Requirements
- `chromium` (or `google-chrome`), Install: ```sudo apt install chromium```
- Python 3.6+

## 📦 Usage Examples
Single URL:
```
python3 headshot.py -u https://example.com
```
List of URLs:
```
python3 headshot.py -l hosts.txt
```

