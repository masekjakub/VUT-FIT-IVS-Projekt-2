import calcLib
from sys import stdin

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

    #sum Xi^2
    for x in numbers:
        deviation+=calcLib.pwr(x,2)

    deviation=calcLib.sub(deviation , calcLib.mul( N , calcLib.pwr(avgXi,2) ) )
    deviation=calcLib.div(deviation, calcLib.sub(N,1) )
    deviation=calcLib.root(deviation,2)

    print(deviation)

if __name__ == "__main__":
    main()