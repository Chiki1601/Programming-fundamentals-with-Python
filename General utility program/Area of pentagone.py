
#Area of pentagone
from math import sqrt
length = int(input("Enter the value of length:"))
area = (sqrt(5*(5+2*(sqrt(5)))) * length *length)/4
print("Area of pentagone:  {0:.2f}".format(area))