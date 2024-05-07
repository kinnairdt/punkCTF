import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def decrypt_with_rsa(encrypted_data, private_key):
    try:
        decrypted_data = private_key.decrypt(
            encrypted_data,
            padding.PKCS1v15(),
            )
        return decrypted_data
    except Exception as e:
        return None
def load_private_key(file_path):
    with open(file_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key

def decrypt_file(file_path, keys_folder):
    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    for key_file in os.listdir(keys_folder):
        if key_file.endswith("1.txt"):
            key_path = os.path.join(keys_folder, key_file)
            private_key = load_private_key(key_path)
            decrypted_data = decrypt_with_rsa(encrypted_data, private_key)
            if decrypted_data is not None:
                print(f"Successfully decrypted with key: {key_file}")
                return decrypted_data
            else:
                print(f"[!] Failed to decrypt file {key_file}")
    return None

keys_folder = './shade-team-keys/keys/alt/static/' #Change to Key Folder 
encrypted_file_path = 'flag.miami_california' #Flag Path
decrypted_content = decrypt_file(encrypted_file_path, keys_folder)
if decrypted_content:
    print("[*] Decryption successful!")
    
    print(decrypted_content)
else:
    print(f"[!] Decryption failed...")
