'''
Write a Python program to get the Fibonacci series between 0 to 50.
 Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it
'''
n = 50
a = 0
b = 1
sum = 0
count = 1
print(f"Fibonacci series: ", end=' ')
while (sum<=50):
    print(sum, end=' ')
    count+=1
    a=b
    b=sum
    sum=a+b

