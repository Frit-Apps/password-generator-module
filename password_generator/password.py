# This script has been developed by the Frit Apps Organization
# Github: https://github.com/frit-apps
# Repository address: https://github.com/frit-apps/password-generator-module
# Documentation: https://password-generator-module.readthedocs.io/en/latest/
# This is a module that allows you to generate passwords safely and quickly
# Version 0.1.2

import string
import secrets


class Password:

    def generate_password(self, length: int) -> str:

        """
        This function generates a password with the length it receives as an argument.

        Parameters:
            length (int): Password length

        Returns:
            password (str): Password generated
        """

        try:
            chars = list(string.digits) + list(string.ascii_letters) + list(string.printable[:-9])
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
