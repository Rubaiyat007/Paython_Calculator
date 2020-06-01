import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

global operatorSign
global signs
operatorSign = ("+", "-", "*", "/", "%")



class Calculator(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

        self.setStyleSheet("""
            QPushButton {
                  border: 2px solid black;
                  border-radius: 10px;
                  background-color: rgb(255, 255, 255);
                  }

            QPushButton#buttonZero {
                  border-radius: 15px;
                  }

            QLineEdit{
               border-radius:5px;
            }

            """)

    def initUI(self):
        self.line = QLineEdit(self)
        self.line.move(10, 5)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        font = self.line.font()
        font.setPointSize(22)
        self.line.setFont(font)
        self.line.resize(205, 170)

        zero = QPushButton("0", self)
        zero.setObjectName("buttonZero")
        zero.move(10, 350)
        zero.resize(90, 30)

        one = QPushButton("1", self)
        one.move(10, 310)
        one.resize(45, 30)

        two = QPushButton("2", self)
        two.move(60, 310)
        two.resize(45, 30)

        three = QPushButton("3", self)
        three.move(115, 310)
        three.resize(45, 30)

        four = QPushButton("4", self)
        four.move(10, 270)
        four.resize(45, 30)

        five = QPushButton("5", self)
        five.move(60, 270)
        five.resize(45, 30)

        six = QPushButton("6", self)
        six.move(115, 270)
        six.resize(45, 30)

        seven = QPushButton("7", self)
        seven.move(10, 230)
        seven.resize(45, 30)

        eight = QPushButton("8", self)
        eight.move(60, 230)
        eight.resize(45, 30)

        nine = QPushButton("9", self)
        nine.move(115, 230)
        nine.resize(45, 30)

        back = QPushButton("C", self)
        back.move(60, 190)
        back.resize(45, 30)
        back.clicked.connect(self.Back)

        point = QPushButton(".", self)
        point.move(115, 350)
        point.resize(45, 30)
        point.clicked.connect(self.Point)

        plus = QPushButton("+", self)
        plus.move(170, 310)
        plus.resize(45, 30)

        minus = QPushButton("-", self)
        minus.move(170, 270)
        minus.resize(45, 30)

        multiply = QPushButton("*", self)
        multiply.move(170, 230)
        multiply.resize(45, 30)

        divide = QPushButton("/", self)
        divide.move(170, 190)
        divide.resize(45, 30)

        percent = QPushButton("%", self)
        percent.move(115, 190)
        percent.resize(45, 30)

        equals = QPushButton("=", self)
        equals.move(170, 350)
        equals.resize(45, 30)
        equals.clicked.connect(self.Equal)

        ac = QPushButton("AC", self)
        ac.move(10, 190)
        ac.resize(45, 30)
        ac.clicked.connect(self.AC)

        # Window Settings
        signs = [zero, one, two, three, four, five, six,
                 seven, eight, nine, plus, minus, multiply, divide, percent]

        for i in signs:
            i.clicked.connect(self.Num)

        self.setGeometry(300, 300, 273, 320)
        self.setWindowTitle("Calculator")
        self.setFixedSize(225, 400)
        self.show()

    def Num(self):
        sender = self.sender().text()

        if not any(sign in sender for sign in operatorSign):
            newNum = int(sender)
            setNum = str(newNum)
            self.line.setText(self.line.text() + setNum)
        else:
            self.line.setText(self.line.text() + sender)

    def Equal(self):
        textExpression = self.line.text().lstrip('0')
        if textExpression != "" and not textExpression.endswith(operatorSign):
            result = str(eval(textExpression))
            self.line.setText(result)

    def Point(self):
        textExpression = self.line.text()
        if "." not in textExpression or textExpression.endswith(operatorSign):
         self.line.setText(textExpression + ".")

    def Back(self):
        self.line.backspace()

    def AC(self):
        self.line.clear()


def main():
    app = QApplication(sys.argv)
    main = Calculator()
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
