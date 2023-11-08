import math

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

radius = 5
area = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} is {area:.2f} square units.")
