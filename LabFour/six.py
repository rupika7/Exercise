'''
write a Python program to count the number of even and odd numbers from a
series of numbers.
'''
x= [2,4,5,6,9,11,13]
count_even=0
count_odd=0
for i in x:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print(f"odd numbers: {count_odd} even number: {count_even}")