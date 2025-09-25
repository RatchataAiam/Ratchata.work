"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""
def Test():
    print("=== PERSONAL INFORMATION VALIDATOR ===")
    Name = str(input("Enter Your name: "))
    ages = int(input("Enter Your age: "))
    Pnumber = str(input("Enter Your phone number: "))

    Name_Valid=True
    for char in Name:
        if char.isalpha()==True or char==" ":
            print("Checking Your Name letters and spaces...")
            Name_Valid=True
        elif char.isalpha()==False:
            print("Name Error!")
            Name_Valid=False
            break

    Ages_Valid=True
    if 18<=ages and ages<=65:
        print("Checking Your Age...")
        Ages_Valid=True
    else:
        print("Age Error!")
        Ages_Valid=False

    Pnumber_check=True
    if len(Pnumber)!=10:
        print("It's not 10 Digits!")
        Pnumber_check=False

        
    Pnumber_valid=True
    for char in Pnumber:
        if char.isdigit()==True:
            print("Checking Your phone number...")
            Pnumber_valid=True
        elif char.isdigit()==False:
            print("Phone number Error!")
            Pnumber_valid=False
            break

    Final=True
    print("Validation Results: ")
    if Name_Valid==True:
        print("Name: Valid (contains only letters and spaces)")
        Final=True
    else:
        print("Something is wrong...")

    if Ages_Valid==True:
        print(f"Age: Valid ({ages} years old)")
        Final=True
    else:
        print("Something is wrong...")

    if Pnumber_valid==True:
        print("Phone: Valid (10-digit number)")
        Final=True
    else:
        print("Something is wrong...")

    if Final==True:
        print("Formatted Information: ")
        print(f"Name: {Name.upper()}")
        if Ages_Valid==False:
            print("Something is wrong...")
        elif ages>30 and ages<=65:
            print("Age Group: Adult (31-65)")
        elif ages<=18 and ages<=30:
            print("Age Group: Young Adult (18-30)")
        if Pnumber_check==True:
            print(f"Phone: +66-{Pnumber[1:]}")
        else:
            print("Something is wrong...")

Test()        