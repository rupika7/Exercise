'''
write a Python program that accepts a word from the user and reverse it.
'''
def rev(word):
    reverse = word[::-1]
    print(f"the reverse of the word is {reverse} ")
word=input("enter a word: ")
rev(word)