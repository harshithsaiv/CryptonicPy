# CryptonicPy/ciphers/caesar.py This is an implementation of Caesar cipher

def caesar_encrypt(text, shift):
    encrypted_text = []
    for char in text:
        if char.isalpha():  # Check if the character is alphabetic
            shift_amount = shift % 26
            start = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - start + shift_amount) % 26 + start)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
