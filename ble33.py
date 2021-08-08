# import serial  # 引用pySerial模組
#
# COM_PORT = 'COM10'  # 指定通訊埠名稱
# BAUD_RATES = 9600  # 設定傳輸速率
# ser = serial.Serial(COM_PORT, BAUD_RATES)  # 初始化序列通訊埠
# try:
#     while True:
#         while ser.in_waiting:  # 若收到序列資料
#             data_raw = ser.readline()  # 讀取一行
#             data = data_raw.decode()  # 用預設的UTF-8解碼
#             print('接收到的原始資料：', data_raw)
#             print('接收到的資料：', data)
#
# except KeyboardInterrupt:
#     ser.close()  # 清除序列通訊物件
#
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # informations
        info = "info"
        new_info = "new info "

        # set the title
        self.setWindowTitle("Label")

        # setting  the geometry of window
        self.setGeometry(0, 0, 400, 300)

        # creating a label widget
        self.label_1 = QLabel(info, self)

        # moving position
        self.label_1.move(100, 100)

        # setting up border
        self.label_1.setStyleSheet("border: 1px solid black;")

        # creating a label widget
        self.label_2 = QLabel(info, self)

        # moving position
        self.label_2.move(100, 150)

        # setting up border
        self.label_2.setStyleSheet("border: 1px solid black;")

        # changing the text of label
        self.label_2.setText(new_info)

        # show all the widgets
        self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
