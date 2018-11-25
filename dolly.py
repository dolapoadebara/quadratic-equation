from math import *
a = float(input("enter a number"))
b = float(input("enter a number"))
c = float(input("enter a number"))

positive_discriminant = (-b + sqrt(b**b - 4*a*c))/2*a
negative_discriminant = (-b - sqrt(b**b - 4*a*c))/2*a

result = (positive_discriminant, negative_discriminant)
print(result)
                      
                      
