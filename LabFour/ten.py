'''
Write a Python program that accepts a string and calculate the number of
digits and letters
'''
string=input("enter a string: ")
count_digit=0
count_letter=0
for i in string:
    if i.isdigit():
        count_digit+= 1
    elif i.isalpha():
        count_letter+=1
print(f"the number of digits: {count_digit} the number of letters: {count_digit}")
