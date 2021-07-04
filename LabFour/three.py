'''
 Write a Python program to guess a number between 1 to 9.
 Note : User is prompted to enter a guess. If the user guesses wrong then the
prompt appears again until the guess is correct, on successful guess, user will
get a "Well guessed!" message, and the program will exit.
'''
import random
random_num=random.randint(1,9)
guess= int(input("enter a guess: "))
i = 1
while random_num!=guess:
    guess=int(input("guess again: "))
    i= i+1
print("well guessed!")

