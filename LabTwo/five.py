'''
For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0
'''
num = int(input("enter the number"))
if num<0:
    print("the number is negative")
elif num>0:
    print("the number is positive")
elif num==0:
    print("the number is zero")