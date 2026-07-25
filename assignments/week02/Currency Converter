"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used

"""
conversion_direction = input("1. for THB to USD \n2. for USD to THB \nChoose conversion direction: ")
amount = float(input("Enter the amount to convert: "))
exchange_rate = 35.5

if conversion_direction == "1":
    result = amount / exchange_rate
    print(f"{amount} THB = {result:.2f} USD")
    print(f"Calculation: {amount} / {exchange_rate} = {result:.2f}")
elif conversion_direction == "2":
    result = amount * exchange_rate
    print(f"{amount} USD = {result:.2f} THB")
    print(f"Calculation: {amount} * {exchange_rate} = {result:.2f}")
else:
    print("Invalid conversion direction.")