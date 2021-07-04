'''
Write a function called showNumbers that takes a parameter called limit.
It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
For example, if the limit is 3, it should print:0 EVEN1 ODD2 EVEN
'''
def showNumbers(limit):
    print("0 EVEN")
    for i in range(1, limit):
        if i//2:
            print(i, "EVEN")
        else:
            print(i, "ODD")
a=int(input("enter a number:"))
print(showNumbers(a))
