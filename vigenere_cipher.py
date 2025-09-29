def vigenere_encrypt(plaintext, key):
    result = ''
    key_index = 0
    key = key.lower()
    
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char.lower()) - shift_base + shift) % 26 + shift_base)
            key_index += 1
        else:
            result += char  # Giữ nguyên các ký tự không phải chữ cái
    return result

def vigenere_decrypt(ciphertext, key):
    result = ''
    key_index = 0
    key = key.lower()
    
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char.lower()) - shift_base - shift) % 26 + shift_base)
            key_index += 1
        else:
            result += char  # Giữ nguyên các ký tự không phải chữ cái
    return result

# Example usage:
if __name__ == "__main__":
    plaintext = "Hello, World!"
    key = "KEY"
    encrypted = vigenere_encrypt(plaintext, key)
    decrypted = vigenere_decrypt(encrypted, key)
    
    print("Original:", plaintext)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
