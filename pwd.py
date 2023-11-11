def is_strong_password(password):
    # Check if the password is strong (at least 8 characters, with both letters and numbers)
    return len(password) >= 8 and any(c.isalpha() for c in password) and any(c.isdigit() for c in password)

user_password = "Passw0rd"
if is_strong_password(user_password):
    print("Password is strong.")
else:
    print("Password is weak. Please use a stronger password.")
