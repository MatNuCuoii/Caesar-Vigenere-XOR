def caesar_encrypt(plaintext, shift):
    result = ''
    for char in plaintext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Giữ nguyên các ký tự không phải chữ cái
    return result

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# Example usage:
if __name__ == "__main__":
    plaintext = "Hello, World!"
    shift = 3
    encrypted = caesar_encrypt(plaintext, shift)
    decrypted = caesar_decrypt(encrypted, shift)
    
    print("Original:", plaintext)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
