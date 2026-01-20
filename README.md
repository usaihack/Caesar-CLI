<div align="center">

# 🏛️ Caesar CLI

**A simple, colorful, and interactive terminal-based Caesar Cipher tool.**

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge)](https://github.com/usaihack/Caesar-CLI/graphs/commit-activity)

</div>

---

## 📖 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Requirements](#-requirements)
- [Contributing](#-contributing)

---

## 🧐 About

**Caesar CLI** allows you to encrypt and decrypt text directly from your terminal with ease. It supports uppercase, lowercase, numbers, and symbols, all wrapped in a colorful CLI interface.

---

## 🚀 Features

- 🔐 **Encrypt & Decrypt**: Seamlessly switch between modes.
- 🔠 **Full Support**: Handles uppercase, lowercase letters, numbers, and symbols.
- 🎨 **Visual Appeal**: Beautiful terminal banners using `Colorama`.
- ⚡ **Interactive**: Simple and intuitive CLI menu.

---

## 🛠️ Installation

### Linux / Kali (Recommended)

#### Option 1: Virtual Environment

```bash
# Clone the repository
git clone https://github.com/usaihack/Caesar-CLI.git
cd Caesar-CLI

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install .

# Run the application
caesar
```

#### Option 2: Global Install (pipx)

```bash
# Install pipx (if not installed)
sudo apt install pipx
pipx ensurepath

# Install directly from source
pipx install git+https://github.com/usaihack/Caesar-CLI.git

# Run anywhere
caesar
```

---

## 💻 Usage

Run the tool and follow the on-screen prompts:

```bash
caesar
```

**Example Session:**

```text
[?] Choose an option:
    1. Encrypt
    2. Decrypt
> 1

[?] Enter text to encrypt: Hello World
[?] Enter shift amount: 3

[+] Encrypted Text: Khoor Zruog
```

---

## 📦 Requirements

- **Python 3.x**
- **Colorama** (`pip install colorama`)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

<div align="center">

Made with ❤️ by [usaihack](https://github.com/usaihack)

</div>
