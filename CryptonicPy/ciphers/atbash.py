# CryptonicPy/ciphers/atbash.py - This is an implementation of Atbash Cipher

def atbash_cipher(text):
    encrypted_text = []
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(ord('z') - (ord(char) - ord('a')))
            else:
                encrypted_char = chr(ord('Z') - (ord(char) - ord('A')))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)
