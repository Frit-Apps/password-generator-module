# Password Generator Module
An incredible module capable of generating very secure passwords. 
This project has been adapted from the [original version](https://github.com/Mazzya/passwordgenerator), which is an interactive script.

Visit [Change Log]()
### How to install
To install the module, you must type the following command in the console :
```python
pip install password-generator
```
### How to use
To use the module, it is necessary to import it before :
```python
import password_generator
# OR
from password_generator import *
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
> FYsY>uFnHnp^
```