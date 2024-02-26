from PySide6.QtWidgets import QApplication
from calculator import CalculatorApp

if __name__ == "__main__":
    app = QApplication([])
    window = CalculatorApp()
    window.show()
    app.exec()
