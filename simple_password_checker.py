import string

password = input("Enter password: ")

has_digit = False

if any(char.isdigit() for char in password):
    print("Password contains a number.")
else:
    print("Password needs at least one number.")