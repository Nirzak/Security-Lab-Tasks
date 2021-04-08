# -*- coding: utf-8 -*-
"""
@title Encryption and Decryption using Vignere Cipher
@author: [NirZak] (github.com/nirzak)

@details
Vigenere Cipher is a method of encrypting alphabetic text.
It uses a simple form of polyalphabetic substitution.
At different points in the encryption process, the cipher
uses a different alphabet from one of the rows.The alphabet
used at each point depends on a repeating keyword.
for more details here: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

"""

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(text, key):
    amount = 0
    cipher = ''
    for letters in text:
        if letters.upper() in alpha:
            index = alpha.index(letters.upper())
            index += alpha.index(key[amount].upper())
            index %= len(alpha)
            if letters.isupper():
                cipher += alpha[index]
            if letters.islower():
                cipher += alpha[index].lower()
            amount += 1
            if amount == len(key):
                amount = 0
        else:
            cipher += letters
    return cipher

def decrypt(cipher, key):
    amount = 0
    text = ''
    for letters in cipher:
        if letters.upper() in alpha:
            index = alpha.index(letters.upper())
            index -= alpha.index(key[amount].upper())
            index %= len(alpha)
            if letters.isupper():
                text += alpha[index]
            if letters.islower():
                text += alpha[index].lower()
            amount += 1
            if amount == len(key):
                amount = 0
        else:
            text += letters
    return text

def main():
    option = input('''Type "e" if you want to encrypt\nType "d" if you want to decrypt\nType "q" to quit : ''')
    if option == 'e':
        text = input('Enter your message : ')
        key = input('Enter your key : ')
        ciphertext = encrypt(text, key)
        print("Encrypted Text: ", ciphertext)
        main()
    elif option == 'd':
        ciphertext = input('Enter The Ciphertext : ')
        key = input('Enter your key : ')
        text = decrypt(ciphertext, key)
        print("Decrypted Text: ", text)
        main()
    elif option =='q':
        return 0
    else:
        main()
    
if __name__ == "__main__":
    main()