def xor_encrypt_decrypt(text, key):
    result = ''.join(chr(ord(char) ^ key) for char in text)
    return result

# Example usage:
if __name__ == "__main__":
    plaintext = "Hello, World!"
    key = 123  # Một giá trị số cho khóa XOR
    encrypted = xor_encrypt_decrypt(plaintext, key)
    decrypted = xor_encrypt_decrypt(encrypted, key)
    
    print("Original:", plaintext)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
