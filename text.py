def duplicate_string(input_string, times):
    if times < 1:
        return "Invalid input: times should be a positive integer"
    
    duplicated_string = input_string * times
    return duplicated_string

# Example usage:
input_string = "Hello, "
times = 3
result = duplicate_string(input_string, times)
print(result)  # Output will be "Hello, Hello, Hello, "
