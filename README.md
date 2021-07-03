# Password Generator Module
An incredible module capable of generating very secure passwords. 
This project has been adapted from the [original version](https://github.com/Mazzya/passwordgenerator), which is an interactive script.

![GitHub release (latest by date)](https://img.shields.io/github/v/release/mazzya/password-generator-module)
![GitHub](https://img.shields.io/github/license/mazzya/password-generator-module)
[![Documentation Status](https://readthedocs.org/projects/password-generator-module/badge/?version=latest)](https://password-generator-module.readthedocs.io/en/latest/?badge=latest)

Visit [Change Log](https://github.com/Frit-Apps/password-generator-module/blob/main/docs/CHANGELOG.md)

Visit the official [documentation](https://password-generator-module.readthedocs.io/en/latest/)

### How to install
[PyPi project](https://pypi.org/project/password-generator-module/)

To install the module, you must type the following command in the console :
```python
pip install password-generator-module
```
### How to use
To use the module, it is necessary to import it before :
```python
from password_generator.password import Password
```
### How to generate a password
```python
# Instantiate the password object
p = Password()

# Let's use the function generate_password () to generate a password of 12 characters
password = p.generate_password(12)

# Show the generated password
print(password)
```
```
> E=Ym*08jYa<I
```
We are actively working on new features that will be available soon. Any contribution is welcome 😃
