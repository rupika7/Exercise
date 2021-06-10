'''
N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket.
How many apples will each single student get? How many apples will remain in the basket? The program reads the numbers N and K.
It should print the two answers for the questions above.
'''

N = int(input("enter the number of students: "))
K = int(input("enter the number of apples: "))
distribution = K//N
remaining = K%N
print(f"Each students will get {distribution}")
print(f"The remaining apples in the basket are {remaining}")
