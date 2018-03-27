class State:
    def __init__(self):
        self.eleList = []
        self.pointerIndex = -1
        self.lastAnswer = ''

    def inputNumber(self, numberStr):
        self.eleList.insert(self.pointerIndex + 1, numberStr)
        self.pointerIndex += 1

    def inputDot(self):
        if self.pointerIndex == -1:
            self.eleList.insert(0, '0')
            self.pointerIndex += 1
        self.eleList.insert(self.pointerIndex + 1, '.')
        self.pointerIndex += 1

    def inputOperator(self, operatorStr):
        self.eleList.insert(self.pointerIndex + 1, operatorStr)
        self.pointerIndex += 1

    def inputFunction(self, funcStr):
        self.eleList.insert(self.pointerIndex + 1, funcStr)
        self.eleList.insert(self.pointerIndex + 2, '(')
        self.eleList.insert(self.pointerIndex + 3, ')')
        self.pointerIndex += 2

    def inputBrackets(self):
        self.eleList.insert(self.pointerIndex + 1, '(')
        self.eleList.insert(self.pointerIndex + 2, ')')
        self.pointerIndex += 1

    def inputLastAnswer(self):
        if self.lastAnswer != '':
            self.eleList.insert(self.pointerIndex + 2, 'ans')
            self.pointerIndex += 1

    def backspace(self):
        if self.pointerIndex == -1:
            return

        currEleLastChar =  self.eleList[self.pointerIndex][-1]
        if currEleLastChar == '(' and len(self.eleList) >= self.pointerIndex + 2 and self.eleList[self.pointerIndex + 1] == ')':
            # when point is just in the middle of '(' and ')', delete both
            self.eleList = self.eleList[:self.pointerIndex + 1] + self.eleList[self.pointerIndex + 2:]
        self.eleList = self.eleList[:self.pointerIndex] + self.eleList[self.pointerIndex + 1:]
        self.pointerIndex -= 1

    def allClear(self):
        self.eleList = []
        self.pointerIndex = -1

    def movePointer(self, direction):
        if direction == 'forward':
            if not self.pointerIndex >= len(self.eleList) - 1:
                self.pointerIndex += 1
                return
        if direction == 'backward':
            if not self.pointerIndex <= -1:
                self.pointerIndex -= 1
                return

    def resetWithAns(self, answer):
        self.eleList = []
        self.pointerIndex = -1
        self.lastAnswer = answer

