# CryptonicPy/ciphers/vigenere.py

def vigenere_encrypt(text, key):
    encrypted_text = []
    key_length = len(key)
    key_as_int = [ord(i.lower()) - ord('a') for i in key]
    for i, char in enumerate(text):
        if char.isalpha():
            shift = key_as_int[i % key_length]
            start = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def vigenere_decrypt(text, key):
    decrypted_text = []
    key_length = len(key)
    key_as_int = [ord(i.lower()) - ord('a') for i in key]
    for i, char in enumerate(text):
        if char.isalpha():
            shift = key_as_int[i % key_length]
            start = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - start - shift + 26) % 26 + start)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)
