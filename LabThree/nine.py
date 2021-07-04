'''
 Write a Python function that checks whether a passed string is palindrome or not.
'''
string = input("Please enter your own String : ")
str1 = ""

for i in string:
    str1 = i + str1
print("String in reverse Order :  ", str1)

if(string == str1):
   print("This is a Palindrome string")
else:
   print("This is Not a Palindrome String")
