# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.6

from PyQt5  import QtCore, QtGui, QtWidgets
from state  import *
from syntax import *
from math   import *

class Ui_MainWindow(object):

    def displayExpression(self):
        expressionObject = self.CalcState.eleList
        cursorPosition = self.CalcState.pointerIndex + 1
        blackText = ''.join(expressionObject[:cursorPosition])
        whiteText = ''.join(expressionObject[cursorPosition:])
        editor = self.CalcEdt
        editor.clear()
        editor.insertHtml(''.join([
                blackText,
                '<span style=\'color: #ccc;\'>',
                whiteText,
                '</span>'
            ]))

    def displayError(self, calcList, errLoc):
        blackText1 = ''.join(calcList[:errLoc])
        blackText2 = ''.join(calcList[errLoc+1:])
        editor = self.CalcEdt
        editor.clear()
        editor.insertHtml(''.join([
                blackText1,
                '<span style=\'color: #f00;\'>',
                calcList[errLoc],
                '</span>',
                blackText2
            ]))

    def appendHistory(self, expressionObject, result):
        blackText = ''.join(expressionObject)
        blueText = str(result)
        editor = self.CalcHist
        if (not(self.historyUpdated)):
            self.historyUpdated = True
            editor.clear()
        editor.append('')
        editor.insertHtml(''.join([
                '<p align=\'right\'>',
                blackText,
                '</p>'
            ]))
        editor.append('')
        editor.insertHtml(''.join([
                '<p align=\'right\'><span style=\'color: #00f;\'>',
                blueText,
                '</span></p>'
            ]))

    def evalExpression(self):
        self.CalcState.pointerIndex = len(self.CalcState.eleList) - 1
        calcList = []
        i = 0
        while (i < len(self.CalcState.eleList)):
            if (self.CalcState.eleList[i] >= '0' and \
                    self.CalcState.eleList[i] <= '9'):
                j = i
                while (j < len(self.CalcState.eleList) and \
                        ((self.CalcState.eleList[j] >= '0' and \
                        self.CalcState.eleList[j] <= '9') or self.CalcState.eleList[j] == '.')):
                    j += 1
                calcList.append(''.join(self.CalcState.eleList[i:j]))
                i = j
            else:
                calcList.append(self.CalcState.eleList[i])
                i += 1
        calcList_ = calcList[:]
        if len(calcList) == 0:
            return
        errLoc = SyntaxCheck(calcList)
        if (errLoc != -1):
            self.displayError(calcList, errLoc)
        else:
            for i in range(len(calcList_)):
                if (calcList_[i] == 'ans'):
                    calcList[i] = self.CalcState.lastAnswer
                elif (calcList_[i] == '^'):
                    calcList[i] = '**'
                else:
                    calcList[i] = calcList_[i]
            result = eval(''.join(calcList))
            self.CalcState.lastAnswer = str(result)
            self.appendHistory(self.CalcState.eleList, result)
            self.DoClr()

    def Push0(self):
        self.CalcState.inputNumber('0')
        self.displayExpression()
    def Push1(self):
        self.CalcState.inputNumber('1')
        self.displayExpression()
    def Push2(self):
        self.CalcState.inputNumber('2')
        self.displayExpression()
    def Push3(self):
        self.CalcState.inputNumber('3')
        self.displayExpression()
    def Push4(self):
        self.CalcState.inputNumber('4')
        self.displayExpression()
    def Push5(self):
        self.CalcState.inputNumber('5')
        self.displayExpression()
    def Push6(self):
        self.CalcState.inputNumber('6')
        self.displayExpression()
    def Push7(self):
        self.CalcState.inputNumber('7')
        self.displayExpression()
    def Push8(self):
        self.CalcState.inputNumber('8')
        self.displayExpression()
    def Push9(self):
        self.CalcState.inputNumber('9')
        self.displayExpression()
    def PushDot(self):
        self.CalcState.inputDot()
        self.displayExpression()
    def PushPlus(self):
        self.CalcState.inputOperator('+')
        self.displayExpression()
    def PushMinus(self):
        self.CalcState.inputOperator('-')
        self.displayExpression()
    def PushTimes(self):
        self.CalcState.inputOperator('*')
        self.displayExpression()
    def PushDiv(self):
        self.CalcState.inputOperator('/')
        self.displayExpression()
    def PushPow(self):
        self.CalcState.inputOperator('^')
        self.displayExpression()
    def PushSin(self):
        self.CalcState.inputFunction('sin')
        self.displayExpression()
    def PushCos(self):
        self.CalcState.inputFunction('cos')
        self.displayExpression()
    def PushBrac(self):
        self.CalcState.inputBrackets()
        self.displayExpression()
    def PushAns(self):
        self.CalcState.inputLastAnswer()
        self.displayExpression()
    def DoClr(self):
        self.CalcState.allClear()
        self.displayExpression()
    def DoDel(self):
        self.CalcState.backspace()
        self.displayExpression()
    def DoLft(self):
        self.CalcState.movePointer('-')
        self.displayExpression()
    def DoRgt(self):
        self.CalcState.movePointer('+')
        self.displayExpression()
    def DoExit(self):
        QtCore.QCoreApplication.exit()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(291, 444)
        self.CentralWidget = QtWidgets.QWidget(MainWindow)
        self.CentralWidget.setObjectName("CentralWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.CentralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 190, 271, 191))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.NumPad = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.NumPad.setContentsMargins(0, 0, 0, 0)
        self.NumPad.setObjectName("NumPad")
        self.Btn0 = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Btn0.setFont(font)
        self.Btn0.setObjectName("Btn0")
        self.NumPad.addWidget(self.Btn0, 4, 3, 1, 1)
        self.Btn9 = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Btn9.setFont(font)
        self.Btn9.setObjectName("Btn9")
        self.NumPad.addWidget(self.Btn9, 1, 4, 1, 1)
        self.BtnDot = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnDot.setFont(font)
        self.BtnDot.setObjectName("BtnDot")
        self.NumPad.addWidget(self.BtnDot, 4, 2, 1, 1)
        self.Btn8 = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Btn8.setFont(font)
        self.Btn8.setObjectName("Btn8")
        self.NumPad.addWidget(self.Btn8, 1, 3, 1, 1)
        self.Btn3 = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Btn3.setFont(font)
        self.Btn3.setObjectName("Btn3")
        self.NumPad.addWidget(self.Btn3, 3, 4, 1, 1)
        self.Btn1 = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Btn1.setFont(font)
        self.Btn1.setObjectName("Btn1")
        self.NumPad.addWidget(self.Btn1, 3, 2, 1, 1)
        self.Btn2 = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Btn2.setFont(font)
        self.Btn2.setObjectName("Btn2")
        self.NumPad.addWidget(self.Btn2, 3, 3, 1, 1)
        self.Btn5 = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Btn5.setFont(font)
        self.Btn5.setObjectName("Btn5")
        self.NumPad.addWidget(self.Btn5, 2, 3, 1, 1)
        self.BtnCalc = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnCalc.setFont(font)
        self.BtnCalc.setObjectName("BtnCalc")
        self.NumPad.addWidget(self.BtnCalc, 4, 4, 1, 1)
        self.Btn6 = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Btn6.setFont(font)
        self.Btn6.setObjectName("Btn6")
        self.NumPad.addWidget(self.Btn6, 2, 4, 1, 1)
        self.Btn7 = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Btn7.setFont(font)
        self.Btn7.setObjectName("Btn7")
        self.NumPad.addWidget(self.Btn7, 1, 2, 1, 1)
        self.Btn4 = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Btn4.setFont(font)
        self.Btn4.setObjectName("Btn4")
        self.NumPad.addWidget(self.Btn4, 2, 2, 1, 1)
        self.BtnTimes = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnTimes.setFont(font)
        self.BtnTimes.setObjectName("BtnTimes")
        self.NumPad.addWidget(self.BtnTimes, 3, 1, 1, 1)
        self.BtnPlus = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnPlus.setFont(font)
        self.BtnPlus.setObjectName("BtnPlus")
        self.NumPad.addWidget(self.BtnPlus, 1, 1, 1, 1)
        self.BtnCl = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnCl.setFont(font)
        self.BtnCl.setObjectName("BtnCl")
        self.NumPad.addWidget(self.BtnCl, 0, 1, 1, 1)
        self.BtnLeft = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnLeft.setFont(font)
        self.BtnLeft.setObjectName("BtnLeft")
        self.NumPad.addWidget(self.BtnLeft, 0, 3, 1, 1)
        self.BtnRight = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnRight.setFont(font)
        self.BtnRight.setObjectName("BtnRight")
        self.NumPad.addWidget(self.BtnRight, 0, 4, 1, 1)
        self.BtnMinus = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnMinus.setFont(font)
        self.BtnMinus.setObjectName("BtnMinus")
        self.NumPad.addWidget(self.BtnMinus, 2, 1, 1, 1)
        self.BtnDel = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnDel.setFont(font)
        self.BtnDel.setObjectName("BtnDel")
        self.NumPad.addWidget(self.BtnDel, 0, 2, 1, 1)
        self.BtnDiv = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnDiv.setFont(font)
        self.BtnDiv.setObjectName("BtnDiv")
        self.NumPad.addWidget(self.BtnDiv, 4, 1, 1, 1)
        self.BtnBra = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnBra.setFont(font)
        self.BtnBra.setObjectName("BtnBra")
        self.NumPad.addWidget(self.BtnBra, 0, 0, 1, 1)
        self.BtnExp = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnExp.setFont(font)
        self.BtnExp.setObjectName("BtnExp")
        self.NumPad.addWidget(self.BtnExp, 1, 0, 1, 1)
        self.BtnSin = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnSin.setFont(font)
        self.BtnSin.setObjectName("BtnSin")
        self.NumPad.addWidget(self.BtnSin, 2, 0, 1, 1)
        self.BtnCos = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnCos.setFont(font)
        self.BtnCos.setObjectName("BtnCos")
        self.NumPad.addWidget(self.BtnCos, 3, 0, 1, 1)
        self.BtnAns = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnAns.setFont(font)
        self.BtnAns.setObjectName("BtnAns")
        self.NumPad.addWidget(self.BtnAns, 4, 0, 1, 1)
        self.CalcHist = QtWidgets.QTextBrowser(self.CentralWidget)
        self.CalcHist.setGeometry(QtCore.QRect(0, 0, 291, 141))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.CalcHist.setFont(font)
        self.CalcHist.setObjectName("CalcHist")
        self.CalcEdt = QtWidgets.QTextBrowser(self.CentralWidget)
        self.CalcEdt.setGeometry(QtCore.QRect(0, 140, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.CalcEdt.setFont(font)
        self.CalcEdt.setObjectName("CalcEdt")
        self.CalcEdt.setCursorWidth(2)
        self.CalcEdt.ensureCursorVisible()
        MainWindow.setCentralWidget(self.CentralWidget)
        self.MenuBar = QtWidgets.QMenuBar(MainWindow)
        self.MenuBar.setGeometry(QtCore.QRect(0, 0, 291, 17))
        self.MenuBar.setObjectName("MenuBar")
        self.MenuEasyCalc = QtWidgets.QMenu(self.MenuBar)
        self.MenuEasyCalc.setObjectName("MenuEasyCalc")
        MainWindow.setMenuBar(self.MenuBar)
        self.StatusBar = QtWidgets.QStatusBar(MainWindow)
        self.StatusBar.setObjectName("StatusBar")
        MainWindow.setStatusBar(self.StatusBar)
        self.actionOpen_History = QtWidgets.QAction(MainWindow)
        self.actionOpen_History.setObjectName("actionOpen_History")
        self.actionOpen_History.setEnabled(False)
        self.actionSave_History = QtWidgets.QAction(MainWindow)
        self.actionSave_History.setObjectName("actionSave_History")
        self.actionSave_History.setEnabled(False)
        self.actionClear_History = QtWidgets.QAction(MainWindow)
        self.actionClear_History.setObjectName("actionClear_History")
        self.actionClear_History.setEnabled(False)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.DoExit)
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionToggle_Dark_Theme = QtWidgets.QAction(MainWindow)
        self.actionToggle_Dark_Theme.setObjectName("actionToggle_Dark_Theme")
        self.actionToggle_Dark_Theme.setEnabled(False)
        self.MenuEasyCalc.addSeparator()
        self.MenuEasyCalc.addAction(self.actionClear_History)
        self.MenuEasyCalc.addAction(self.actionOpen_History)
        self.MenuEasyCalc.addAction(self.actionSave_History)
        self.MenuEasyCalc.addSeparator()
        self.MenuEasyCalc.addAction(self.actionToggle_Dark_Theme)
        self.MenuEasyCalc.addSeparator()
        self.MenuEasyCalc.addAction(self.actionExit)
        self.MenuBar.addAction(self.MenuEasyCalc.menuAction())

        self.CalcState = State()
        self.historyUpdated = False
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # set up bindings
        self.Btn0.clicked.connect(self.Push0)
        self.Btn1.clicked.connect(self.Push1)
        self.Btn2.clicked.connect(self.Push2)
        self.Btn3.clicked.connect(self.Push3)
        self.Btn4.clicked.connect(self.Push4)
        self.Btn5.clicked.connect(self.Push5)
        self.Btn6.clicked.connect(self.Push6)
        self.Btn7.clicked.connect(self.Push7)
        self.Btn8.clicked.connect(self.Push8)
        self.Btn9.clicked.connect(self.Push9)
        self.BtnPlus.clicked.connect(self.PushPlus)
        self.BtnMinus.clicked.connect(self.PushMinus)
        self.BtnTimes.clicked.connect(self.PushTimes)
        self.BtnDiv.clicked.connect(self.PushDiv)
        self.BtnDot.clicked.connect(self.PushDot)
        self.BtnExp.clicked.connect(self.PushPow)
        self.BtnSin.clicked.connect(self.PushSin)
        self.BtnCos.clicked.connect(self.PushCos)
        self.BtnAns.clicked.connect(self.PushAns)
        self.BtnBra.clicked.connect(self.PushBrac)
        self.BtnCl.clicked.connect(self.DoClr)
        self.BtnDel.clicked.connect(self.DoDel)
        self.BtnLeft.clicked.connect(self.DoLft)
        self.BtnRight.clicked.connect(self.DoRgt)
        self.BtnCalc.clicked.connect(self.evalExpression)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EasyCalc"))
        self.Btn0.setText(_translate("MainWindow", "0"))
        self.Btn9.setText(_translate("MainWindow", "9"))
        self.BtnDot.setText(_translate("MainWindow", "."))
        self.Btn8.setText(_translate("MainWindow", "8"))
        self.Btn3.setText(_translate("MainWindow", "3"))
        self.Btn1.setText(_translate("MainWindow", "1"))
        self.Btn2.setText(_translate("MainWindow", "2"))
        self.Btn5.setText(_translate("MainWindow", "5"))
        self.BtnCalc.setText(_translate("MainWindow", "="))
        self.Btn6.setText(_translate("MainWindow", "6"))
        self.Btn7.setText(_translate("MainWindow", "7"))
        self.Btn4.setText(_translate("MainWindow", "4"))
        self.BtnTimes.setText(_translate("MainWindow", "*"))
        self.BtnPlus.setText(_translate("MainWindow", "+"))
        self.BtnCl.setText(_translate("MainWindow", "C"))
        self.BtnLeft.setText(_translate("MainWindow", "<"))
        self.BtnRight.setText(_translate("MainWindow", ">"))
        self.BtnMinus.setText(_translate("MainWindow", "-"))
        self.BtnDel.setText(_translate("MainWindow", "X"))
        self.BtnDiv.setText(_translate("MainWindow", "/"))
        self.BtnBra.setText(_translate("MainWindow", "(.)"))
        self.BtnExp.setText(_translate("MainWindow", "x^n"))
        self.BtnSin.setText(_translate("MainWindow", "SIN"))
        self.BtnCos.setText(_translate("MainWindow", "COS"))
        self.BtnAns.setText(_translate("MainWindow", "ANS"))
        self.CalcHist.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Your History Here</p></body></html>"))
        self.CalcEdt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Expression Here</p></body></html>"))
        self.MenuEasyCalc.setTitle(_translate("MainWindow", "EasyCalc"))
        self.actionOpen_History.setText(_translate("MainWindow", "Open History..."))
        self.actionSave_History.setText(_translate("MainWindow", "Save History..."))
        self.actionClear_History.setText(_translate("MainWindow", "Clear History"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionToggle_Dark_Theme.setText(_translate("MainWindow", "Toggle Dark Theme"))

