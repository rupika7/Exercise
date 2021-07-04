'''
Accept string from the user and display only those characters which are present at an even index.
'''
def index(str):
    modified_string = str[0::2]
    print(modified_string)
a = input("Enter a string: ")
index(a)