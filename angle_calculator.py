import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QIcon, QDoubleValidator
from PyQt5.QtCore import Qt

class AngleCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("角度計算器")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(500, 300, 400, 300)
        self.initUI()

    def initUI(self):
        f_label = QFont("Microsoft JhengHei", 11)
        f_result = QFont("Microsoft JhengHei", 12, QFont.Bold)
        f_sign = QFont("Microsoft JhengHei", 9, QFont.StyleItalic)
        validator = QDoubleValidator(-9999.0, 9999.0, 3)

        # 屏距
        self.dist_input = QLineEdit()
        self.dist_input.setPlaceholderText("輸入屏距 (例：2)")
        self.dist_input.setValidator(validator)
        self.dist_input.setInputMethodHints(Qt.ImhDigitsOnly)
        self.dist_input.returnPressed.connect(lambda: self.wind_force_input.setFocus())

        # 風力
        self.wind_force_input = QLineEdit()
        self.wind_force_input.setPlaceholderText("輸入風力 (例：1.5 或 -1.5)")
        self.wind_force_input.setValidator(validator)
        self.wind_force_input.setInputMethodHints(Qt.ImhDigitsOnly)
        self.wind_force_input.returnPressed.connect(self.calculate_angle)

        # 按鈕
        calc_btn = QPushButton("計算角度")
        calc_btn.clicked.connect(self.calculate_angle)
        clr_btn = QPushButton("清除風力")
        clr_btn.clicked.connect(lambda: (self.wind_force_input.clear(), self.result_label.clear()))

        # 結果
        self.result_label = QLabel("")
        self.result_label.setFont(f_result)
        self.result_label.setStyleSheet("color: blue; margin-top: 10px;")

        # 底部標籤
        sign = QLabel("© 2025  Made by BroJack")
        sign.setFont(f_sign)
        sign.setAlignment(Qt.AlignCenter)
        sign.setStyleSheet("color: gray; margin-top: 12px;")

        # 版面
        layout = QVBoxLayout()
        for lbl, widget in [("屏距：", self.dist_input), ("風力：", self.wind_force_input)]:
            row = QHBoxLayout()
            label = QLabel(lbl)
            label.setFont(f_label)
            row.addWidget(label)
            row.addWidget(widget)
            layout.addLayout(row)
        btn_row = QHBoxLayout()
        btn_row.addWidget(calc_btn)
        btn_row.addWidget(clr_btn)
        layout.addLayout(btn_row)
        layout.addWidget(self.result_label)
        layout.addWidget(sign)
        self.setLayout(layout)

    def calculate_angle(self):
        try:
            dist = float(self.dist_input.text())
            wind = float(self.wind_force_input.text())
            angle = (90 - dist) + (wind * 2)
            direction = "順風" if wind > 0 else "逆風"
            strength = "95 或少一些" if wind > 0 else "95 或多一些"
            self.result_label.setText(
                f"方向：{direction}\n"
                f"角度 = {angle:.1f}°\n"
                f"建議角度：{round(angle)}°\n"
                f"建議力度：{strength}"
            )
        except ValueError:
            self.result_label.setText("請輸入正確的數字！")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AngleCalculator()
    win.show()
    sys.exit(app.exec_())
