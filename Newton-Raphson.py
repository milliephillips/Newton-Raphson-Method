import numpy as np


#Defining the function f(x) and its derivitive
def f(x) :
    return (np.exp(x)*(5-x)) - 5

def fp(x) :
    return (4-x)* np.exp(x)

#Setting initial estimation for x (from the graph in Figure 1 of the report):
x1 = 5

#Setting number of decimal places and maximum number of iterations:
precision = 1.e-6
nmax = 100

diff = 1
xi = x1
counter = 1


while diff > precision and counter < nmax:
    
#^Meaning if the value of x decreases by amount 'diff', this must be less than the precision value of 0.000001 to achieve a value to our desired accuracy- Otherwise the code will repeat until this is true. The code will only continue until it reaches the maximum number of iterations
   
    diff = np.abs((f(xi)/(fp(xi)))/xi)
    x1 = xi - (f(xi)/fp(xi))
    print('Counter, i: %i,    xi: %f,    x(i-1)-x(i): %f,    Precision: %f' % (counter+1, x1, np.abs(f(xi)/fp(xi)), diff))
    xi = x1
    counter += 1