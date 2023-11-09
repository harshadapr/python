def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Division by zero is not allowed."
    except Exception as e:
        return f"An error occurred: {e}"
    return result

numerator = 10
denominator = 0
division_result = divide(numerator, denominator)
print(division_result)
