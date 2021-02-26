# Program 14: Write a program in python language to display the given pattern:
"""
                5
            4   5
        3   4   5
    2   3   4   5
1   2   3   4   5
"""

#CODE
for i in range(1,6):
    for j in range(1, 6-i):
        print("\t",end="")
    for j in range(6-i,6):
        print(j,end="\t")
    print("")
#OUTPUT