# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:

age = float(input("Enter Your Age: "))
if age < 0:
    print("That doesn't seem right..")
elif age <= 12:
    print("You're Child")
elif age <= 19:
    print("You're Teenager")
elif age <= 59:
    print("You're Adult")
elif age <= 100:
    print("You're Senior")
else :
    print("You're Now An Elder")