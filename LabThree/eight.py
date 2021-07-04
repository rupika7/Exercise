'''
 Write a Python function that takes a number as a parameter and check the number is prime or not
'''
def prim(num):
 count=0
 for i in range(2,num-1):
    if num % i==0:
      count=count+1
 if count>=1:
     print('The number is not a prime no')
 else:
     print('The number is a prime number')
num=int(input('Enter a number: '))
prim(num)