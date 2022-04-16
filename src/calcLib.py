#CALC LIBRARY
from math import log

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return  x * y

def div(x,y):
    return x / y 

def fac(x):
    result = x
    if x == 1 or x == 0:
        result = 1
    elif not(isinstance(x, int)) or x < 0:
        raise TypeError("Number must be bigger or equal than zero!")
    else:
        while x > 0:
            x -= 1
            if x == 0:
                break
            result = result * x
    return result

def pwr(x,n):
    if n < 0:
        x = 1 / x
        n = -n
    return x**n

def root(x,n):
    if n < 2 and n != 1:
        raise TypeError("Root number must be bigger or equal than one!")
    elif (n % 2) == 0 and x < 0:
        raise TypeError("Under the square root cannot be negative number!")
    elif n == 1:
        return x
    elif (n % 2) == 1 and x < 0:
        x = -x
        n = 1 / n
        x = x**n
        return -x
    else:
        n = 1 / n
    return x**n

def ln(x):
    e = 2.718281828459045 #Euler's number
    if x <= 0: 
        raise TypeError("The natural logarithm is defined only in the interval") 
    else:
        x = log(x, e)
    return x

def pi():
    pi = 3.141592653589793
    return pi