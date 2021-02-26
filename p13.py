# Program 13: Write a Program to enter the 5 subjects numbers and print the grades A/B/C/D/E.

#CODE
sub1=int(input("\nEnter marks for Subject 1: "))
sub2=int(input("\nEnter marks for Subject 2: "))
sub3=int(input("\nEnter marks for Subject 3: "))
sub4=int(input("\nEnter marks for Subject 4: "))
sub5=int(input("\nEnter marks for Subject 5: "))
avg=(sub1+sub2+sub3+sub4+sub5) / 5
if(avg>0.8):
 grade='A'
elif(avg>0.6):
 grade='B'
elif(avg>0.45):
 grade='C'
elif(avg>0.33):
 grade='D'
else:
 grade='E'
print("\nThe grade is ",grade,".")


#OUTPUT