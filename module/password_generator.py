# !/usr/bin/env python
# This script has been developed by Mazzya
# Github : https://github.com/Mazzya
# Repository address : https://github.com/Mazzya/password-generator-module
# This is a module that allows you to generate passwords safely and quickly

import string
import secrets


class Password:

    def generate_password(self, length: int) -> str:
        """ This function generates a password with the length it receives as an argument """
        try:
            chars = list(string.digits) + list(string.ascii_letters) + list(string.printable[:-9])
            if length >= 4:
                """If the length is greater than or equal to 4"""
                password = ""
                for i in range(length): password += secrets.choice(chars)
                return password
            else:
                print("The password must contain at least 4 characters")
        except TypeError:
            """If the user passes a non-numeric value as a parameter"""
            print("Please enter a numeric value")
