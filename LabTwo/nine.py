'''
 Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else print ‘COMMON YEAR’.
Hint: • a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
• a year is always a leap year if its number is exactly divisible by 400
'''
year = int(input("enter the year: "))
a = year%4
b = year%100
c = year%400
if a==0 and b!=0 and c==400:
    print("LEAP YEAR")
else:
    print("COMMON YEAR")