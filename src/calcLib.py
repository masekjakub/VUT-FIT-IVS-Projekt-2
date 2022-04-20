"""
Project name: VUT FIT IVS 2. Project
File: calcLib.py
Date: 20.4.2022
Authors: Filip Polomski xpolom00
         Martin Zelenák xzelen27
Description: Math library for calculator 
"""

##
# @file calcLib.py
# @brief Math library for calculator
# @author Filip Polomski and Martin Zelenák

from math import log

## The function adds two operads
# @param x First operand
# @param y Second operand
# @return Returns sum of operands
def add( x , y ):
    return x + y

## The function subtracts one operand from another
# @param x First operand
# @param y Second operand
# @return Returns sum of operands
def sub(x,y):
    return x - y

## The function multiplies two operads
# @param x First operand
# @param y Second operand
# @return Returns the result after multiplication 
def mul(x,y):
    return  x * y

## The function divides one operand by another
# @param x First operand
# @param y Second operand
# @return Returns the result after division
def div(x,y):
    return x / y 

## The function makes a factorial of a single operand. Function also handles wrong inputs and returns error message.
# @param x Operand 
# @return Returns the result of factorial
def fac(x):
    result = x
    if x == 1 or x == 0:
        result = 1
    elif not(isinstance(x, int)) or x < 0:
        raise TypeError("Number must be integer greater than or equal zero!")
    else:
        while x > 0:
            x -= 1
            if x == 0:
                break
            result = result * x
    return result

## The function squares operand by input number n.
# @param x Operand
# @param n Number
# @return Returns the result after power
def pwr(x,n):
    if n < 0:
        x = 1 / x
        n = -n
    return x**n

## The function roots operand by input number n. Function also handles wrong inputs and returns error messages. 
# @param x Operand
# @param n Number
# @return Returns the result after root
def root(x,n):
    if n == 0:
        raise TypeError("Root number cannot be zero (division by zero)!")
    elif (n % 2) == 0 and x < 0:
        raise TypeError("Under the square root cannot be negative number!")
    elif n == 1:
        return x
    elif (n % 2) == 1 and x < 0: 
        x = -x #Changes number's sign, because negative number would return number in complex form
        n = 1 / n 
        x = x**n
        return -x
    else:
        n = 1 / n
    return x**n

## The function makes natural logarithm of operand. Function also handles wrong inputs and returns error message.
# @param x Operand
# @return Returns result of natural logarithm
def ln(x):
    e = 2.718281828459045 #Euler's number
    if x <= 0: 
        raise TypeError("The natural logarithm is defined only in the interval (0, ∞)")
    else:
        x = log(x, e)
    return x

## The function returns value of pi.
# @return Returns value of pi
def pi():
    pi = 3.141592653589793
    return pi

# End of file calcLib.py