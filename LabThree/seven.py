'''
Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters
'''
def case(string):
    uppers = 0
    lowers = 0
    for char in string:
        if char.islower():
            lowers += 1
        elif char.isupper():
            uppers += 1
            return(uppers , lowers)
a=input("enter a string: ")
print(case(a))







a=input("enter a string: ")