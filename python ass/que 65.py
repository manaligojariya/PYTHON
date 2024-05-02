# Write a Python program to calculate surface volume and area of a cylinder

import math

def cylinder_surface_area(radius,height):

    surface_area=2*math.pi*radius**2+2*math.pi*radius*height
    
    return surface_area

def cylinder_volume(radius,height):
    volume=math.pi*radius**2*height
    return volume

radius=5
height=10

surface_area=cylinder_surface_area(radius, height)
volume=cylinder_volume(radius,height)

print(f"The surface area of the cylinder is {surface_area:.2f} square units.")
print(f"The volume of the cylinder is {volume:.2f} cubic units.")