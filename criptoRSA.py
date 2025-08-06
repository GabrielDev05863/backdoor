from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os


def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    with open("private.pem", "wb") as f:
        f.write(private_key)
    public_key = key.publickey().export_key()
    with open("public.pem", "wb") as f:
        f.write(public_key)




def encrypt_message(message, public_key_path="public.pem"):
    with open(public_key_path, "rb") as f:
        public_key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message



def decrypt_message(encrypted_message, private_key_path="private.pem"):
    with open(private_key_path, "rb") as f:
        private_key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()


# Example usage
if __name__ == "__main__":
    generate_keys()
    message = input("digite a mesnagem para criptografar:")
    encrypted = encrypt_message(message)
    print(f"Mensagem criptografada: {encrypted}")   


    decrypt_message = decrypt_message(encrypted)
    print(f"Mensagem descriptografada: {decrypt_message}")  