from PyQt5 import QtWidgets
import re
import calcLib

class Ui_calculator(object):
    from ui import setupUi, retranslateUi
    
    #add symbol from pushed button to inputs cursor position
    def addSymbolToInput(self, num):
        curText = self.lineInput.text()
        cursorPos = self.lineInput.cursorPosition()

        curText = curText[0:cursorPos] + str(num) + curText[cursorPos:]
        self.lineInput.setText(curText)
        self.lineInput.setFocus()
        self.lineInput.setCursorPosition(cursorPos + len(str(num)))

    #clear whole input line
    def clear(self):
        self.lineInput.setText("")
        self.lineInput.setFocus()

    #delete one character before cursor positioin
    def backspace(self):
        curText = self.lineInput.text()
        cursorIndex = self.lineInput.cursorPosition()-1
        if cursorIndex == -1:
            self.lineInput.setFocus()
            return

        self.lineInput.setText(curText[0 : cursorIndex : ] + curText[cursorIndex + 1 : :])
        self.lineInput.setFocus()
        self.lineInput.setCursorPosition(cursorIndex)

    #adds previous result to input line
    def ansToInput(self):
        curText = self.lineInput.text()
        self.lineInput.setText(curText + str(self.res))
        self.lineInput.setFocus()

    #deletes whole history label
    def delHistory(self):
        self.textDisplay.clear()
        self.lineInput.setFocus()

    #splits expression by operators and special characters
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

                if i == "π" and not len(expArr)-index-1 == 0 and not re.match(r'(\+|-|x|\*|/|!|\^)',expArr[index+1]):
                    expArr.insert(index+1,"x")

                if i == "π" and index > 0 and not re.fullmatch(r'(\+|-|x|\*|/|!|\^|√|π|ln)',expArr[index-1]):
                        expArr.insert(index,"x")
            return expArr

    def removeFromArr(self,arr, indexes):
        for index in indexes:
            arr.pop(int(index))
        indexes.clear()
        return arr

    def processLvl1(self, expArr):
        for index,i in enumerate(expArr):  
            if i == "!":
                expArr = self.processOneOperand(expArr, index, "fac", index-1)
                self.indexesToRemove.insert(0,index-1) 

            if i == "π":
                expArr = self.processNoOperand(expArr, index, "pi")
        return expArr

    def processLvl2(self, expArr):
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

    def processLvl3(self, expArr):
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

    def processLvl4(self, expArr):
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

    def calculate(self,key):
        try:
            expression = self.lineInput.text()
            expArr = self.splitExprToArr(expression)
            self.indexesToRemove = []

            #empty input
            if len(expArr) == 0:
                self.lineInput.setFocus()
                return

            #process operations with highest priority
            expArr = self.processLvl1(expArr)
            expArr = self.removeFromArr(expArr, self.indexesToRemove)

            #process operations with 2nd highest priority
            expArr = self.processLvl2(expArr)
            expArr = self.removeFromArr(expArr, self.indexesToRemove)
            
            #process operations with 3nd highest priority
            expArr = self.processLvl3(expArr)
            expArr = self.removeFromArr(expArr, self.indexesToRemove)

            #process operations with 4rd highest priority
            expArr = self.processLvl4(expArr)
            expArr = self.removeFromArr(expArr, self.indexesToRemove)
            
            #more then 1 node in array means something is not processed
            if len(expArr) != 1:
                raise SyntaxError()
            
            print(expArr)
            self.res = eval(expArr[0])
            self.res = (f'{self.res:.15f}')
            self.res = self.res.rstrip('0')
            self.res = self.res.rstrip('.')
            self.resString = expression + '        =       ' + str(self.res)

        except TypeError as e: 
            self.resString=repr(e)

        except ZeroDivisionError as e:
            self.resString = "Division by zero!"

        except Exception as e:
            self.resString = "Wrong syntax!"

        self.textDisplay.append(self.resString)
        self.textDisplay.ensureCursorVisible()

        self.lineInput.setText(str(self.res))
        self.lineInput.setFocus()

    def processTwoOperands(self, expArr, operation, operand1, operand2):
        expr = 'calcLib.'+operation+'('+expArr[operand1]+','+expArr[operand2]+')'
        lastIndex = max(operand1, operand2)
        expArr[lastIndex] = expr
        return expArr

    def processOneOperand(self, expArr, operationIndex, operation, operand):
        expr = 'calcLib.'+operation+'('+expArr[operand]+')'
        lastIndex = max(operand, operationIndex)
        expArr[lastIndex] = expr
        return expArr

    def processNoOperand(self, expArr, operationIndex, operation):
        expr = 'calcLib.'+operation+'()'
        expArr[operationIndex] = expr
        return expArr

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calculator = QtWidgets.QMainWindow()
    ui = Ui_calculator()
    ui.setupUi(calculator)
    calculator.show()
    sys.exit(app.exec_())