!!! success ""
    PGM is very easy to use, seriously ! 

### How to generate a password
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
Magical, right? As you can see, using PGM is not complicated.