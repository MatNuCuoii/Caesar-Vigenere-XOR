from caesar_cipher import caesar_encrypt, caesar_decrypt
from vigenere_cipher import vigenere_encrypt, vigenere_decrypt
from xor_cipher import xor_encrypt_decrypt

def main():
    print("Choose an encryption algorithm:")
    print("1. Caesar Cipher")
    print("2. Vigenère Cipher")
    print("3. XOR Cipher")
    
    choice = input("Enter choice (1/2/3): ")
    
    if choice == '1':
        text = input("Enter text: ")
        shift = int(input("Enter shift value: "))
        encrypted = caesar_encrypt(text, shift)
        print("Encrypted:", encrypted)
        print("Decrypted:", caesar_decrypt(encrypted, shift))
    
    elif choice == '2':
        text = input("Enter text: ")
        key = input("Enter key: ")
        encrypted = vigenere_encrypt(text, key)
        print("Encrypted:", encrypted)
        print("Decrypted:", vigenere_decrypt(encrypted, key))
    
    elif choice == '3':
        text = input("Enter text: ")
        key = int(input("Enter XOR key: "))
        encrypted = xor_encrypt_decrypt(text, key)
        print("Encrypted:", encrypted)
        print("Decrypted:", xor_encrypt_decrypt(encrypted, key))
    
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
