import re

def is_valid_password(password):
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    return re.match(pattern, password) is not None

user_password = "SecurePwd123"
if is_valid_password(user_password):
    print("Password is valid.")
else:
    print("Password is not valid. It should contain at least 8 characters, including a letter and a digit.")
