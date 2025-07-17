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
print("Select 1 for THB To USD")
print("Select 2 for USD To THB")
X = input("Pls choose Your Faction: ")

if X == "1":
    THB = float(input("Enter Your Money as THB: "))
    print(f"{THB} THB = {THB / 35.5} USD")

elif X == "2":
    USD = float(input("Enter Your Money as USD: "))
    print(f"{USD} USD = {USD * 35.5} THB")