class State:

    def __init__(self):
        self.eleList = []
        self.pointerIndex = -1
        self.lastAnswer = ''

    def inputNumber(self, numberStr):
        self.eleList.insert(self.pointerIndex + 1, numberStr)
        self.pointerIndex += 1

    def inputDot(self):
        if (self.pointerIndex == -1 or \
                self.eleList[self.pointerIndex] < '0' or \
                self.eleList[self.pointerIndex] > '9'):
            self.inputNumber('0')
        self.eleList.insert(self.pointerIndex + 1, '.')
        self.pointerIndex += 1

    def inputOperator(self, operatorStr):
        self.eleList.insert(self.pointerIndex + 1, operatorStr)
        self.pointerIndex += 1

    def inputFunction(self, funcStr):
        if (self.pointerIndex != -1 and \
                self.eleList[self.pointerIndex] >= '0' and \
                self.eleList[self.pointerIndex] <= '9'):
            self.inputOperator('*')
        self.eleList.insert(self.pointerIndex + 1, funcStr)
        self.eleList.insert(self.pointerIndex + 2, '(')
        self.eleList.insert(self.pointerIndex + 3, ')')
        self.pointerIndex += 2

    def inputBrackets(self):
        if (self.pointerIndex != -1 and \
                self.eleList[self.pointerIndex] >= '0' and \
                self.eleList[self.pointerIndex] <= '9'):
            self.inputOperator('*')
        self.eleList.insert(self.pointerIndex + 1, '(')
        self.eleList.insert(self.pointerIndex + 2, ')')
        self.pointerIndex += 1

    def inputLastAnswer(self):
        if self.lastAnswer != '':
            self.eleList.insert(self.pointerIndex + 1, 'ans')
            self.pointerIndex += 1

    def backspace(self):
        if self.pointerIndex == -1:
            return

        if (self.eleList[self.pointerIndex] == '('):
            endIndex = self.eleList[self.pointerIndex:].index(')') + 1
            del self.eleList[self.pointerIndex:endIndex+1]
            self.pointerIndex -= 1
        elif (self.eleList[self.pointerIndex] == ')'):
            startIndex = self.pointerIndex - \
                    self.eleList[self.pointerIndex::-1].index('(')
            del self.eleList[startIndex:self.pointerIndex+1]
            self.pointerIndex = startIndex - 1
        else:
            del self.eleList[self.pointerIndex]
            self.pointerIndex -= 1

    def allClear(self):
        self.eleList = []
        self.pointerIndex = -1

    def movePointer(self, direction):
        if direction == '+':
            if not self.pointerIndex >= len(self.eleList) - 1:
                self.pointerIndex += 1
                return
        if direction == '-':
            if not self.pointerIndex <= -1:
                self.pointerIndex -= 1
                return

    def resetWithAns(self, answer):
        self.eleList = []
        self.pointerIndex = -1
        self.lastAnswer = answer

