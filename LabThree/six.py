'''
 Write a Python program to reverse a string
'''
def reverse(str):
    s = ""
    for chr in str:
        s = chr + s
    return s

#given string
mystr = "myname"
print("Given String: ", mystr)

# reversed string
print("Reversed String: ", reverse(mystr))