import random

def generate_unique_numbers(count, start, end):
    if count > (end - start + 1):
        raise ValueError("Cannot generate more unique numbers than the range allows.")
    return random.sample(range(start, end + 1), count)

unique_numbers = generate_unique_numbers(5, 1, 10)
print(f"Unique Random Numbers: {unique_numbers}")
