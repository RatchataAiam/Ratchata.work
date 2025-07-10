# Exercise 1: Personal Profile Creator
print("=== Personal Profile Creator ===")
# Create a program that asks for:
# - Full name
# - Age
# - Email
# - Phone number
# - Favorite hobby
# Then display it as a profile

# Write your solution here:
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
Age = input("How old are you?: ")
Email = input("Enter your Email: ")
PNumber = input("Enter your phone Number: ")
FH = input("What's your favorite Hobby?: ")

print("=== Personal Profile ===")
print("Full name:", first_name + " " + last_name)
print("Age: ",Age)
print("Email: ",Email)
print("Phone Number: ",PNumber)
print("Favorite hobby: ",FH)