print('""""')
print("Personal Finance Calculator")
print("Student: Ratchata Aiamsaart")
print("Date: 27/7/2568")
print("ID: 6730251336")
print("Purpose: Calculate monthly budget and savings")
print('""""')

X = int(input("Enter 1 To continue: "))
if X ==1:
    while True:
        M_IC = float(input("Enter Your Monthly income as THB: "))
        if M_IC < 0:
            print("Monthly income cannot be less then 0....")
            break
        R_C = float(input("Enter Your Monthly housing cost as THB: "))
        if R_C <= 0:
            print("Didn't you need to pay your taxes?")
            break
        F_B = int(input("Enter Your Monthly food budget as THB: "))
        if F_B <= 0:
            print("You can't live without food!")
            break
        T_C = float(input("Monthly transportation expenses as THB: "))
        if T_C < 0:
            print("Transportation expenses cannot be less then 0....")
            break
        elif T_C == 0:
            print("Travel by car could make it in time! trust me :)")
        E_B = int(input("Monthly entertainment budget as THB: "))
        if E_B < 0:
            print("Entertainment budget cannot be less then 0....")
            break
        elif E_B == 0:
            print("You don't have time to rest..I see")
        E_F_P = float(input("Percentage to save for emergency, You can enter up to max 10.5: "))
        if E_F_P > 10.5:
            print("You can only enter up to 10.5!")
            break
        elif E_F_P == 0:
            print("Good Health No Meds!")
        I_P = float(input("Percentage to invest,You can enter up to max 15: "))
        if I_P > 15:
            print("You can only enter up to 15!")
            break
        elif T_C == 0:
            print("Perfect Life Need Nothing More!")
        TFE = R_C + T_C
        TVE = F_B + E_B
        TE = TFE + TVE
        RI = M_IC - TE
        EFA = M_IC * (E_F_P/100)
        IA = M_IC * (I_P/100)
        AFS = RI-EFA-IA
        ER =(TE/M_IC)*100
        print("=== MONTHLY BUDGET REPORT ===")
        print(f"Income: {M_IC:.2f}THB")
        print(f"Fixed Expenses: {TFE:.2f}THB")
        print(f"Variable Expenses: {TVE:.2f}THB")
        print(f"Total Expenses: {TE:.2f}THB")
        print(f"Remaining: {RI:.2f}THB")

        print("=== SAVINGS BREAKDOWN ===")
        print(f"Emergency Fund ({E_F_P:}%): {EFA:.2f}THB")
        print(f"Investment ({I_P:}%): {IA:.2f}THB")
        print(f"Available for Savings: {AFS:.2f}THB")

        print("=== ANALYSIS ===")
        print(f"Expense Ratio: {ER:}%")

        if AFS < 0:
            print("How did You be in deficit?!")
        break
else:
 print("press 1!")