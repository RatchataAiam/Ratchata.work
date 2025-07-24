# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        IP = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if IP == "1":
            print("Balance : ",balance)
        elif IP == "2":
            WD = float(input("Withdraw : "))
            if WD < 0:
                print("Withdraw Cannot be less then 0")
                break
            elif WD > balance :
                print("You Cannot Withdraw more then you have!")
                break
            balance =balance - WD
            print("Now You have : ",balance)
        elif IP =="3":
            DP = float(input("Deposit :"))
            if DP < 0:
                print("Deposit Cannot be less then 0")
                break
            balance =balance + DP
            print("Now You have : ",balance)
        elif IP =="4":
            print("Thank You!")
            break
        else :
            print("Please choose 1-4")
else:
    print("Invalid PIN")