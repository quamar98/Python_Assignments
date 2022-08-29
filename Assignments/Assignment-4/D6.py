import math
side1 = eval(input("Enter the lenght of first side : "))
side2 = eval(input("Enter the lenght of Second side : "))
side3 = eval(input("Enter the lenght of third side : "))

s = (side1+side2+side3)/2
area = math.sqrt((s*(s-side1)*(s-side2)*(s-side3)))
print("The area of Triangle is %f"%area)
