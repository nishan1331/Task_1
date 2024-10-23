# Caesar Cipher Program for Encryption and Decryption

def encrypt(text, shift):
    result = ""
    
    # traverse through each character in the text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Handle non-alphabetical characters (leave unchanged)
        else:
            result += char
            
    return result


def decrypt(text, shift):
    # Decrypt by using the inverse of encryption (negative shift)
    return encrypt(text, -shift)


def main():
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")
        
        elif choice == '3':
            print("Exiting program.")
            break
        
        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
