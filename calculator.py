from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys


class RetroCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.current_expression = ""

    def initUI(self):
        self.setWindowTitle("Retro Calculator")
        self.setGeometry(100, 100, 250, 400)
        self.setStyleSheet("background: white;")

        layout = QVBoxLayout()

        # Display label
        self.display = QLabel("0", self)
        self.display.setFont(QFont("Courier", 20))  # Pixelated font style
        self.display.setStyleSheet("background: white; border: 2px solid black; padding: 5px; color: black;")
        self.display.setAlignment(Qt.AlignRight)
        layout.addWidget(self.display)

        # Grid layout for buttons
        grid_layout = QGridLayout()
        buttons = [
            ('C', 0, 0), ('E', 0, 1), ('=', 0, 2), ('*', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 1)
        ]

        for btn_text, row, col in buttons:
            button = QPushButton(btn_text, self)
            button.setFont(QFont("Courier", 16))  # Pixelated font
            button.setStyleSheet("background: white; border: 2px solid black; color: black;")
            button.clicked.connect(lambda checked, text=btn_text: self.on_button_click(text))
            grid_layout.addWidget(button, row, col)

        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def on_button_click(self, button_text):
        if button_text == "C":
            self.current_expression = ""
        elif button_text == "E":
            self.current_expression = self.current_expression[:-1]
        elif button_text == "=":
            try:
                self.current_expression = str(eval(self.current_expression))
            except Exception:
                self.current_expression = "Error"
        else:
            self.current_expression += button_text

        self.display.setText(self.current_expression if self.current_expression else "0")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RetroCalculator()
    window.show()
    sys.exit(app.exec_())
