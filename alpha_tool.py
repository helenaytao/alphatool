import os
from cryptography.fernet import Fernet

class AlphaTool:
    def __init__(self, key_file='secret.key'):
        self.key_file = key_file
        self.key = self.load_key()

    def generate_key(self):
        """
        Generates a new encryption key and saves it to a file.
        """
        self.key = Fernet.generate_key()
        with open(self.key_file, 'wb') as key_file:
            key_file.write(self.key)
        print("Encryption key generated and saved to", self.key_file)

    def load_key(self):
        """
        Loads the encryption key from a file.
        """
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as key_file:
                return key_file.read()
        else:
            print("No key found, generating a new key.")
            self.generate_key()
            return self.key

    def encrypt_file(self, file_path):
        """
        Encrypts a file with the loaded encryption key.
        """
        fernet = Fernet(self.key)
        with open(file_path, 'rb') as file:
            file_data = file.read()
        encrypted_data = fernet.encrypt(file_data)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)
        print(f"File {file_path} encrypted successfully.")

    def decrypt_file(self, file_path):
        """
        Decrypts a file with the loaded encryption key.
        """
        fernet = Fernet(self.key)
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        try:
            decrypted_data = fernet.decrypt(encrypted_data)
            with open(file_path, 'wb') as file:
                file.write(decrypted_data)
            print(f"File {file_path} decrypted successfully.")
        except Exception as e:
            print("Decryption failed:", e)

    def protect_directory(self, directory_path):
        """
        Encrypts all files in a given directory.
        """
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                self.encrypt_file(file_path)

    def unprotect_directory(self, directory_path):
        """
        Decrypts all files in a given directory.
        """
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                self.decrypt_file(file_path)

if __name__ == "__main__":
    alpha_tool = AlphaTool()
    directory_to_protect = input("Enter the directory path to protect: ")
    alpha_tool.protect_directory(directory_to_protect)