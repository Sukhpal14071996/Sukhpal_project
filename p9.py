# Program 9: Write a Program to find factorial of the entered number using recursion. 

#CODE
n = int(input("Enter a number"))
def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
print("Factorial of", n, "is: ", fact(n))
#OUTPUT