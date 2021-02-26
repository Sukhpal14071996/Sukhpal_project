#Program 3: To compute the roots of a quadratic equation.
# CODE
import math
a=int(input("\nEnter coefficient of x^2: \n"))
b=int(input("\nEnter coefficient of x:\n"))
c=int(input("\nEnter constant:\n"))
disc=(b*b) -(4*a*c)
if(disc>0):
    root1= ( -b + math.sqrt(disc) ) / ( 2 * a )
    root2= ( -b - math.sqrt(disc) ) / ( 2 * a )
    print("\n2 roots are ", root1 , " and ", root2)
elif(disc<0):
    real= -b /(2*a)
    img= math.sqrt(-disc)/(2*a)
    print("\n2 roots are \n", real , " + i(", img , ")\n and", real , " -i(", img, ")")
else:
    root= -b/ (2*a)
    print("\nCoinciding roots are ", root, " and ", root)

# OUTPUT
