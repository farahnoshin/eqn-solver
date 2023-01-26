import math

"""
# Solving eqn with two unknowns a1x+ b1y+c1=0, a2x+b2y+c2=0
x+y=3, x-y=1
x=2, y=1
"""

a1 = int(input("Enter a1: "))
b1 = int(input("Enter b1: "))
c1 = int(input("Enter c1: "))

a2 = int(input("Enter a2: "))
b2 = int(input("Enter b2: "))
c2 = int(input("Enter c2: "))

p = (a1*b2-a2*b1)
# print(p)

x =(b1*c2-b2*c1)/p
print(x)

y = (c1*a2-c2*a1)/p
print(y)