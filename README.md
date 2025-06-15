# Hashpy
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
---

A simple command-line tool to hash and verify passwords using bcrypt, featuring a colorful ASCII art logo and an interactive menu with colored prompts.

---

## Features

- Hash passwords securely with bcrypt (including automatic salt generation).
- Verify passwords against stored bcrypt hashes.
---

## Requirements

- Python 3.6+
- [bcrypt](https://pypi.org/project/bcrypt/)
- [colorama](https://pypi.org/project/colorama/)

---

## Installation

1. Clone the repository or download the script.

2. Install dependencies:

```bash
pip install bcrypt colorama
```

---
## Usage
Run the script with Python:
```bash
python password_hasher.py
```
You will see a colorful ASCII art logo and a menu:
```bash
Password Hashing Menu:
1. Hash a password
2. Verify a password
3. Exit
```
* Choose 1 to hash a password. Enter your password, and the tool will output the bcrypt hash.

* Choose 2 to verify a password. Enter the password and the stored hash to check if they match.

* Choose 3 to exit.
---
## Notes

* Make sure to save your hashed passwords securely.
* The password inputs are not masked (visible) in this version.
