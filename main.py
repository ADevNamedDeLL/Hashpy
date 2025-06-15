import bcrypt
import os
import sys
import time
from colorama import init, Fore, Style

init(autoreset=True)

LOGO = r"""
/$$   /$$  /$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$  /$$     /$$
| $$  | $$ /$$__  $$ /$$__  $$| $$  | $$| $$__  $$|  $$   /$$/
| $$  | $$| $$  \ $$| $$  \__/| $$  | $$| $$  \ $$ \  $$ /$$/ 
| $$$$$$$$| $$$$$$$$|  $$$$$$ | $$$$$$$$| $$$$$$$/  \  $$$$/  
| $$__  $$| $$__  $$ \____  $$| $$__  $$| $$____/    \  $$/   
| $$  | $$| $$  | $$ /$$  \ $$| $$  | $$| $$          | $$    
| $$  | $$| $$  | $$|  $$$$$$/| $$  | $$| $$          | $$    
|__/  |__/|__/  |__/ \______/ |__/  |__/|__/          |__/    
"""

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_logo():
    colors = [
        Fore.RED, Fore.YELLOW, Fore.GREEN,
        Fore.CYAN, Fore.BLUE, Fore.MAGENTA,
        Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX
    ]
    lines = LOGO.split('\n')
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        print(color + line)
    print(Style.RESET_ALL)

def show_menu():
    clear_console()
    print_logo()
    print(Fore.MAGENTA + "Password Hashing Menu:" + Style.RESET_ALL)
    print(Fore.WHITE + "1. Hash a password" + Style.RESET_ALL)
    print(Fore.WHITE + "2. Verify a password" + Style.RESET_ALL)
    print(Fore.WHITE + "3. Exit" + Style.RESET_ALL)

def hash_password(password: str) -> bytes:
    print(Fore.YELLOW + "Hashing password..." + Style.RESET_ALL)
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed

def verify_password(password: str, hashed: bytes) -> bool:
    print(Fore.YELLOW + "Verifying password..." + Style.RESET_ALL)
    return bcrypt.checkpw(password.encode(), hashed)

def main():
    while True:
        show_menu()
        choice = input(Fore.WHITE + "Enter choice: " + Style.RESET_ALL).strip()

        if choice == '1':
            show_menu()
            pwd = input(Fore.WHITE + "Enter password to hash: " + Style.RESET_ALL)
            try:
                hashed = hash_password(pwd)
                print(Fore.GREEN + "Hashed password (save this):" + Style.RESET_ALL)
                print(Fore.GREEN + hashed.decode() + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Error hashing password: {e}" + Style.RESET_ALL)
            input(Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)

        elif choice == '2':
            show_menu()
            pwd = input(Fore.WHITE + "Enter password to verify: " + Style.RESET_ALL)
            stored_hash = input(Fore.WHITE + "Enter stored hash: " + Style.RESET_ALL).encode()
            try:
                if verify_password(pwd, stored_hash):
                    print(Fore.GREEN + "Password is VALID!" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Password is INVALID!" + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Error verifying password: {e}" + Style.RESET_ALL)
            input(Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)

        elif choice == '3':
            print(Fore.MAGENTA + "Exiting..." + Style.RESET_ALL)
            time.sleep(1)
            break

        else:
            print(Fore.RED + "Invalid choice. Please enter 1, 2, or 3." + Style.RESET_ALL)
            input(Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
