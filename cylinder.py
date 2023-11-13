import math

def calculate_cylinder_volume(radius, height):
    return math.pi * radius**2 * height

cylinder_radius = 3
cylinder_height = 5
volume = calculate_cylinder_volume(cylinder_radius, cylinder_height)
print(f"The volume of the cylinder is {volume:.2f} cubic units.")
