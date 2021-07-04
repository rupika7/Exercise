'''
Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters
'''
def case():
    uppers = 0
    lowers = 0
    for char in string:
        if char.islower():
            lowers += 1
        elif char.isupper():
            uppers += 1
    print('Lowercase characters:', lowers)
    print('Lowercase characters:', uppers)

string=input("enter a string: ")
case()








