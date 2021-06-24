'''
Given a positive real number, print its fractional part
'''
real_num = float(input("enter a real number: "))
if real_num > 0:
    integer = int(real_num)
    fraction =  real_num - integer
print(f"the fractional part is {fraction}")

#or
import math
num = float(input("Enter any positive real numbers : "))
fractional = math.modf(num)
print(f"Fractional part is {fractional}")
