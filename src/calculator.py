"""
Project name: VUT FIT IVS 2. Project
File: calculator.py
Date: 23.4.2022
Authors: Jakub Mašek xmasek19
Description: Main file of calculator app
"""

##
# @file calculator.py
# @brief Main file of calculator app
# @author Jakub Mašek xmasek19

"""
This file is part of CubiCulator.
CubiCulator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
CubiCulator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with Foobar. If not, see <https://www.gnu.org/licenses/>.
"""

from PyQt5 import QtWidgets
import re
import calcLib
from ui import Ui_calculator
import keyboard
import os

indexesToRemove = [] #array of indexes to be removed
resList=[""]

## Function that adds symbol to input line.
# @param symbol Symbol to be added
def addSymbolToInput(symbol):
    curText = ui.lineInput.text()
    cursorPos = ui.lineInput.cursorPosition()

    curText = curText[0:cursorPos] + str(symbol) + curText[cursorPos:]
    ui.lineInput.setText(curText)
    ui.lineInput.setFocus()
    ui.lineInput.setCursorPosition(cursorPos + len(str(symbol)))

## Function that clears input line.
def clear():
    ui.lineInput.setText("")
    ui.lineInput.setFocus()

## Function deletes character ahead of cursor position.
def backspace():
    curText = ui.lineInput.text()
    cursorIndex = ui.lineInput.cursorPosition()-1
    if cursorIndex == -1:
        ui.lineInput.setFocus()
        return

    ui.lineInput.setText(curText[0 : cursorIndex : ] + curText[cursorIndex + 1 : :])
    ui.lineInput.setFocus()
    ui.lineInput.setCursorPosition(cursorIndex)

## Function that adds previous result to input line.
def ansToInput():
    curText = ui.lineInput.text()
    ui.lineInput.setText(curText + str(resList[ui.resIndex]))
    ui.lineInput.setFocus()

## Function that clears history.
def delHistory():
    ui.textDisplay.clear()
    ui.lineInput.setFocus()

## Function splits expression by operators and special characters, validates expression and makes necessary changes in it. 
# @param expression Math expression to be splitted
# @return Returns splitted expression as array
def splitExprToArr(expression):
        expArr = re.split(r'(\+|-|x|\*|/|!|\^|√|π|pi|ln)', expression)
        
        for i in expArr:
            if i == '':
                expArr.remove('')

        for index,i in enumerate(expArr):

            #if operator x|*|/|+|- is ahead of root or power, adds default value (2) ahead of operator √|^
            if (i == "√" or i == "^") and (index == 0 or re.fullmatch(r'(x|\*|/|\+|-)',expArr[index-1])):
                expArr.insert(index,"2")

            #if char index-1 is x|/|^|ln and index is -|+ and index+1 is number, connect index to index+1
            if (i == "-" or i == "+") and (index == 0 or re.fullmatch(r'(x|/|\^|ln|√)',expArr[index-1])):
                if expArr[index+1].isnumeric():
                    expArr[index] = str(expArr[index]) + str(expArr.pop(index+1))

            #if number is next to pi(on right side), adds mul between it
            if (i == "π" or i == "pi") and not len(expArr)-index-1 == 0 and not re.match(r'(\+|-|x|\*|/|!|\^)',expArr[index+1]):
                expArr.insert(index+1,"x")

            #if number is next to pi(on left side), adds mul between it
            if (i == "π" or i == "pi") and index > 0 and not re.fullmatch(r'(\+|-|x|\*|/|!|\^|√|π|pi|ln)',expArr[index-1]):
                    expArr.insert(index,"x")
        return expArr

## Function removes values on specific indexes from array.
# @param arr Array
# @param indexes Indexes of array to be removed
# @return Returns array with removed indexes
def removeFromArr(arr, indexes):
    for index in indexes:
        arr.pop(int(index))
    indexes.clear()
    return arr

## Function processes operation with highest priority.
# @param expArr Array to be processed
# @return Returns array with processed operations
def processPriority1(expArr):
    for index,i in enumerate(expArr):  
        if i == "!":
            expArr = processOneOperand(expArr, index, "fac", index-1)
            indexesToRemove.insert(0,index-1) 

        if i == "π" or i == "pi":
            expArr = processNoOperand(expArr, index, "pi")
    return expArr

## Function processes operation with 2nd highest priority.
# @param expArr Array to be processed
# @return Returns array with processed operations
def processPriority2(expArr):
    for index,i in enumerate(expArr):   
        if i == "ln":
            expArr = processOneOperand(expArr, index, "ln", index+1)
            indexesToRemove.insert(0,index)

        if i == "^":  
            if re.fullmatch(r'(\+|-|x|\*|/|!|\^|√|π|pi|ln)',expArr[index+1]):
                break  
            expArr = processTwoOperands(expArr, "pwr", index-1,index+1)
            indexesToRemove.insert(0,index-1)
            indexesToRemove.insert(0,index)

        if i == "√":
            if re.fullmatch(r'(\+|-|x|\*|/|!|\^|√|π | pi|ln)',expArr[index+1]):
                break
            expArr = processTwoOperands(expArr, "root", index+1,index-1)
            indexesToRemove.insert(0,index-1)
            indexesToRemove.insert(0,index)
    return expArr

## Function processes operation with 3rd highest priority.
# @param expArr Array to be processed
# @return Returns array with processed operations
def processPriority3(expArr):
    for index,i in enumerate(expArr):
        if i == "x" or i == "*":
            expArr = processTwoOperands(expArr, "mul", index-1,index+1)
            indexesToRemove.insert(0,index-1)
            indexesToRemove.insert(0,index)
        if i == "/":
            expArr = processTwoOperands(expArr, "div", index-1,index+1)
            indexesToRemove.insert(0,index-1)
            indexesToRemove.insert(0,index)
    return expArr

## Function processes operation with 4th highest priority.
# @param expArr Array to be processed
# @return Returns array with processed operations
def processPriority4(expArr):
    for index,i in enumerate(expArr):
        if i == "+":
            expArr = processTwoOperands(expArr, "add", index-1,index+1)
            indexesToRemove.insert(0,index-1)
            indexesToRemove.insert(0,index)
        if i == "-":
            expArr = processTwoOperands(expArr, "sub", index-1,index+1)
            indexesToRemove.insert(0,index-1)
            indexesToRemove.insert(0,index)
    return expArr

## Function processes whole expression.
# @param expArr Array to be processed
# @return Returns array with processed operations
def calculate():
    ## Stores last result
    res=""
    try:
        expression = ui.lineInput.text()
        expArr = splitExprToArr(expression)

        #empty input
        if len(expArr) == 0:
            ui.lineInput.setFocus()
            return

        #process operations with highest priority.
        expArr = processPriority1(expArr)
        expArr = removeFromArr(expArr, indexesToRemove)

        #if first character is + or -, insert 0 ahead.
        if expArr[0]  == "-" or expArr[0]  == "+":
            expArr.insert(0,"0")

        #process operations with 2nd highest priority.
        expArr = processPriority2(expArr)
        expArr = removeFromArr(expArr, indexesToRemove)
        
        #process operations with 3nd highest priority.
        expArr = processPriority3(expArr)
        expArr = removeFromArr(expArr, indexesToRemove)

        #process operations with 4rd highest priority.
        expArr = processPriority4(expArr)
        expArr = removeFromArr(expArr, indexesToRemove)

        #more then 1 node in array means something is not processed.
        if len(expArr) != 1:
            raise SyntaxError()
        
        #eval whole expression and round result
        ui.res = eval(expArr[0])
        ui.res = (f'{ui.res:.15f}')
        ui.res = ui.res.rstrip('0')
        ui.res = ui.res.rstrip('.')
        resString = expression + '  =   ' + str(ui.res)

    except TypeError as e: 
        resString=repr(e)

    except ZeroDivisionError as e:
        resString = "Division by zero!"

    except OverflowError as e:
        resString = "Too large number!"

    except Exception as e:
        resString = "Wrong syntax!"

    else:
        ui.lineInput.setText("")
        ui.lineInput.setFocus()

    #add result to history and ensure history text label is scrolled down
    ui.resIndex = 0
    resList.insert(1,ui.res)
    ui.textDisplay.append(resString)
    ui.textDisplay.ensureCursorVisible()

## Function processes operation with 2 operands, inserts result to the greatest index used.
# @param expArr Array to be processed
# @param operation Name of operation to be precessed
# @param operand1 Index of first operand
# @param operand2 Index of second operand
# @return Returns array with processed operation
def processTwoOperands(expArr, operation, operand1, operand2):
    expr = 'calcLib.'+operation+'('+expArr[operand1]+','+expArr[operand2]+')'
    lastIndex = max(operand1, operand2)
    expArr[lastIndex] = expr
    return expArr

## Function processes operation with 1 operand, inserts result to the greatest index used.
# @param expArr Array to be processed
# @param operationIndex Index of operation
# @param operation Name of operation to be precessed
# @param operand Index of operand
# @return Returns array with processed operation
def processOneOperand(expArr, operationIndex, operation, operand):
    expr = 'calcLib.'+operation+'('+expArr[operand]+')'
    lastIndex = max(operand, operationIndex)
    expArr[lastIndex] = expr
    return expArr

## Function processes operation with no operand, inserts result to the greatest index used.
# @param expArr Array to be processed
# @param operationIndex Index of operation
# @param operation Name of operation to be precessed
# @param operand Index of operand
# @return Returns array with processed operation
def processNoOperand(expArr, operationIndex, operation):
    expr = 'calcLib.'+operation+'()'
    expArr[operationIndex] = expr
    return expArr

## Opens file with help.
def showHelp():
    os.startfile("help.pdf")
     
## Function attaches buttons and keys to proper functions.
def attachButtons():
    ui.Num0.clicked.connect(lambda: (addSymbolToInput(0)))
    ui.Num1.clicked.connect(lambda: (addSymbolToInput(1)))
    ui.Num2.clicked.connect(lambda: (addSymbolToInput(2)))
    ui.Num3.clicked.connect(lambda: (addSymbolToInput(3)))
    ui.Num4.clicked.connect(lambda: (addSymbolToInput(4)))
    ui.Num5.clicked.connect(lambda: (addSymbolToInput(5)))
    ui.Num6.clicked.connect(lambda: (addSymbolToInput(6)))
    ui.Num7.clicked.connect(lambda: (addSymbolToInput(7)))
    ui.Num8.clicked.connect(lambda: (addSymbolToInput(8)))
    ui.Num9.clicked.connect(lambda: (addSymbolToInput(9)))
    ui.PlusBtn.clicked.connect(lambda: (addSymbolToInput("+")))
    ui.DivBtn.clicked.connect(lambda: (addSymbolToInput("/")))
    ui.MultiplyBtn.clicked.connect(lambda: (addSymbolToInput("x")))
    ui.MinusBtn.clicked.connect(lambda: (addSymbolToInput("-")))
    ui.CommaBtn.clicked.connect(lambda: (addSymbolToInput(".")))
    ui.FacBtn.clicked.connect(lambda: (addSymbolToInput("!")))
    ui.PowBtn.clicked.connect(lambda: (addSymbolToInput("^")))
    ui.SqrBtn.clicked.connect(lambda: (addSymbolToInput("√")))
    ui.PiBtn.clicked.connect(lambda: (addSymbolToInput("π")))
    ui.LnBtn.clicked.connect(lambda: (addSymbolToInput("ln")))
    ui.delHistoryBtn.clicked.connect(delHistory)
    ui.ClearBtn.clicked.connect(clear)
    ui.BackspaceBtn.clicked.connect(backspace)
    ui.EqualBtn.clicked.connect(calculate)
    ui.AnsBtn.clicked.connect(lambda: ansToInput)
    ui.helpBtn.clicked.connect(showHelp)
    keyboard.add_hotkey('Enter', calculate, args=())
    keyboard.on_press_key("down", historyDown)
    keyboard.on_press_key('up', historyUp)

## Function scrolls up between previous results and prints it to the input.
# @param key Pressed key
def historyUp(key):
    if  str(key) == "KeyboardEvent(8 down)":return
    maxIndex = len(resList)-1
    ui.resIndex=ui.resIndex+1
    if ui.resIndex > maxIndex:
        ui.resIndex = 0

    ui.lineInput.clear()
    ansToInput()

## Function scrolls down between previous results and prints it to the input.
# @param key Pressed key
def historyDown(key):
    if str(key) == "KeyboardEvent(2 down)":return
    maxIndex = len(resList)-1
    ui.resIndex=ui.resIndex-1
    if ui.resIndex < 0:
        ui.resIndex = maxIndex

    ui.lineInput.clear()
    ansToInput()

## Main function.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.instance().thread()
    calculator = QtWidgets.QMainWindow()
    ui = Ui_calculator()
    ui.setupUi(calculator)
    ui.resIndex=0
    attachButtons()
    calculator.show()
    ui.lineInput.setFocus()
    sys.exit(app.exec_())
