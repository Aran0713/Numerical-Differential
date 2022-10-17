#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from scipy import *
import numpy as np
import matplotlib.pyplot as plt
import math
import time

N = 100
h = (2*np.pi) / N
I = 1/(h**2)
x = np.linspace(-np.pi, np.pi, N) #start, stop, step in radians 

#sin function
def f(x):
    return np.sin(x)

plt.plot(x,f(x), 'g', label = "sin(x)")
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Plot of sin(x)')
plt.legend(bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0)
plt.show() 

#cos function
def F(x):
    return np.cos(x)

plt.plot(x,F(x), 'b', label = "cos(x)")

# 2-point formula derivative
def df2point(x):
    return (f(x+h) - f(x)) / h

plt.plot(x,df2point(x), 'r--', label = "df(x)")

# 3-point formula derivative
def df3point(x):
    return (f(x+h) - f(x-h)) / (2*h)

plt.plot(x,df3point(x), 'g--', label = "df(x)")
plt.xlabel('x')
plt.ylabel('df(x)')
plt.title('Plot of first derivative of sin(x)')
plt.legend(bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0)
plt.show() 

# 2-point formula error
def error2point(x):
    return abs(df2point(x) - F(x))

plt.plot(x, error2point(x), label = "2-point Formula Error") 

# 3-point formula error
def error3point(x):
    return abs(df3point(x) - F(x))
 
plt.plot(x, error3point(x), label = "3-point Formula Error")
plt.xlabel('x')
plt.ylabel('error')
plt.title('Plot of error')
plt.legend(bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0)
plt.show()

#-sinx function
def F2(x):
    return -np.sin(x)

plt.plot(x, F2(x), 'b', label = "-sin(x)") 

# Second derivative of sin(x)
Fendpoint = abs((2*f(-np.pi) - 5*f(-np.pi + h) + 4*f(-np.pi + 2*h) - f(-np.pi + 3*h)) * I)
Lendpoint = abs((2*f(np.pi) - 5*f(np.pi - h) + 4*f(np.pi - 2*h) -f(np.pi - 3*h)) * I)

def ddf(x):
    return (f(x + h) -(2*f(x)) + f(x - h)) * I

plt.plot(x,ddf(x), 'r.', label = "Second derivative of sin(x)") 
plt.plot(-np.pi,Fendpoint, 'r.') 
plt.plot(np.pi,Lendpoint, 'r.') 
plt.xlabel('x')
plt.ylabel('ddf(x)')
plt.title('Plot of ddf(x)')
plt.legend(bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0)
plt.show() 

#Second derivative error
def errorddf(x):
    return abs(ddf(x) - F2(x))
 
plt.plot(x,errorddf(x), label = "Second derivative Error")
plt.plot(-np.pi,Fendpoint - F2(-np.pi),'b') 
plt.plot(np.pi, Lendpoint- F2(-np.pi),'b')
plt.xlabel('x')
plt.ylabel('error')
plt.title('Plot of second derivative error')
plt.legend(bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0)
plt.show() 
