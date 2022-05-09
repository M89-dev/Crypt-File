from cryptography.fernet import Fernet
import string
import os
import random 

class Gestionnaire_Password():
    def __init__(self, passwordFile):
        self.passwordFile = passwordFile

    def loadPassword(self, login, password):
        with open(self.passwordFile + "password.txt", "a") as file_data:
            file_data.write("{} : {}\n".format(login, password))
            file_data.close()

    def createKey(self):
        key = Fernet.generate_key()
        if (os.path.exists(self.passwordFile + "key.key")):
            print("Une clé est déja sur votre système")
        else:
            with open(self.passwordFile + "key.key", "wb") as key_file:
                key_file.write(key)
                key_file.close()

    def changeKey(self):
        key = Fernet.generate_key()
        with open(self.passwordFile + "key.key", "wb") as key_file:
            key_file.write(key)
            key_file.close()

    def loadKey(self):
        return open(self.passwordFile + "key.key", "rb").read()

    def encryptFile(self):
        key = self.loadKey()
        f = Fernet(key)

        try:
            with open(self.passwordFile + "password.txt", "rb") as file_data:
                data_text = file_data.read()
                data_encrypt = f.encrypt(data_text)
                file_data.close()
            
            with open(self.passwordFile + "password.txt", "wb") as file_data:
                file_data.write(data_encrypt)
                file_data.close()
        
        except FileNotFoundError:
            print("Création du fichier password")
            with open('password.txt', 'w') as file:
                file.write("Gestionnaire de mot de passe :")

    def decryptFile(self):
        key = self.loadKey()
        f = Fernet(key)

        try:
            with open(self.passwordFile + "password.txt", "rb") as file_data:
                data_text = file_data.read()
                data_decrypt = f.decrypt(data_text)
                file_data.close()

            with open(self.passwordFile + "password.txt", "wb") as file_data:
                file_data.write(data_decrypt)
                file_data.close()
        except ValueError:
            print("Mauvaise clé de chiffrement")

    def generatePassword(self, lenght, login):
        ascii_letter = string.ascii_letters
        digit = string.digits
        ponctuation = string.punctuation

        list_string = ascii_letter + digit + ponctuation
        
        password = "".join(random.sample(list_string, lenght))
        self.loadPassword(login, password)
        

Gestionnaire = Gestionnaire_Password("URL")
Gestionnaire.decryptFile()