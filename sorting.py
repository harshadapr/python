# List of numbers to be sorted
numbers = [5, 2, 9, 1, 5, 6]

# Sort the list in ascending order
ascending_sorted = sorted(numbers)

# Sort the list in descending order
descending_sorted = sorted(numbers, reverse=True)

# Alternatively, you can sort the list in-place
numbers.sort()  # Ascending order
numbers.sort(reverse=True)  # Descending order

# Print the sorted lists
print("Ascending Order:", ascending_sorted)
print("Descending Order:", descending_sorted)

# If you want to sort the original list, you can use the sort() method
print("Original List (Ascending):", numbers)
