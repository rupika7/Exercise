'''
 Write a Python function to find the Max of three numbers
'''
def max():
    a = int(input("enter number"))
    b = int(input("enter number"))
    c= int(input("enter number"))
    if a>b and a>c:
        print(f"the max number is {a}")
    elif b>a and b>c:
        print(f"the max number is {b}")
    else:
        print(f"the max number is {c}")
max()