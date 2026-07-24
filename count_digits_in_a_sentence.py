import string

text = input("Enter text: ")

count = 0

count = sum(char.isdigit() for char in text)
print("Number of digits:", count)