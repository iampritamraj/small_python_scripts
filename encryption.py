import os
import sys
from os.path import expanduser
from cryptography.fernet import Fernet

class Encryptor(object):
    """ Encrypt & Decrypt files """
    def __init__(self):
        self.key = None         # Key to decrypt
        self.encryptor = None   # Object to encrypt

    def key_generator(self):
        """ Generate the key to encrypt & decrypt files """
        self.key = Fernet.generate_key()
        self.encryptor = Fernet(self.key)
    
    def read_key(self, key_file):
        """ Reads the encryption key """
        with open(key_file, "rb") as file:
            self.key = file.read()
            self.encryptor = Fernet(self.key)

    def write_key(self, key_file):
        """ Save encryption key to file """
        with open(key_file, "wb") as file:
            file.write(self.key)
        print(f"Key Generated: {self.key}")
    
    def encrypt_decrypt(self, directory, encrypted=False):
        """ Recursively encrypt or decrypt files in directory """
        for folders, _, files in os.walk(directory):
            for file in files:
                absolute_path = os.path.join(folders, file)

                self.encrypt_file(absolute_path, encrypted=encrypted)
    
    def encrypt_file(self, file_path, encrypted=False):
        """ Encrypt & Decrypt function """
        with open(file_path, "rb+") as file:
            _data = file.read()
            if not encrypted:
                # Encryption
                data = self.encryptor.encrypt(_data)
            else:
                # Decryption
                data = self.encryptor.decrypt(_data)
            file.seek(0)
            file.write(data)

menu = ("""
[Encrypt - Decrypt]
[0] Exit.
[1] Encrypt.
[2] Decrypt.
""")

if __name__ == "__main__":
    while True:
        print(menu)
        crypt = Encryptor()
        try:
            choice = int(input(" > "))
            print("\n")
            if choice == 0:
                sys.exit()
            
            elif choice == 1:
                print("[ ENCRYPTION ]")
                path = input(r"Drag file/folder here: ").strip('"')
                crypt.key_generator()
                crypt.write_key("key_file")
                crypt.encrypt_decrypt(path)

            elif choice == 2:
                print("[ DECRYPTION ]")
                file = input(r"Drag encrypted file here: ").strip('"')
                key = input("Drag key_file here: ")
                crypt.read_key(key)
                crypt.encrypt_decrypt(file, encrypted=True)
            
            else:
                print("Choose from menu!")
                continue
        except ValueError:
            print("Need integer value 0 - 2")
            continue
