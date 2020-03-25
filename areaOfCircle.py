# This code section calculates the area of a circle

# user asked to provide the radius of the circle

radius = input("Please Enter the radius of the circle: ")
radius = float(radius)

pi = 22 / 7  # pi defined as 22/7
areaOfCircle = pi * (radius ** 2)  # formula to calculate the area of a circle

print("The area of the circle is {0:.2f} " .format(areaOfCircle))   # to display the area of circle calculated
