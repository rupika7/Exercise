'''
Write a Python program to convert temperatures to and from celsius,
fahrenheit.
 C = (5/9) * (F - 32)
'''
def temp():
    F = float(input("enter temperature in Fahrenheit: "))
    C = (5/9)*(F - 32)
    print(f"the temperature in Celcius is: {C}")
temp()
