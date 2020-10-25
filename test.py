# str = [['0.01', '3', '2020-10-13  06:52:44', '1.0', '1.0', '游標卡尺', '111 - 1', '1 - 1'], ['1', '3', '2020-10-13  06:52:47', '1.0', '1.0', '3', '111 - 1', '1 - 2'], ['0.01', '3', '2020-10-13  06:52:55', '1.0', '1.0', '游標卡尺', '111 - 1', '1 - 3'], ['10', '3', '2020-10-13  06:52:58', '1.0', '1.0', '3', '111 - 1', '2 - 1'], ['6.65', '3', '2020-10-13  06:53:11', '1.0', '1.0', '3', '111 - 1', '2 - 2'], ['2.24', '3', '2020-10-13  06:53:06', '1.0', '1.0', '游標卡尺', '111 - 1', '2 - 3'], ['8.73', '3', '2020-10-13  06:53:07', '1.0', '1.0', '游標卡尺', '111 - 1', '3 - 1'], ['5.78', '3', '2020-10-13  06:53:07', '1.0', '1.0', '游標卡尺', '111 - 1', '3 - 2'], ['1.87', '3', '2020-10-13  06:53:08', '1.0', '1.0', '游標卡尺', '111 - 1', '3 - 3'], ['10.78', '3', '2020-10-13  06:53:09', '1.0', '1.0', '游標卡尺', '111 - 1', '4 - 1'], ['6.05', '3', '2020-10-13  06:53:11', '1.0', '1.0', '游標卡尺', '111 - 1', '4 - 2'], ['10', '3', '2020-10-13  06:53:32', '9.0', '9.5', '3', '555 - 1', '1 - 1'], ['10', '3', '2020-10-13  06:54:32', '1.0', '1.0', '3', '111 - 1', '4 - 3']]
# print(len(str))
# # x = [tuple(a[-1].split(" - ")) for a in str]
# x = [[a[0]] + [tuple(a[-1].split(' - '))] for a in str]
# y = sorted(x, key= lambda s: int(s[-1][0]))
# print(x, '\n\n')
# print(y)
# a = [['6.94', 'mm', '2020-10-13  20:45:42', '1.0', '2.5', '游標卡尺', '111 - 1', '1 - 1'], ['6.94', 'mm', '2020-10-13  20:45:43', '1.0', '2.5', '游標卡尺', '111 - 1', '1 - 2'], ['6.94', 'mm', '2020-10-13  20:45:43', '1.0', '2.5', '游標卡尺', '111 - 1', '1 - 3'], ['6.94', 'mm', '2020-10-13  20:45:46', '9.0', '9.5', '游標卡尺', '555 - 1', '1 - 1'], ['6.94', 'mm', '2020-10-13  20:45:47', '9.0', '9.5', '游標卡尺', '555 - 1', '1 - 2'], ['10', 'mm', '2020-10-13  20:47:15', '9.0', '9.5', '3', '555 - 1', '1 - 3'], ['6.94', 'mm', '2020-10-13  20:46:10', '9.0', '9.5', '游標卡尺', '555 - 2', '1 - 1'], ['6.94', 'mm', '2020-10-13  20:46:10', '9.0', '9.5', '游標卡尺', '555 - 2', '1 - 2'], ['6.94', 'mm', '2020-10-13  20:46:11', '9.0', '9.5', '游標卡尺', '555 - 2', '1 - 3'], ['6.94', 'mm', '2020-10-13  20:46:24', '1.0', '2.5', '游標卡尺', '111 - 1', '2 - 1'], ['10', 'mm', '2020-10-13  20:46:32', '1.0', '2.5', '3', '111 - 1', '2 - 2']]
# print(len(a))
# a = float(0.4)
# print(format(a, ".3f"))

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.myButton = QtWidgets.QPushButton(self)
        self.myButton.setObjectName("myButton")
        self.myButton.setText("Test")
        self.myButton.clicked.connect(self.msg)

    def msg(self):
        directory1 = QFileDialog.getExistingDirectory(None,
                                                      "選取資料夾")
        print("選取資料夾%s" % directory1)
        # fileName1, filetype = QFileDialog.getOpenFileName(self,
        #                                                   "選取檔案",
        #                                                   "./",
        #                                                   "All Files (*);;Text Files (*.txt)")  # 設定副檔名過濾,注意用雙分號間隔
        # print(fileName1, filetype)
        # files, ok1 = QFileDialog.getOpenFileNames(self,
        #                                           "多檔案選擇",
        #                                           "./",
        #                                           "All Files (*);;Text Files (*.txt)")
        # print(files, ok1)
        # fileName2, ok2 = QFileDialog.getSaveFileName(self,
        #                                              "檔案儲存",
        #                                              "./")
        #

if __name__=="__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())