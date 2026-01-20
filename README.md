# Caesar CLI

A simple terminal-based Caesar Cipher tool written in Python.

Encrypt and decrypt text directly from your terminal. Supports uppercase, lowercase, numbers, symbols, and colorful CLI banners.

---

## Features

- Encrypt and decrypt text using Caesar Cipher
- Supports both uppercase and lowercase letters
- Numbers and symbols remain unchanged
- Colorful terminal banners with Colorama
- Simple and interactive CLI menu

---

## Installation (Kali/Linux)

### Option 1: Using a virtual environment (recommended)

# Clone the repo
git clone https://github.com/usaihack/Caesar-CLI.git
cd Caesar-CLI

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install .

# Run the CLI in venv
caesar


### Option 2: Using pipx (global CLI installation)

# Install pipx if not already installed
sudo apt install pipx
pipx ensurepath

# Clone and install
git clone https://github.com/usaihack/Caesar-CLI.git
cd Caesar-CLI
pipx install .

# Run the CLI anywhere
caesar


## Usage

- Run the CLI: caesar
- Choose Encrypt or Decrypt from the menu
- Enter your text and the shift number
- Get the encrypted or decrypted output instantly


## Requirements

- Python 3.x
- Colorama library (pip install colorama)


## Contributing

- Feel free to open issues or pull requests
- Improve banners, colors, or add features
# Run the CLI
caesar
