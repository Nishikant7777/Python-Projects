# area calculator
import math

# area of the square
def square():
    a=int(input("enter the side : "))
    return a*a
     

# area of the rectangle 

def rectangle():
    x=int(input("enter the length : "))
    y=int(input("enter the width : "))
    return x*y
     

# area of triangle 
def triangle():
    n=int(input("enter the base : "))
    s=int(input("enter the height : "))
    return 0.5*n*s

# area of the circle 
def  circle():
    r=int(input("enter the radius : "))
    return math.pi * r**2

desired_shape=int(input("enter the 1/4 : "))

if desired_shape == 1:
    print(f'the area of the suare is {square()}')
elif desired_shape==2:
    print(f'the the area of rectangle is {rectangle()}')
elif desired_shape==3:
    print(f'the the area of triangle is {triangle()}')
elif desired_shape==4:
    print(f'the the area of circle is {circle()}')
else:
    print("invalid ")


