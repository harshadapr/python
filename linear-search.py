def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

numbers = [10, 20, 30, 40, 50]
target_value = 30
result = linear_search(numbers, target_value)

if result != -1:
    print(f"{target_value} found at index {result}")
else:
    print(f"{target_value} not found in the list")

