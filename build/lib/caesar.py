#!/usr/bin/env python3

from colorama import init, Fore, Style
init(autoreset=True)

def encrypt(text, shift):
    result = ''

    for char in text:
        if char.isupper():
            number = ord(char) - ord('A')
            new_number = (number + shift) % 26
            new_char = chr(new_number + ord('A'))
            result += new_char
        
        elif char.islower():
            number = ord(char) - ord('a')
            new_number = (number + shift) % 26
            new_char = chr(new_number + ord('a'))
            result += new_char

        else:
            result += char

    return result


def print_banner():
    print(Fore.CYAN + Style.BRIGHT + r'''
   ___                                     ___   _          _                
  / __|  __ _   ___   ___  __ _   _ _     / __| (_)  _ __  | |_    ___   _ _ 
 | (__  / _` | / -_) (_-< / _` | | '_|   | (__  | | | '_ \ | ' \  / -_) | '_|
  \___| \__,_| \___| /__/ \__,_| |_|      \___| |_| | .__/ |_||_| \___| |_|  
                                                    |_|                      
    ''')

def print_menu():
    print(Fore.GREEN + Style.BRIGHT + '''
-------------------------------------------------
                   MENU
-------------------------------------------------
1. Encrypt Text
2. Decrypt Text
3. Exit
-------------------------------------------------
''')

def print_encrypt_banner():
    print(Fore.YELLOW + Style.BRIGHT + r'''
         ___                                   _   
        | __|  _ _    __   _ _   _  _   _ __  | |_ 
        | _|  | ' \  / _| | '_| | || | | '_ \ |  _|
        |___| |_||_| \__| |_|    \_, | | .__/  \__|
                                 |__/  |_|         
    ''')

def print_decrypt_banner():
    print(Fore.MAGENTA + Style.BRIGHT + r'''
          ___                                   _   
         |   \   ___   __   _ _   _  _   _ __  | |_ 
         | |) | / -_) / _| | '_| | || | | '_ \ |  _|
         |___/  \___| \__| |_|    \_, | | .__/  \__|
                                  |__/  |_|         
    ''')


print_banner()

def main():
    while True:
        print_menu()
        try:
            choice = int(input(Fore.CYAN + 'Enter your choice: '))
        except ValueError:
            print(Fore.RED + 'Invalid input! Enter a number.')
            continue

        if choice == 1:
            print_encrypt_banner()
            text = input(Fore.CYAN + 'Enter the text to Encrypt: ')
            try:
                shift = int(input(Fore.CYAN + 'Enter the shift (number): '))
            except ValueError:
                print(Fore.RED + 'Shift must be a number!')
                continue
            encrypted_text = encrypt(text, shift)
            print(Fore.GREEN + Style.BRIGHT + f'\nEncrypted Text: {encrypted_text}\n')

        elif choice == 2:
            print_decrypt_banner()
            text = input(Fore.CYAN + 'Enter the text to Decrypt: ')
            try:
                shift = int(input(Fore.CYAN + 'Enter the shift (number): '))
            except ValueError:
                print(Fore.RED + 'Shift must be a number!')
                continue
            decrypted_text = encrypt(text, -shift)
            print(Fore.GREEN + Style.BRIGHT + f'\nDecrypted Text: {decrypted_text}\n')

        elif choice == 3:
            print(Fore.CYAN + 'Goodbye!')
            break

        else:
            print(Fore.RED + 'Invalid choice, Try again...\n')

    pass

if __name__ == "__main__":
    main()
