# Program 2: Write a menu driven program to enter two numbers and print the arithmetic operations like
# a. + b. – c. * d. / e. // f. %."""
# CODE
y = "y"
while(y=="y" or y=="Y"):
    f1 = float(input("Enter first number : "))
    ch = input("Enter: \na. + \nb. – \nc. * \nd. / \ne. // \nf. %\nYour choice is: ")
    f2 = float(input("Enter second number : "))
    if ch=="a":
        o = "+"
        result = f1+f2
    elif ch=="b":
        o = "-"
        result = f1-f2
    elif ch=="c":
        o = "*"
        result = f1*f2
    elif ch=="d":
        o = "/"
        result = f1/f2
    elif ch=="e":
        o = "//"
        result = f1//f2
    elif ch=="f":
        o = "%"
        result = f1%f2
    else:
        print("Enter correct choice")
        result = "Error"
    print("Result is : ", f1, o, f2, "=", result)
    y = input("Press y to continue : ")

# OUTPUT
