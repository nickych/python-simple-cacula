import math

def main_cylinder(radios, hight):
  volume = math.pi * radios ** 2 * hight
  return volume

radius = int(input("Enter the radius: "))
hight = int(input("Enter the hight: "))
volum = main_cylinder(radios, hight)
print(f"The volume of the cylinder is: {volume}")

