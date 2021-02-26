# Program 12: Write a Program to enter the string and to check if it’s palindrome or not using loop.

#CODE
str1 = input("Enter a string : ")
str2 = ""
for i in str1:
    str2 = i+str2
if str1 == str2:
    print("The given string", str1, "is palindrome")
else:
    print("The given string", str1, "is not palindrome")
    
#OUTPUT