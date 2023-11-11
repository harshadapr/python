import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

email_address = "user@example.com"
if is_valid_email(email_address):
    print(f"{email_address} is a valid email address.")
else:
    print(f"{email_address} is not a valid email address.")
