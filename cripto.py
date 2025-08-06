from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("SecretKey.key", "wb") as key_file:
        key_file.write(key)
    return key  


def load_key():
 return open("SecretKey.Key", "rb").read()


def encrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message



  
def decrypt_message(encrypted_message):
    key = load_key()
    fernet = Fernet(key) 
    decrypt_message = fernet.decrypt(encrypted_message)
    return decrypt_message.decode()

# Test the encryption and decryption functions
if __name__ == "__main__":
    key = generate_key()
    print(f"Generated Key: {key.decode()}")

    message = input("Enter a message to encrypt: ")
    encrypted = encrypt_message(message)
    print(f"Encrypted message: {encrypted.decode()}")

    decrypted = decrypt_message(encrypted)
    print(f"Decrypted message: {decrypted}")