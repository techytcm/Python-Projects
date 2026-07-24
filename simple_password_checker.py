import string

password = input("Enter password: ")

has_digit = False

for char in password:
    if char in string.digits:
        has_digit = True

if has_digit:
    print("Password contains a number.")
else:
    print("Password needs at least one number.")