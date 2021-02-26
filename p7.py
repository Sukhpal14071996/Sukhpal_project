# Program 7: Write a program to display ASCII code of a character and vice versa.

#CODE
y = "y"
while(y=="y" or y=="Y"):
    ch = int(input("Enter: \n1: ASCII code to Character\n2: Character to ASCII Code\nEnter your choice : "))
    if ch == 1:
        n = int(input("Enter ASCII code: "))
        print("Character for ASCII code", n, "is", chr(n))
    elif ch == 2:
        n = input("Enter Character: ")
        print("ASCII code for Character", n, "is", ord(n))
    else:
        print("Enter correct choice ...")
    y = input("Press y to continue : ")
    
#OUTPUT