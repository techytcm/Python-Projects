def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

temp = float(input("Enter Celsius: "))

print("Fahrenheit:", celsius_to_fahrenheit(temp))