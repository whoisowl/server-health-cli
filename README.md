# 🖥️ Server Health CLI

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

</p>

A lightweight command-line tool written in Python for monitoring system health.

## ✨ Features
- CPU, memory and disk monitoring
- Uptime, hostname and current user
- Top CPU and memory consuming processes
- JSON output
- Watch mode
- Colored terminal output
- Configurable thresholds
- Proper exit codes

## 📷 Screenshots

> Replace this section with terminal screenshots after running the tool.

## 🚀 Installation

```bash
git clone https://github.com/whoisowl/server-health-cli.git
cd server-health-cli
pip install -r requirements.txt
```

## 💻 Usage

```bash
python health_check.py
python health_check.py --json
python health_check.py --watch 5
python health_check.py --cpu-threshold 85 --memory-threshold 80 --disk-threshold 90
```

## 📁 Project Structure

```text
server-health-cli/
├── .github/workflows/ci.yml
├── health_check.py
├── requirements.txt
├── pyproject.toml
├── README.md
├── LICENSE
└── .gitignore
```

## 🛠 Built With
- Python
- psutil
- argparse

## 📜 License
MIT License.

## 👨‍💻 Author
**Arian Salarian**

GitHub: https://github.com/whoisowl

⭐ If you found this project useful, consider starring it!
