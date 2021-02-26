# Program 25: Write a program in python to plot a graph for the function y = x2

#CODE
import matplotlib.pyplot as plt
x= range(-50,50)
y= [i**2 for i in x]
plt.plot(x,y)
plt.show()
#OUTPUT