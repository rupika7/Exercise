'''
Write a Python program to construct the following pattern, using a nested for
loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
def pattern(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print(" ")
    for i in range(n, -1, -1):
        for j in range(0, i + 1):
            print("* ", end ="")
        print(" ")
pattern(5)