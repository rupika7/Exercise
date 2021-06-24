'''
 Given a three-digit number. Find the sum of its digits.
'''
num = int(input("enter a three digit number: "))
a = num//100
print(f"the first digit is {a}")
b = (num//10)%10
print(f"the second digit is {b}")
c = num % 10
print(f"the third digit is {c}")
sum = a + b + c
print(f"the sum of its digit is {sum}")