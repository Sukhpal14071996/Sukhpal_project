# Program 4: Write a menu driven Program to reverse the entered numbers and print the sum of digits entered.
# CODE
def sum_of_digits(n):
    num = 0
    for i in n:
        num = num+int(i)
    return num
    
y = "y"
while(y=="y" or y=="Y"):
    n = input("Enter number: ")
    ch = int(input("Enter: \n1: Reverse Number\n2: Sum of digits"))
    if ch == 1:
        print("Reverse number of", n, "is", n[::-1])
    elif ch == 2:
        print("Reverse number of", n, "is", sum_of_digits(n))
    else:
        print("Enter correct choice ...")
    y = input("Press y to continue : ")
# OUTPUT