def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

weight = 70  # in kilograms
height = 1.75  # in meters
bmi = calculate_bmi(weight, height)
print(f"The BMI is: {bmi:.2f}")
