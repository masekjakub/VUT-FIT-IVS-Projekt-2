"""
Project name: VUT FIT IVS 2. Project
File: profiling.py
Date: 22.4.2022
Authors: Martin Zelenák xzelen27
Description: Script calculating standard deviation. Script is used for profiling
"""

##
# @file profiling.py
# @brief Script calculating standard deviation used for profiling
# @author Martin Zelenák

"""
This file is part of CubiCulator.
CubiCulator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
CubiCulator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with Foobar. If not, see https://www.gnu.org/licenses/.
    
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

import calcLib
from sys import stdin

## Main function calculating standard deviation.
# @brief Calculates standard deviation from stdin and prints the result to stdout
def main():
    ####################
    #### READ INPUT ####
    ####################
    rawNumbers=""
    for line in stdin:
        rawNumbers+=" "+line
    rawNumbers = rawNumbers.replace(",",".") #Correcting floats
    rawNumbers = rawNumbers.split(" ")  #Split input string into a list

    numbers=[]
    for num in rawNumbers:
        num = num.strip()
        try:
            num=float(num)
        except:
            continue
        else:
            numbers.append(num)

    N=numbers.__len__()
    if N == 0:
        print("No numbers were inputed!")
        exit(1)

    #########
    ### _ ###
    ### X ###
    #########
    avgXi=float(0)
    for x in numbers:
        avgXi = calcLib.add(avgXi,x)
    avgXi = calcLib.div(avgXi,N)

    #################
    ### DEVIATION ###
    #################
    deviation=0

    for x in numbers:   #sum Xi^2
        deviation+=calcLib.pwr(x,2)

    deviation=calcLib.sub(deviation , calcLib.mul( N , calcLib.pwr(avgXi,2) ) )
    deviation=calcLib.div(deviation, calcLib.sub(N,1) )
    deviation=calcLib.root(deviation,2)

    print(deviation)

if __name__ == "__main__":
    main()

### End of file profiling.py ###
