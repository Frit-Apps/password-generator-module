# This script has been developed by the Frit Apps Organization
# Github: https://github.com/frit-apps
# Repository address: https://github.com/frit-apps/password-generator-module
# Documentation: https://password-generator-module.readthedocs.io/en/latest/
# This is a module that allows you to generate passwords safely and quickly
# Version 0.3.0

import string
import secrets
from cryptography.fernet import Fernet
import re


class Password:

    __key = Fernet.generate_key()

    def generate_password(self, length: int) -> str:

        """
        This function generates a password with the length it receives as an argument.

        Parameters:
            length (int): Password length

        Returns:
            password (str): Password generated
        """

        try:
            chars = list(string.digits) + list(string.ascii_letters) + list(string.printable[62:-9])
            if length >= 4:
                """If the length is greater than or equal to 4"""
                password = ""
                for i in range(length): password += secrets.choice(chars)
                return password
            else:
                raise ValueError("The password must contain at least 4 characters")
        except TypeError:
            """If the user passes a non-numeric value as a parameter"""
            print("Please enter a numeric value")

    def encrypt_password(self, password: str) -> bytes:
        """
        This function encrypts the generated password

        Parameters:
            password (str): The password that has been generated

        Returns:
            encrypted_password (bytes): The encrypted password in bytes
        """
        try:
            f = Fernet(self.__key)
            encrypted_password = f.encrypt(password.encode())
            return encrypted_password
        except AttributeError:
            print("Enter the password generated")

    def decrypt_password(self, encrypted_password: bytes) -> str:
        """
        This function decrypts the password that has been encrypted so that it can be read

        Parameters:
            encrypted_password (bytes): The encrypted password
        Returns:
            password (str): The decrypted password
        """
        try:
            f = Fernet(self.__key)
            decrypted = f.decrypt(encrypted_password)
            password = decrypted.decode()
            return password
        except TypeError:
            print("Enter the encrypted password")

    def check_password(self, password: str):
        """
        This function checks the password strength

        Parameters:
            password (str): The password to be tested
        """
        levels = ("HIGH", "MEDIUM", "LOW")
        try:
            if len(password) >= 8:
                if password.isdigit():
                    print(levels[2])
                elif password.isalpha():
                    print(levels[2])
                else:
                    if re.search('[a-z]', password):
                        if re.search('[A-Z]', password):
                            if re.search('[0-9]', password):
                                if re.search('''[!"#$%&'()*+,-./:;<=>?@[\\]^_`{]''', password):
                                    print(levels[0])
                                else:
                                    print(levels[1])
                            else:
                                print(levels[1])
                        else:
                            print(levels[1])
                    else:
                        print(levels[1])

            elif len(password) >= 6:
                if password.isdigit():
                    print(levels[2])
                elif password.isalpha():
                    print(levels[2])
                else:
                    if re.search('[a-z]', password):
                        if re.search('[A-Z]', password):
                            if re.search('[0-9]', password):
                                if re.search('''[!"#$%&'()*+,-./:;<=>?@[\\]^_`{]''', password):
                                    print(levels[1])
                                else:
                                    print(levels[2])
                            else:
                                print(levels[2])
                        else:
                            print(levels[2])
                    else:
                        print(levels[2])
            else:
                print(levels[2])
        except TypeError:
            print("Please enter a text string")


