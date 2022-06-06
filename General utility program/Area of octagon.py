
#Area of octagon
from math import sqrt
side = int(input("Enter length of side:"))

Area = 2* (1+ sqrt(2))*side **2
print("Area of octagon is:  {0:.2f} ".format(Area))