while True:
    print()
    print("Welcome to the Bill Spliter App!")
    print()
    print()

    tbill = float(input("Enter total bill amount:"))
    if tbill <= 0:
        print("Please Enter a Valid amount")
    npeple = int(input("Enter number of people:"))
    if npeple <= 0:
        print("PLease Enter a Valid Number")
    tpr = int(input("Enter tip percentage (05/10/15/20):"))
    print()
    print()

    tpr = (tpr/100)*tbill
    tobill = tbill + tpr
    eachamount = tobill/npeple

    print("Tip amount (in ₹):", end=" ")
    print("₹",end="")
    print(tpr)
    print("Total Bill (with Tip):",end=" ")
    print("₹",end="")
    print(tobill)
    print("Each person should pay:",end="")
    print("₹",end=" ")
    print(eachamount)
    print()
    print()
    y = 1
    n = 0

    uchoice = (input("Would you like to calculate another bill? (y/n):"))
    if (uchoice == "n"):
        print("Thank You For Using This App")
    break
