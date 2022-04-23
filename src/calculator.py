
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
# @author Jakub Mašek

from PyQt5 import QtWidgets
import re
import calcLib

## Main class of calculator
class Ui_calculator(object):
    #import ui classes
    from ui import setupUi, retranslateUi
    
    ## Function that adds symbol to input line.
    # @param symbol Symbol to be added
    def addSymbolToInput(self, symbol):
        curText = self.lineInput.text()
        cursorPos = self.lineInput.cursorPosition()

        curText = curText[0:cursorPos] + str(symbol) + curText[cursorPos:]
        self.lineInput.setText(curText)
        self.lineInput.setFocus()
        self.lineInput.setCursorPosition(cursorPos + len(str(symbol)))

    ## Function that clears input line.
    def clear(self):
        self.lineInput.setText("")
        self.lineInput.setFocus()

    ## Function deletes character ahead of cursor position
    def backspace(self):
        curText = self.lineInput.text()
        cursorIndex = self.lineInput.cursorPosition()-1
        if cursorIndex == -1:
            self.lineInput.setFocus()
            return

        self.lineInput.setText(curText[0 : cursorIndex : ] + curText[cursorIndex + 1 : :])
        self.lineInput.setFocus()
        self.lineInput.setCursorPosition(cursorIndex)

    ## Function that adds previous result to input line.
    def ansToInput(self):
        curText = self.lineInput.text()
        self.lineInput.setText(curText + str(self.res))
        self.lineInput.setFocus()

    ## Function that clears history.
    def delHistory(self):
        self.textDisplay.clear()
        self.lineInput.setFocus()

    ## Function splits expression by operators and special characters, validates expression and makes necessary changes in it. 
    # @param expression Math expression to be splitted
    # @return Returns splitted expression as array
    def splitExprToArr(self, expression):
            expArr = re.split(r'(\+|-|x|\*|/|!|\^|√|π|ln)', expression)
            
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
                if i == "π" and not len(expArr)-index-1 == 0 and not re.match(r'(\+|-|x|\*|/|!|\^)',expArr[index+1]):
                    expArr.insert(index+1,"x")

                #if number is next to pi(on left side), adds mul between it
                if i == "π" and index > 0 and not re.fullmatch(r'(\+|-|x|\*|/|!|\^|√|π|ln)',expArr[index-1]):
                        expArr.insert(index,"x")
            return expArr

    ## Function removes values on specific indexes from array
    # @param arr Array
    # @param indexes Indexes of array to be removed
    # @return Returns array with removed indexes
    def removeFromArr(self,arr, indexes):
        for index in indexes:
            arr.pop(int(index))
        indexes.clear()
        return arr

    ## Function processes operation with highest priority
    # @param expArr Array to be processed
    # @return Returns array with processed operations
    def processPriority1(self, expArr):
        for index,i in enumerate(expArr):  
            if i == "!":
                expArr = self.processOneOperand(expArr, index, "fac", index-1)
                self.indexesToRemove.insert(0,index-1) 

            if i == "π":
                expArr = self.processNoOperand(expArr, index, "pi")
        return expArr

    ## Function processes operation with 2nd highest priority
    # @param expArr Array to be processed
    # @return Returns array with processed operations
    def processPriority2(self, expArr):
        for index,i in enumerate(expArr):   
            if i == "ln":
                expArr = self.processOneOperand(expArr, index, "ln", index+1)
                self.indexesToRemove.insert(0,index)

            if i == "^":  
                if re.fullmatch(r'(\+|-|x|\*|/|!|\^|√|π|ln)',expArr[index+1]):
                    break  
                expArr = self.processTwoOperands(expArr, "pwr", index-1,index+1)
                self.indexesToRemove.insert(0,index-1)
                self.indexesToRemove.insert(0,index)

            if i == "√":
                if re.fullmatch(r'(\+|-|x|\*|/|!|\^|√|π|ln)',expArr[index+1]):
                    break
                expArr = self.processTwoOperands(expArr, "root", index+1,index-1)
                self.indexesToRemove.insert(0,index-1)
                self.indexesToRemove.insert(0,index)
        return expArr

    ## Function processes operation with 3rd highest priority
    # @param expArr Array to be processed
    # @return Returns array with processed operations
    def processPriority3(self, expArr):
        for index,i in enumerate(expArr):
            if i == "x" or i == "*":
                expArr = self.processTwoOperands(expArr, "mul", index-1,index+1)
                self.indexesToRemove.insert(0,index-1)
                self.indexesToRemove.insert(0,index)
            if i == "/":
                expArr = self.processTwoOperands(expArr, "div", index-1,index+1)
                self.indexesToRemove.insert(0,index-1)
                self.indexesToRemove.insert(0,index)
        return expArr

    ## Function processes operation with 4th highest priority
    # @param expArr Array to be processed
    # @return Returns array with processed operations
    def processPriority4(self, expArr):
        for index,i in enumerate(expArr):
            if i == "+":
                expArr = self.processTwoOperands(expArr, "add", index-1,index+1)
                self.indexesToRemove.insert(0,index-1)
                self.indexesToRemove.insert(0,index)
            if i == "-":
                expArr = self.processTwoOperands(expArr, "sub", index-1,index+1)
                self.indexesToRemove.insert(0,index-1)
                self.indexesToRemove.insert(0,index)
        return expArr

    ## Function processes whole expression
    # @param expArr Array to be processed
    # @return Returns array with processed operations
    def calculate(self,key):
        ## Stores last result
        self.res=""
        ## Stores indexes of array to be deleted
        self.indexesToRemove=[]
        try:
            expression = self.lineInput.text()
            expArr = self.splitExprToArr(expression)
            self.indexesToRemove = []

            #empty input
            if len(expArr) == 0:
                self.lineInput.setFocus()
                return

            #process operations with highest priority
            expArr = self.processPriority1(expArr)
            expArr = self.removeFromArr(expArr, self.indexesToRemove)

            #if first character is + or -, insert 0 ahead
            if expArr[0]  == "-" or expArr[0]  == "+":
                expArr.insert(0,"0")

            #process operations with 2nd highest priority
            expArr = self.processPriority2(expArr)
            expArr = self.removeFromArr(expArr, self.indexesToRemove)
            
            #process operations with 3nd highest priority
            expArr = self.processPriority3(expArr)
            expArr = self.removeFromArr(expArr, self.indexesToRemove)

            #process operations with 4rd highest priority
            expArr = self.processPriority4(expArr)
            expArr = self.removeFromArr(expArr, self.indexesToRemove)
            
            #more then 1 node in array means something is not processed
            if len(expArr) != 1:
                raise SyntaxError()
            
            print(expArr)#debug REMOVE
            #eval whole expression and round result
            self.res = eval(expArr[0])
            self.res = (f'{self.res:.15f}')
            self.res = self.res.rstrip('0')
            self.res = self.res.rstrip('.')
            resString = expression + '        =       ' + str(self.res)

        except TypeError as e: 
            resString=repr(e)

        except ZeroDivisionError as e:
            resString = "Division by zero!"

        except Exception as e:
            resString = "Wrong syntax!"

        else:
            self.lineInput.setText(str(self.res))
            self.lineInput.setFocus()

        #add result to history and ensure history text label is scrolled down
        self.textDisplay.append(resString)
        self.textDisplay.ensureCursorVisible()

    ## Function processes operation with 2 operands, inserts result to the greatest index used
    # @param expArr Array to be processed
    # @param operation Name of operation to be precessed
    # @param operand1 Index of first operand
    # @param operand2 Index of second operand
    # @return Returns array with processed operation
    def processTwoOperands(self, expArr, operation, operand1, operand2):
        expr = 'calcLib.'+operation+'('+expArr[operand1]+','+expArr[operand2]+')'
        lastIndex = max(operand1, operand2)
        expArr[lastIndex] = expr
        return expArr

    ## Function processes operation with 1 operand, inserts result to the greatest index used
    # @param expArr Array to be processed
    # @param operationIndex Index of operation
    # @param operation Name of operation to be precessed
    # @param operand Index of operand
    # @return Returns array with processed operation
    def processOneOperand(self, expArr, operationIndex, operation, operand):
        expr = 'calcLib.'+operation+'('+expArr[operand]+')'
        lastIndex = max(operand, operationIndex)
        expArr[lastIndex] = expr
        return expArr

    ## Function processes operation with no operand, inserts result to the greatest index used
    # @param expArr Array to be processed
    # @param operationIndex Index of operation
    # @param operation Name of operation to be precessed
    # @param operand Index of operand
    # @return Returns array with processed operation
    def processNoOperand(self, expArr, operationIndex, operation):
        expr = 'calcLib.'+operation+'()'
        expArr[operationIndex] = expr
        return expArr

## Main function
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calculator = QtWidgets.QMainWindow()
    ui = Ui_calculator()
    ui.setupUi(calculator)
    calculator.show()
    sys.exit(app.exec_())