from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QLineEdit, QWidget, QGridLayout

class CalculatorApp(QMainWindow):
    def __init__(self):
        super(CalculatorApp, self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.line_edit = QLineEdit(self)
        self.layout.addWidget(self.line_edit)

        grid_layout = QGridLayout()

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row, col = 0, 0
        for button_text in buttons:
            button = QPushButton(button_text, self)
            button.clicked.connect(self.on_button_click)
            grid_layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # 新しいボタンを追加
        clear_button = QPushButton('C', self)
        clear_button.clicked.connect(self.clear_last)
        grid_layout.addWidget(clear_button, row, col)

        all_clear_button = QPushButton('CE', self)
        all_clear_button.clicked.connect(self.clear_all)
        grid_layout.addWidget(all_clear_button, row, col + 1)

        self.layout.addLayout(grid_layout)

        self.last_button_is_operator = False  # 直前のボタンが演算子かどうかのフラグ

    def on_button_click(self):
        button = self.sender()
        current_text = self.line_edit.text()

        if button.text() == '=':
            try:
                result = eval(current_text)
                self.line_edit.setText(str(result))
            except Exception as e:
                self.line_edit.setText("Error")
        else:
            # 直前のボタンが演算子で、かつ今押されたボタンも演算子の場合、処理をスキップ
            if self.last_button_is_operator and button.text() in ['/', '*', '-', '+']:
                return

            self.line_edit.setText(current_text + button.text())
            self.last_button_is_operator = button.text() in ['/', '*', '-', '+']

    def clear_last(self):
        current_text = self.line_edit.text()
        if current_text:
            self.line_edit.setText(current_text[:-1])

            # 直前のボタンが演算子の場合、フラグも更新
            if current_text[-1] in ['/', '*', '-', '+']:
                self.last_button_is_operator = True
            else:
                self.last_button_is_operator = False

    def clear_all(self):
        self.line_edit.clear()
        self.last_button_is_operator = False
