!!! success ""
    PGM is very easy to use, seriously ! 

#### How to generate a password
!!! Example
    To generate a password, start by importing the module you just installed :
    ```python
    from password_generator.password import Password
    ```
    Once the module is imported, we are going to create an object of type password to start using its functionalities.
    ```python
    p = Password()
    ```
    We are almost there! Now you only need to generate the password with the magic functionality. This functionality requires the number of characters that the password will contain, it is mandatory !
    ```python
    password = p.generate_password(12)
    ```
    The function returns the generated password, let's see what it has generated !
    ```
    @Jju5XBbL377
    ```
!!! success ""
    Magical, right ? As you can see, using PGM is not complicated.

#### How to encrypt a password
!!! Example
    If you want to encrypt the password, use the ```encrypt_password()``` function. Let's see an example :
    
    We start by generating a password : 
    ```python
    p = Password()
    password = p.generate_password(12)
    ```
    This is the password that we will encrypt :
    ```
    As,%$YF'_R9X
    ```
    When we have the password generated, we use the function ```encrypt_password()``` like this :
    ```python
    encrypted_password = p.encrypt_password(password)
    ```
    Let's see what the encrypted password contains:
    ```
    b'gAAAAABgxeGoLXm2ZipeY49mxAKR6UDsARB1z2Dm9LJEp3cR1qhk2e7tMXfRBu7pPJJqPx6Ip-zBQ8fGdKJR-BR42EJt5RdOSw=='
    ```
!!! success ""
    As you can see, encrypting passwords with PGM is very easy!

#### How to decrypt a password
!!! Example
    If you want to decrypt a password, use the ````decrypt_password()```` function. We will use the previous example, so we already have the encrypted password.
    
    Let's see an example :
    
    ```python
    password = p.decrypt_password(encrypted_password)
    ```
    Let's see the decrypted password :
    ```
    As,%$YF'_R9X
    ```
!!! success ""
    Easier, impossible, right ?