def generate_fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return generate_fibonacci_recursive(n - 1) + generate_fibonacci_recursive(n - 2)

num_terms = 8
fibonacci_sequence = [generate_fibonacci_recursive(i) for i in range(num_terms)]
print(f"Fibonacci Sequence (first {num_terms} terms): {fibonacci_sequence}")
