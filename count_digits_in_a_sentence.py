import string

text = input("Enter text: ")

count = 0

for char in text:
    if char in string.digits:
        count += 1

print("Number of digits:", count)