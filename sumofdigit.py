def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

number = 12345
digit_sum = sum_of_digits(number)
print(f"The sum of digits in {number} is {digit_sum}")
