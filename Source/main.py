NumberOne = str("")
NumberTwo = str("")
Operation = str("")

print("Welcome To Simple Calculator (Wrote By Python Programming Language)")
print("If You Want To Leave This Program Please Do These Works")
print("In Windows Please Press (Ctrl+C)")
print("In Linux Please Press (Ctrl+C)")
print("In Mac Please Press (Command+C)")

while True:
    # Get NumberOne Value From User
    while True:
        NumberOne = input("Please Enter NumberOne : ")
        try:
            NumberOne = int(NumberOne)
            break
        except:
            print("Error : Please Enter A Number (A Number Is Cantain (1234567890)). Please Try Again.")
            continue

    # Get NumberTwo Value From User
    while True:
        NumberTwo = input("Please Enter Number Two : ")
        try:
            NumberTwo = int(NumberTwo)
            break
        except:
            print("Error : Please Enter A Number (A Number Is Cantain (1234567890)). Please Try Again.")
            continue

    # Get Operation From User
    while True:
        print("1) Sum")
        print("2) Subtraction")
        print("3) Multiplication")
        print("4) Divide")
        Operation = input("Please Enter A Number Of Operation : ")
        try:
            Operation = int(Operation)
            if (Operation < 1) or (Operation > 4):
                print("Error : The Selected Operation Not Valid. Please Try Again.")
                continue
            else:
                break
        except:
            print("Error : Please Enter A Number (A Number Is Cantain (1234567890)). Please Try Again.")
            continue

    # Print Total Of User's Selected Operation
    if Operation == 1:
        Sum = int()
        Sum = NumberOne + NumberTwo
        print(f"Sum Is : {Sum}")

    elif Operation == 2:
        Subtraction = int()
        Subtraction = NumberOne - NumberTwo
        print(f"Subtraction Is : {Subtraction}")

    elif Operation == 3:
        Multiplication = int()
        Multiplication = NumberOne * NumberTwo
        print(f"Multiplication Is : {Multiplication}")

    elif Operation == 4:
        if NumberTwo == 0:
            print("Error : We Can't Divide A Number To Zero. Please Try Again.")
        else:
            Divide = int()
            Divide = NumberOne / NumberTwo
            print(f"Divide Is : {Divide}")