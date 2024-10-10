# Naithen Ramirez, cris padilla 
# Oct 10, 2024 
# This program is a cipher program that allows the user to encrypt or decrypt a message.

from cipher import Cipher  
from caesar import CaesarCipher
from check_input import get_int_range

def main():
    """
    Main function to handle user input for encryption and decryption using Atbash or Caesar cipher.
    """
    while True:
        
        print("Secret Decoder Ring:")
        print("1. Encrypt")
        print("2. Decrypt")
        decoder = get_int_range("Enter 1 or 2: ", 1, 2)
        
        if decoder == 1: # Encrypt
            print('1. Atbash')
            print('2. Caesar')
            encryption_type = get_int_range("Enter 1 or 2: ", 1, 2)
            message = input("Enter message: ")
            
            if encryption_type == 1: # Atbash
                cipher = Cipher()
                encrypted_message = cipher.encrypt_message(message)
                
            elif encryption_type == 2: # Caesar
                shift = get_int_range("Enter shift value: ", 1, 25) 
                cipher = CaesarCipher(shift) 
                encrypted_message = cipher.encrypt_message(message)

            try: # Save encrypted message to file
                with open('message.txt', 'w') as file: 
                    file.write(encrypted_message) 
                print("Encrypted message saved to 'message.txt'.")
            except: 
                print("Error saving encrypted message.")
            
            
        elif decoder == 2: # Decrypt
            print('1. Atbash')
            print('2. Caesar')
            decryption_type = get_int_range("Enter 1 or 2: ", 1, 2)
        
            try: # Read encrypted message from file
                with open('message.txt', 'r') as file: 
                    message = file.read()
            except FileNotFoundError:
                print("No encrypted message found to decrypt.")
                continue
                
            if decryption_type == 1: # Atbash
                cipher = Cipher()
                decrypted_message = cipher.decrypt_message(message)
                print(f"Decrypted message: {decrypted_message}")
                
            elif decryption_type == 2: # Caesar
                shift = get_int_range("Enter shift value: ", 1, 25) 
                cipher = CaesarCipher(shift)
                decrypted_message = cipher.decrypt_message(message)
                print(f"Decrypted message: {decrypted_message}")           
     

if __name__ == "__main__":
    main()