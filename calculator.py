import sys
from typing import cast

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout, QPushButton, QVBoxLayout


class Display(QLineEdit):
    def __init__(self):
        super().__init__()


class ResultDisplay(Display):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(self.default_style())
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

    @staticmethod
    def default_style():
        return ("font-size: 100px;"
                "font-weight: italic;"
                "font-style: italic;"
                "border: 3px inset darkslategray;"
                "color: darkslategray;"
                "background-color: honeydew;"
                "border-radius: 10px;"
                "padding: 10px;"
                "margin: 0;")

    def error_message(self):
        self.setStyleSheet("font-size: 100px;"
                           "font-weight: italic;"
                           "font-style: italic;"
                           "color: DarkRed;"
                           "background-color: tomato;"
                           "padding: 10px;"
                           "margin: 0;"
                           "border-radius: 10px")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setText("Error")

    def reset_style(self):
        self.setStyleSheet(self.default_style())
        self.setAlignment(Qt.AlignmentFlag.AlignRight)


class ConditionDisplay(Display):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("font-size: 40px;"
                           "font-weight: italic;"
                           "font-style: italic;"
                           "border: 3px inset darkslategray;"
                           "color: darkslategray;"
                           "background-color: honeydew;"
                           "border-radius: 10px;"
                           "padding: 10px;"
                           "margin: 0;")
        self.setAlignment(Qt.AlignmentFlag.AlignRight)


class Buttons(QPushButton):
    def __init__(self):
        super().__init__()


class DelButton(Buttons):
    def __init__(self):
        super().__init__()
        self.setText("Del")
        self.setStyleSheet("""QPushButton {
        font-size: 20px;
        font-style: italic;
        font-weight: italic;
        background-color: ivory;
        border-radius: 15px;
        padding: 10px;
        border: 1px inset darkslategray;
        }
        QPushButton:hover {
        font-size: 20px;
        font-style: italic;
        font-weight: italic;
        background-color: lemonchiffon;
        border-radius: 15px;
        padding: 10px;
        border: 1px inset darkslategray;
        }
        """)


class CButton(Buttons):
    def __init__(self):
        super().__init__()
        self.setText("C")
        self.setStyleSheet("""QPushButton{
               font-size: 20px;
               font-style: italic;
               font-weight: italic;
               background-color: salmon;
               border-radius: 15px;
               padding: 10px;
               border: 1px inset darkslategray;
               }
               QPushButton:hover {
                 font-size: 20px;
               font-style: italic;
               font-weight: italic;
               background-color: tomato;
               border-radius: 15px;
               padding: 10px;
               border: 1px inset darkslategray;
               }""")


class DivisorButton(Buttons):
    def __init__(self):
        super().__init__()
        self.setText("/")
        self.setStyleSheet("""QPushButton {
              font-size: 20px;
              font-style: italic;
              font-weight: italic;
              background-color: ivory;
              border-radius: 15px;
              padding: 10px;
              border: 1px inset darkslategray;
              }
              QPushButton:hover {
              font-size: 20px;
              font-style: italic;
              font-weight: italic;
              background-color: lemonchiffon;
              border-radius: 15px;
              padding: 10px;
              border: 1px inset darkslategray;
              }
              """)


class Number(Buttons):
    def __init__(self, number):
        super().__init__()
        self.number = number
        self.setText(self.number)
        self.setStyleSheet("""QPushButton{
               font-size: 20px;
               font-style: italic;
               font-weight: italic;
               background-color: lightcyan;
               border-radius: 15px;
               padding: 10px;
               border: 1px inset darkslategray;
               }
               QPushButton:hover {
                 font-size: 20px;
               font-style: italic;
               font-weight: italic;
               background-color: paleturquoise;
               border-radius: 15px;
               padding: 10px;
               border: 1px inset darkslategray;
               }""")


class Symbol(Buttons):
    def __init__(self, symbol):
        super().__init__()
        self.symbol = symbol
        self.setText(self.symbol)
        self.setStyleSheet("""QPushButton {
              font-size: 20px;
              font-style: italic;
              font-weight: italic;
              background-color: ivory;
              border-radius: 15px;
              padding: 10px;
              border: 1px inset darkslategray;
              }
              QPushButton:hover {
              font-size: 20px;
              font-style: italic;
              font-weight: italic;
              background-color: lemonchiffon;
              border-radius: 15px;
              padding: 10px;
              border: 1px inset darkslategray;
              }
              """)


class ResultButton(Buttons):
    def __init__(self):
        super().__init__()
        self.setText("=")
        self.setStyleSheet("""QPushButton{
               font-size: 20px;
               font-style: italic;
               font-weight: italic;
               background-color: palegreen;
               border-radius: 15px;
               padding: 10px;
               border: 1px inset darkslategray;
               }
               QPushButton:hover {
                 font-size: 20px;
               font-style: italic;
               font-weight: italic;
               background-color: chartreuse;
               border-radius: 15px;
               padding: 10px;
               border: 1px inset darkslategray;
               }""")


class Grid(QGridLayout):
    def __init__(self):
        super().__init__()
        self.result_display = ResultDisplay()
        self.condition_display = ConditionDisplay()
        self.addWidget(self.result_display, 0, 0, 1, 4)
        self.addWidget(self.condition_display, 1, 0, 1, 4)
        self.add_buttons()
        self.setContentsMargins(0, 5, 0, 450)

    def clicked_button(self):
        sender = self.sender()
        sender = cast(QPushButton, sender)

        if sender:
            text_on_clicked_button = sender.text()

            if text_on_clicked_button == "Del":
                self.result_display.reset_style()
                current_text = self.condition_display.text()
                self.result_display.clear()
                self.condition_display.setText(current_text[:-1])
            elif text_on_clicked_button == "C":
                self.result_display.reset_style()
                self.condition_display.clear()
                self.result_display.clear()
            elif text_on_clicked_button != "=":

                current_text = self.condition_display.text()
                self.condition_display.setText(current_text + text_on_clicked_button)
            else:

                try:
                    result = str(eval(self.condition_display.text()))
                    self.result_display.setText(result[:7])
                except Exception:
                    self.result_display.error_message()

    def add_buttons(self):

        c_button = CButton()
        self.addWidget(c_button, 2, 0, 1, 2)
        c_button.clicked.connect(self.clicked_button)

        buttons_title = ['7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+', '0', '.']
        del_button = DelButton()
        self.addWidget(del_button, 2, 2, 1, 1)
        del_button.clicked.connect(self.clicked_button)

        div_button = DivisorButton()
        self.addWidget(div_button, 2, 3, 1, 1)
        div_button.clicked.connect(self.clicked_button)

        result_button = ResultButton()
        self.addWidget(result_button, 6, 2, 1, 2)
        result_button.clicked.connect(self.clicked_button)

        for i, button in enumerate(buttons_title):

            if button in ("-", "*", "+"):
                b = Symbol(button)
            else:
                b = Number(button)
            b.clicked.connect(self.clicked_button)
            row = i // 4 + 3
            col = i % 4
            self.addWidget(b, row, col)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Simply Calculator")
        self.setGeometry(10, 10, 500, 500)
        self.setStyleSheet("background-color: whitesmoke;")
        layout = QVBoxLayout()
        self.setLayout(layout)

        grid = Grid()
        layout.addLayout(grid)


app = QApplication(sys.argv)

window = MyApp()

window.show()
app.exec()
