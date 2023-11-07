def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

original_string = "Hello, World!"
reversed_string = reverse_string(original_string)
print(reversed_string) 
