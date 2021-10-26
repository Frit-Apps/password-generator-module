
# PGM is very easy to use, seriously

## How to generate a password

To generate a password, start by importing the module you just installed:

    from password_generator.password import Password

Once the module is imported, we are going to create an object of type password to start using its functionalities.

    p = Password()

We are almost there! Now you only need to generate the password with the magic functionality. This functionality requires the number of characters that the password will contain, it is mandatory !

    password = p.generate_password(12)

The function returns the generated password, let's see what it has generated !

    @Jju5XBbL377

Success! Magical, right? As you can see, using PGM is not complicated.

---

## How to encrypt a password

If you want to encrypt the password, use the `encrypt_password()` function. Let's see an example:

We start by generating a password

    p = Password()
    password = p.generate_password(12)

This is the password that we will encrypt

    As,%$YF'_R9X

When we have the password generated, we use the function `encrypt_password()` like this

    encrypted_password = p.encrypt_password(password)

Let's see what the encrypted password contains

    b'gAAAAABgxeGoLXm2ZipeY49mxAKR6UDsARB1z2Dm9LJEp3cR1qhk2e7tMXfRBu7pPJJqPx6Ip-zBQ8fGdKJR-BR42EJt5RdOSw=='

Success! As you can see, encrypting passwords with PGM is very easy !

---

## How to decrypt a password

If you want to decrypt a password, use the `decrypt_password()` function. We will use the previous example, so we already have the encrypted password.

Let's see an example :

    password = p.decrypt_password(encrypted_password)

Let's see the decrypted password :

    As,%$YF'_R9X

Success!! Easier, impossible, right?

---

## How to check password strength

It is important to verify the strength of the passwords that are generated, that is why this function exists. There are 3 levels of password strength:

* **High :** The password contains at least 8 characters, it is made up of numbers, letters and special symbols.
* **Medium :** The password contains at least 6 characters, it is made up of numbers, letters and special symbols.
* **Low :** This level is attributed to whose passwords that only contain numbers or only letters or are only composed of 4 characters

Let's see how to check the strength level of the password that we generate with the previous example, this is the password that we are going to test :

    As,%$YF'_R9X

To check the strength level of the password, we will use the `check_password()` function :

    password = "As,%$YF'_R9X"
    p.check_password(password)

If you look at the console, you will see the following :

    HIGH

This message tells us that the password is strong and secure.

---

## Warning

Remember, use strong passwords and change them frequently !
