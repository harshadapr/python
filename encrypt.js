def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            result += shifted
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

message = "HELLO WORLD"
shift_amount = 3
encrypted_message = encrypt(message, shift_amount)
decrypted_message = decrypt(encrypted_message, shift_amount)

print(f"Original message: {message}")
print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {decrypted_message}")
