'''
Write a python program to check whether the number is Armstrong number or not using function:
[Hint: 153 - 1*1*1 + 5*5*5 + 3*3*3]
'''
def armstrong(digit):
    sum = 0
    # find the sum of the cube of each digit
    n = num
    while n > 0:
        digit = n % 10
        sum += digit ** 3
        n //= 10
    # display the result
    if num==sum:
        return True
    else:
        return False

# take input from the user
num = int(input("Enter a number: "))
print(armstrong(num))