"""
Project name: VUT FIT IVS 2. Project
File: calcLib.py
Date: 22.4.2022
Authors: Filip Polomski xpolom00
         Martin Zelenák xzelen27
Description: Math library for calculator 
"""

## 
# @file calcLib.py
# @brief Math library for calculator
# @author Filip Polomski and Martin Zelenák

"""
CubiCulator is a desktop program, made by team EXPECT\_EQ(oznuk, false) as a second and final IVS project. It can calculate basic mathematical expressions.
    Copyright (C) 2022 EXPECT\_EQ(oznuk, false) xkucha30 xzelen27 xpolom00 xmasek19

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    
    Contact mail: xkucha30@vutbr.cz

    CubiCulator  Copyright (C) 2022  Kuchař Vojtěch, Zelenák Martin, Polomski Filip, Mašek Jakub
    This program comes with ABSOLUTELY NO WARRANTY;
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.
"""

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

### End of file calcLib.py ###
