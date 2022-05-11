# Required Imports
import numpy as np
import math
import matplotlib.pyplot as plt
from decimal import Decimal

# To find the pairs where sign changes
def find_sign_changes(f, step, a, b):
    pairs = []
    x = a
    while (x < b):
        if (f(x + step)/f(x) < 0):
            pairs.append([x,x+step])
        x += step
    return pairs

# Root Finding Function
def bisect(f, pairs, tolerance):
    zeros = []
    
    for pair in pairs:
        
        midpoint = (pair[1] - pair[0])/2.0 + pair[0]
        
        while (abs(f(midpoint)) > tolerance):
            
            if (f(midpoint)/f(pair[0]) < 0):
                pair[1] = midpoint
            else:
                pair[0] = midpoint

            midpoint = (pair[1] - pair[0])/2.0 + pair[0]
            
        zeros.append(midpoint)
    return zeros


# Defining the constants
a = 1e-10
v0 = 4.0e-17
m = 9.109e-31
h = 1.0546e-34

E = ((math.pi**2) * (h**2))/(2*m*a**2) 
l = math.sqrt(2*m*(E + v0))/h

z0 = a/h*math.sqrt(2*m*v0)
z = a*l


# Q2
x = np.linspace(-1e-10, 1e-10, 10)

z = np.linspace(0, 10, 100)

fz=[]
for i in z:
    if(i==0):
        fz.append(0) # to avoide divide by zero
        continue
    temp = (z0/i)**2-1
    if(temp >= 0):
        fz.append(math.sqrt(temp))
    else:
        fz.append(0)
tanz = np.tan(z)

plt.plot(fz, z, c='b')
plt.plot(tanz, z, c='r')


z = np.linspace(1/50, 8, 50)
fz = list(map(lambda z: math.sqrt((z0/z)**2 - 1), z))
cotz = -1/np.tan(z)

plt.plot(fz, z, c='b')
plt.plot(cotz, z, c='r')


# Q3
z = np.linspace(-8, 8, 50)
zero=np.linspace(0,0,50)
eq_tan=[]
eq_cot=[]
for i in z:
    if(i==0): # to avoide divide by zero 
        eq_tan.append(-1)
        eq_cot.append(-1)
        continue
    temp=(z0/i)**2-1
    eq_tan.append(math.sqrt(temp)-math.tan(i))
    eq_cot.append(math.sqrt(temp)+1/math.tan(i))
plt.plot(eq_tan, z, c='b')
plt.plot(eq_cot, z, c='r')
plt.plot(zero,z,c='g')
_='''
The plot is shown below, there are lines at discontinuous points so those points will also be included as roots,
this is the mistake
'''


# Q4
def bisect(f, pairs, tolerance, max_iter=int(4e2)):
    zeros = []
    
    for pair in pairs:
        
        i=0
        midpoint = (pair[1] - pair[0])/2.0 + pair[0]
        
        while ((abs(f(midpoint)) > tolerance) and i<max_iter):
            
            if (f(midpoint)/f(pair[0]) < 0):
                pair[1] = midpoint
            else:
                pair[0] = midpoint
            i+=1
            midpoint = (pair[1] - pair[0])/2.0 + pair[0]
            
        zeros.append(midpoint)
    return zeros


# Q5
def f_tan(i):
    temp=(z0/i)**2-1
    try:
        return math.sqrt(temp)-math.tan(i)
    except:
        return -1

def f_cot(i):
    temp=(z0/i)**2-1
    try:
        return math.sqrt(temp)+1/math.tan(i)
    except:
        return -1

step=z0/3
a=-8
b=+8
print(bisect(f_tan,find_sign_changes(f_tan,step,a,b),z0/100))
print(bisect(f_cot,find_sign_changes(f_cot,step,a,b),z0/100))


# yes, we found 2+3 roots