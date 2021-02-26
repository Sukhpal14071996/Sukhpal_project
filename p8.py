# Program 8: Write a Program to check if the entered number is Armstrong or not.

#CODE
n = input("Enter a number: ")
s= 0
for i in n:
    s = s + pow(int(i),3)
if s == int(n):
    print("The given number", n, "is an armstrong number")
else:
    print("The given number", n, "is not an armstrong number")
#OUTPUT