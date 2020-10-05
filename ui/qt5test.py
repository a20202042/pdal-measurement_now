from PyQt5 import QtWidgets, QtGui ,QtCore
from PyQt5.QtWidgets import QMessageBox, QAbstractItemView, QTableWidgetItem
from qt5 import Ui_MainWindow, Ui_Form, Ui_toolcheck, Ui_widget_projectcheck , Ui_check
import sys, re, time, serial.tools.list_ports
import toolconnect, sql_connect, measure
from PyQt5.QtCore import QThread, pyqtSignal

# GLOBAL VARIABLES
selected_com_port = ''

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, work_order_data, measure_item_data, project_name, tool_com):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('D:/GitHub/pythonProject/ico.ico'))
        self.main_window_center()
        self.tool_com = tool_com
        self.measure_mode = ""
        self.measure_item_data = measure_item_data
        self.measure_project_time = time.strftime("%Y-%m-%d", time.localtime())#量測日期
        self.measure_time = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime())#量測數值日期
        self.measure_value_data = []
        self.measure_yield = []
        self.measure_number = 0
        self.measure_color_number = 1
        self.measure_column = int
        self.measure_row = int
        self.measure_row_number = 1

        self.tb = self.addToolBar("open")
        self.new = QtWidgets.QAction(QtGui.QIcon("D:\GitHub\pythonProject\po.png"), "UP project", self)
        self.tb.addAction(self.new)
        self.new = QtWidgets.QAction(QtGui.QIcon("D:\GitHub\pythonProject\project_item.png"), "project_item", self)
        self.tb.addAction(self.new)
        self.new = QtWidgets.QAction(QtGui.QIcon("D:\GitHub\pythonProject\measure_choose.png"), "project_choose", self)
        self.tb.addAction(self.new)

        self.tb.actionTriggered[QtWidgets.QAction].connect(self.toolbar)#toolbar槽函數
        self.ui.label_4.setText( "量測專案名稱：%s"%project_name)


        self.measure_value = measure_thread()
        self.measure_value.measure_value.connect(self.setmeasurevalue)
        self.ui.tableWidget_3_measure.itemClicked.connect(self.get_measure_item)
        # self.measure_value.measure_unit.connect()

        # self.work_order_data = work_order_data
        # self.work_order_item = ["專案名稱", "工單", "件號", "件數", "材料", "機台名稱", "批號", "班別", "量測人員", "備註"]
        # self.ui.tableWidget_project_item.setRowCount(len(self.work_order_item))
        # self.ui.tableWidget_project_item.setVerticalHeaderLabels(self.work_order_item)
        # self.ui.tableWidget_project_item.setColumnCount(1)
        # self.ui.tableWidget_project_item.setHorizontalHeaderLabels(["參數"])
        # for i in range(len(self.work_order_item)):
        #     self.ui.tableWidget_project_item.setItem(i, 0, QTableWidgetItem(str(self.work_order_data[0][i])))
        # self.ui.tableWidget_project_item.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.ui.tableWidget_project_item.resizeRowsToContents()
        # self.ui.tableWidget_project_item.resizeColumnsToContents()
        # self.ui.tableWidget_project_item.setSelectionBehavior(self.ui.tableWidget_project_item.SelectRows)

        self.measure_value_item = ['量測屬性值', '量測日期', 'GO/NOGO']
        self.ui.tableWidget_project_item.setRowCount(3)
        self.ui.tableWidget_project_item.setColumnCount(1)
        self.ui.tableWidget_project_item.horizontalHeader().setVisible(False)
        self.ui.tableWidget_project_item.setVerticalHeaderLabels(self.measure_value_item)
        self.ui.tableWidget_project_item.setItem(0, 0, QTableWidgetItem('量測屬性質'))
        # self.ui.tableWidget_measure_value_item.setEditTriggers(QAbstractItemView.NoEditTriggers)#不可編輯
        self.ui.tableWidget_measure_value_item.resizeRowsToContents()
        self.ui.tableWidget_measure_value_item.setSelectionBehavior(self.ui.tableWidget_measure_value_item.SelectRows)

        self.ui.tableWidget_project_item.setRowCount(5)
        self.project_item = ["專案名稱", "量測日期", "良數", "不良數", "總數"]
        self.ui.tableWidget_project_item.setColumnCount(1)
        self.ui.tableWidget_project_item.horizontalHeader().setVisible(False)
        self.ui.tableWidget_project_item.setVerticalHeaderLabels(self.project_item)
        self.ui.tableWidget_project_item.setItem(0, 0, QTableWidgetItem(str(project_name)))
        self.ui.tableWidget_project_item.setItem(0, 1, QTableWidgetItem(str(self.measure_project_time)))
        self.ui.tableWidget_project_item.resizeRowsToContents()
        self.ui.tableWidget_project_item.resizeColumnsToContents()


        self.measure_item = ["專案名稱", "量測項目名稱", "量測數值上限", "量測數值下限", "量測數值中心", "量測小數點位數","量測單位", "量具名稱" ]
        print(self.measure_item_data)
        self.ui.tableWidget_3_measure.setColumnCount(len(measure_item_data))
        self.number = ["1", "2", "3", "4", "5"]
        self.ui.tableWidget_3_measure.setRowCount(len(self.measure_item)+len(self.number))
        self.ui.tableWidget_3_measure.horizontalHeader().setVisible(False)
        self.ui.tableWidget_3_measure.setVerticalHeaderLabels(self.measure_item+self.number)
        print(measure_item_data)
        for i in range(0,len(measure_item_data)):
            for i_2 in range(0,len(self.measure_item)):
                self.ui.tableWidget_3_measure.setItem(i_2, i, QTableWidgetItem(str(measure_item_data[i][i_2])))
        self.measure_tool_start()

    def toolbar(self, a):
        print(a.text())
        if a.text() == "project_item":
            print("1")
        elif a.text() == "project_choose":
            print("輸入模式選擇")
            self.window = tool_measure_choose()
            self.window.measure_mode.connect(self.get_measure_mode)
            self.window.show()
        elif a.text() == "UP project":
            self.project_value_insert_sql()
            print("檔案上傳完成")
    def get_measure_mode(self, mode):
        self.measure_mode = str(mode)
        print("主視窗%s"%mode)
    def tool_value_reture(self):
        print("ok")
    def main_window_center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height() - size.height())/2)
    def closeEvent(self, QCloseEvent):
        self.measure_value.is_on = False
        print('self.measure_value.is_on=%s' % self.measure_value.is_on)
        self.window = TOOLWindow()
        self.window.show()
    def main_window_center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height() - size.height())/2)

    def setmeasurevalue(self, value):
        if self.measure_mode == "零件部位" or self.measure_mode == "":
            if self.measure_column != self.ui.tableWidget_3_measure.currentColumn():
                self.measure_number = 0
                print("資料清除")
            if self.measure_row != self.ui.tableWidget_3_measure.currentRow():
                self.measure_number = 0
                print("資料清除")
            self.measure_column = self.ui.tableWidget_3_measure.currentColumn()  # 行數檢查換行時歸零
            self.measure_row = self.ui.tableWidget_3_measure.currentRow()

            self.measure_time = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime())  # 量測數值日期
            self.value = value
            self.row = self.ui.tableWidget_3_measure.currentRow()
            self.column = self.ui.tableWidget_3_measure.currentColumn()
            # for i in range(self.row, len(self.number)):

            self.ui.tableWidget_3_measure.setItem(self.row + self.measure_number, self.column,
                                                  QTableWidgetItem(str(self.value)))
            self.ui.tableWidget_3_measure.item(self.row, self.column).setSelected(False)

            # new_m = QTableWidgetItem("")
            # new_m.setBackground(QtGui.QBrush(QtGui.QColor(0, 255, 0)))
            # self.ui.tableWidget_3_measure.setItem(self.row+self.measure_color_number, self.column, new_m)
            # self.measure_color_number = self.measure_color_number+1
            # print(self.row, self.column)
            # print(self.row+self.measure_number, self.column)
            # new_m.setSelected(True)
            # item.setBackground(QtGui.QBrush(QtGui.QColor(0,255,0)))
            # self.ui.tableWidget_3_measure.verticalScrollBar().setSliderPosition(item.row())

            self.gonogo = measure.measure_go_nogo_calculate(
                float(self.ui.tableWidget_3_measure.item(2, self.column).text()),
                float(self.ui.tableWidget_3_measure.item(3, self.column).text()),
                float(self.value))
            if self.gonogo == True:
                self.ui.label_LOGO.setPixmap(QtGui.QPixmap("D:/GitHub/pythonProject/GO.PNG"))  # go
                self.ui.tableWidget_measure_value_item.setItem(0, 2, QTableWidgetItem("GO"))
                self.ui.tableWidget_measure_value_item.setItem(0, 1, QTableWidgetItem(self.measure_time))
                self.ui.tableWidget_measure_value_item.resizeColumnsToContents()
            elif self.gonogo == False:
                self.ui.tableWidget_measure_value_item.setItem(0, 1, QTableWidgetItem(self.measure_time))
                self.ui.label_LOGO.setPixmap(QtGui.QPixmap("D:/GitHub/pythonProject/NOGO.PNG"))  # nogo
                self.ui.tableWidget_measure_value_item.setItem(0, 2, QTableWidgetItem("NO GO"))
                setcolor = QTableWidgetItem(str(self.value))
                setcolor.setForeground(QtGui.QBrush(QtGui.QColor(255, 0, 0)))
                self.ui.tableWidget_3_measure.setItem(self.row + self.measure_number, self.column, setcolor)
                self.ui.tableWidget_measure_value_item.resizeColumnsToContents()

            self.measure_number = self.measure_number + 1

            self.measure_value_new_data = [self.value, "mm", self.measure_time,
                                           self.ui.tableWidget_3_measure.item(1, self.column).text(),
                                           self.ui.tableWidget_3_measure.item(0, self.column).text(),
                                           self.row + self.measure_number]

            # 判別匯入的資料是否在同一格中
            if len(self.measure_value_data) == 0:  # 第一筆資料匯入
                self.measure_value_data.append(self.measure_value_new_data)
            self.measure_repeat = False
            for item in self.measure_value_data:  # 從資料傳列中找尋
                if item[3] == self.measure_value_new_data[3] and item[5] == self.measure_value_new_data[5]:  # 項目名稱以及列數一樣
                    self.measure_repeat = True
                    self.measure_repeat_delet = item
            if self.measure_repeat == None:
                self.measure_repeat = False
            if self.measure_repeat == True:
                self.measure_value_data.remove(self.measure_repeat_delet)
                self.measure_value_data.append(self.measure_value_new_data)
            elif self.measure_repeat == False:
                self.measure_value_data.append(self.measure_value_new_data)

            # print(self.measure_value_data)
            for item in self.measure_value_data:  # 每次收集並計算
                if item[3] == self.measure_value_new_data[3]:
                    self.measure_yield.append(item[0])
            # print(self.measure_yield)
            (value_excellent, value_inferior, all) = measure.measure_Yield(
                float(self.ui.tableWidget_3_measure.item(2, self.column).text()),
                float(self.ui.tableWidget_3_measure.item(3, self.column).text()),
                self.measure_yield)
            print(value_excellent, value_inferior, all)
            self.ui.tableWidget_project_item.setItem(0, 2, QTableWidgetItem(str(value_excellent)))
            self.ui.tableWidget_project_item.setItem(0, 3, QTableWidgetItem(str(value_inferior)))
            self.ui.tableWidget_project_item.setItem(0, 4, QTableWidgetItem(str(all)))
            self.measure_yield.clear()

            if all + 1 > len(self.number):  # 如果總數大於已經有的數量
                self.ui.tableWidget_3_measure.setRowCount(
                    len(self.measure_item) + 5 + self.measure_row_number)  # 列數為量測item+原本5位+應該增加的數量
                self.measure_row_number = self.measure_row_number + 1
                self.number.append(str(all + 1))
                self.ui.tableWidget_3_measure.setVerticalHeaderLabels(self.measure_item + self.number)
                print(all)
                print(self.measure_row_number)
            # print(str(self.ui.tableWidget_3_measure.item(self.column, 3).text()))
            # [123.0, 'mm', datetime.date(2020, 9, 6), 1量測項目名稱, 1量測專案名稱]
            # text = str(self.value)
            # items = self.ui.tableWidget_3_measure.findItems(text,QtCore.Qt.MatchExactly)
            # item = items[0]
            # item.setSelected(True)

        elif self.measure_mode =="依照件數": #另一種量測方式
            print("mode_2")
            if self.measure_column != self.ui.tableWidget_3_measure.currentColumn():
                self.measure_number = 0
                print("資料清除")
            if self.measure_row != self.ui.tableWidget_3_measure.currentRow():
                self.measure_number = 0
                print("資料清除")
            self.measure_row = self.ui.tableWidget_3_measure.currentRow()
            self.measure_column = self.ui.tableWidget_3_measure.currentColumn()
            self.measure_time = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime())
            self.value = value
            self.pieces_cloumn = self.ui.tableWidget_3_measure.currentColumn()
            self.pieces_row = self.ui.tableWidget_3_measure.currentRow()
            self.ui.tableWidget_3_measure.setItem(self.pieces_row,self.pieces_cloumn+self.measure_number,
                                                  QTableWidgetItem(str(self.value)))
            self.ui.tableWidget_3_measure.item(self.pieces_row, self.pieces_cloumn).setSelected(False)
            self.measure_number = self.measure_number + 1

            self.gonogo = measure.measure_go_nogo_calculate(
                float(self.ui.tableWidget_3_measure.item(2, self.pieces_cloumn).text()),
                float(self.ui.tableWidget_3_measure.item(3, self.pieces_cloumn).text()),
                float(self.value)
            )
            print(self.ui.tableWidget_3_measure.item(2, self.pieces_cloumn).text())
            print(self.gonogo)

    def measure_tool_start(self):
        self.measure_value.is_on = True
        self.measure_value.set_port(str(self.tool_com))
        self.measure_value.start()

    def get_measure_item(self, item):
        column = self.ui.tableWidget_3_measure.currentColumn()  # 行數檢查換行時歸零
        row = self.ui.tableWidget_3_measure.currentRow()

        if column is None:
            print("not")

        for item in self.measure_value_data:#每次收集並計算
            if item[3] == self.ui.tableWidget_3_measure.item(1, column).text():
                self.measure_yield.append(item[0])
        (value_excellent, value_inferior, all) = measure.measure_Yield(
            float(self.ui.tableWidget_3_measure.item(2, column).text()),
            float(self.ui.tableWidget_3_measure.item(3, column).text()),
            self.measure_yield)
        self.ui.tableWidget_project_item.setItem(0, 2, QTableWidgetItem(str(value_excellent)))
        self.ui.tableWidget_project_item.setItem(0, 3, QTableWidgetItem(str(value_inferior)))
        self.ui.tableWidget_project_item.setItem(0, 4, QTableWidgetItem(str(all)))
        self.measure_yield.clear()
        self.gonogo = measure.measure_go_nogo_calculate(
            float(self.ui.tableWidget_3_measure.item(2, column).text()),
            float(self.ui.tableWidget_3_measure.item(3, column).text()),
            float(self.ui.tableWidget_3_measure.item(row, column).text()))
        if self.gonogo == True:
            self.ui.label_LOGO.setPixmap(QtGui.QPixmap("D:/GitHub/pythonProject/GO.PNG"))  # go
            self.ui.tableWidget_measure_value_item.setItem(0, 2, QTableWidgetItem("GO"))
            self.ui.tableWidget_measure_value_item.resizeColumnsToContents()
        elif self.gonogo == False:
            self.ui.label_LOGO.setPixmap(QtGui.QPixmap("D:/GitHub/pythonProject/NOGO.PNG"))  # nogo
            self.ui.tableWidget_measure_value_item.setItem(0, 2, QTableWidgetItem("NO GO"))
            self.ui.tableWidget_measure_value_item.resizeColumnsToContents()

        for i in self.measure_value_data:
            if i[5] == row+1:
                print(i)
                self.item_time = i[2]
        self.ui.tableWidget_measure_value_item.setItem(0, 1, QTableWidgetItem(self.item_time))
    def project_value_insert_sql(self):
        print(self.measure_value_data)
        for item in self.measure_value_data:
            if len(item)>5:
                item.pop(-1)
                print(item)
                sql = sql_connect.sql_connect()
                sql.sql_inaert_value(item)
        print(self.measure_value_data)
        pass

class tool_measure_choose(QtWidgets.QWidget, Ui_check):
    measure_mode = pyqtSignal(str)
    def __init__(self):
        super(tool_measure_choose, self).__init__()
        self.ui = Ui_check()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('D:/GitHub/pythonProject/ico.ico'))
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.radioButton.clicked.connect(self.mode_show)
        self.ui.radioButton_2.clicked.connect(self.mode_show)
        self.ui.pushButton_setup.clicked.connect(self.mode_set_ok)
    def mode_show(self):
        rad = self.sender()
        if rad.text() == "依照零件部位":
            self.mode = "零件部位"
        elif rad.text() == "依照件數":
            self.mode = "依照件數"
        print("子視窗%s" % self.mode)
    def mode_set_ok(self):
        mode = self.mode
        self.measure_mode.emit(mode)
        self.close()
    def close(self):
        self.hide()

class project_check_window(QtWidgets.QWidget,Ui_widget_projectcheck):
    def __init__(self, data_all, tool_ok_com):
        super(project_check_window, self).__init__()
        self.tool_com = tool_ok_com
        self.sql_project_data = data_all
        self.ui = Ui_widget_projectcheck()
        self.sql = sql_connect.sql_connect()
        self.setWindowIcon(QtGui.QIcon('D:/GitHub/pythonProject/ico.ico'))
        self.ui.setupUi(self)
        self.ui.pushButton_close.clicked.connect(self.close)
        self.ui.pushButton_cinfirm_project.clicked.connect(self.open_start_measure_window)
        self.ui.pushButton_rest_project.clicked.connect(self.resst_project)

        #匯入量測專案資料
        self.project_name_item = ["專案名稱", "建立日期", "建立人", "備註"]
        self.ui.tableWidget_project.setRowCount(len(self.sql_project_data))
        self.ui.tableWidget_project.setColumnCount(len(self.project_name_item))
        self.ui.tableWidget_project.setHorizontalHeaderLabels(self.project_name_item)
        for i in range(len(self.sql_project_data)):
            for i_2 in range(0,len(self.sql_project_data[i])):
                self.ui.tableWidget_project.setItem(i, i_2, QTableWidgetItem(str(self.sql_project_data[i][i_2])))
        self.ui.tableWidget_project.setEditTriggers(QAbstractItemView.NoEditTriggers)#不可編輯
        self.ui.tableWidget_project.resizeColumnsToContents()#調整欄位大小
        self.ui.tableWidget_project.resizeRowsToContents()#調整欄位大小
        self.ui.tableWidget_project.setSelectionBehavior(self.ui.tableWidget_project.SelectRows)
        self.ui.tableWidget_project.itemClicked.connect(self.set_work_order_measure_item)


    def set_work_order_measure_item(self,item):
        print(self.sql_project_data[item.row()][0])#專案名稱
        self.ui.lineEdit_now_project_name.setText(self.sql_project_data[item.row()][0])
        #匯入工單表單內容
        self.work_order_item = ["專案名稱", "工單", "件號", "件數", "材料", "機台名稱", "批號", "班別", "量測人員", "備註"]
        sql = sql_connect.sql_connect()
        print(self.sql_project_data[item.row()][0])
        self.work_order_data = sql.sql_find_work_order(str(self.sql_project_data[item.row()][0]))
        print(self.work_order_data)
        self.ui.tableWidget_work_order.setRowCount(len(self.work_order_data))
        self.ui.tableWidget_work_order.setColumnCount(len(self.work_order_item))
        self.ui.tableWidget_work_order.setHorizontalHeaderLabels(self.work_order_item)
        self.ui.tableWidget_work_order.verticalHeader().setVisible(False)
        for i in range(len(self.work_order_data)):
            for i_2 in range(0, len(self.work_order_data[i])):
                self.ui.tableWidget_work_order.setItem(i, i_2, QTableWidgetItem(str(self.work_order_data[i][i_2])))
        self.ui.tableWidget_work_order.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget_work_order.resizeColumnsToContents()
        self.ui.tableWidget_work_order.resizeRowsToContents()
        self.ui.tableWidget_work_order.setSelectionBehavior(self.ui.tableWidget_work_order.SelectRows)
        #
        #匯入量測item
        self.measure_item = ["量測專案名稱", "量測項目名稱", "量測數值上限", "量測數值下限", "量測數值中心", "量測小數點位數","量測單位" ,"量具名稱"]
        self.measure_item_data = sql.sql_find_measure_item(self.sql_project_data[item.row()][0])
        self.ui.tableWidget_measureitem.setRowCount(len(self.measure_item_data))
        self.ui.tableWidget_measureitem.setColumnCount(len(self.measure_item))
        self.ui.tableWidget_measureitem.setHorizontalHeaderLabels(self.measure_item)
        print(self.measure_item_data)
        for i in range(len(self.measure_item_data)):
            for i_2 in range(len(self.measure_item_data[i])):
                self.ui.tableWidget_measureitem.setItem(i, i_2, QTableWidgetItem(str(self.measure_item_data[i][i_2])))
        self.ui.tableWidget_measureitem.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget_measureitem.resizeColumnsToContents()
        self.ui.tableWidget_measureitem.resizeRowsToContents()
        self.ui.tableWidget_measureitem.setSelectionBehavior(self.ui.tableWidget_measureitem.SelectRows)
        try :
            if len(self.measure_item_data) == 0:
                self.measure_check = False
            else:
                self.measure_check = True

        except:
            pass
    def resst_project(self):
        self.ui.tableWidget_project.clear()
        self.ui.tableWidget_project.setEditTriggers(QAbstractItemView.CurrentChanged)
        sql = sql_connect.sql_connect()
        self.sql_project_data = sql.sql_all_date("mysite_project")
        self.ui.tableWidget_project.setRowCount(len(self.sql_project_data))
        self.ui.tableWidget_project.setColumnCount(len(self.project_name_item))
        self.ui.tableWidget_project.setHorizontalHeaderLabels(self.project_name_item)
        for i in range(len(self.sql_project_data)):
            for i_2 in range(0, len(self.sql_project_data[i])):
                self.ui.tableWidget_project.setItem(i, i_2, QTableWidgetItem(str(self.sql_project_data[i][i_2])))
        self.ui.tableWidget_project.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget_project.resizeColumnsToContents()
        self.ui.tableWidget_project.resizeRowsToContents()
        self.ui.tableWidget_project.setSelectionBehavior(self.ui.tableWidget_measureitem.SelectRows)

    def close(self):
        self.hide()
        self.window = TOOLWindow()
        self.window.show()

    def closeEvent(self, QCloseEvent):
        self.hide()
        self.window = TOOLWindow()
        self.window.show()

    def open_start_measure_window(self, QCloseEvent):
        if self.measure_check ==True:
            self.hide()
            print(self.ui.lineEdit_now_project_name.text())
            sql = sql_connect.sql_connect()
            self.window = MainWindow(sql.sql_find_work_order(self.ui.lineEdit_now_project_name.text()),
                                     sql.sql_find_measure_item(self.ui.lineEdit_now_project_name.text()),
                                     self.ui.lineEdit_now_project_name.text(),
                                     self.tool_com)
            self.window.show()
        elif self.measure_check == False:
            self.reply = QMessageBox.question(self, 'Message', "量測專案沒有工單以及量測設定", QMessageBox.Yes)
            # if self.reply == QMessageBox.Yes:
            #     print("1")
            # else:
            #     print("2")
class TOOLWindow(QtWidgets.QWidget, Ui_Form):
    com_signal = pyqtSignal(str)
    def __init__(self):
        super(TOOLWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('D:/GitHub/pythonProject/ico.ico'))
        # self.ui.start_measure.clicked.connect(self.open_main_measure_window)
        self.ui.tool_test.clicked.connect(self.open_tool_test)
        self.ui.start_measure.clicked.connect(self.open_porject_check_window)
        # self.ui.excit.clicked.connect(self.close)
        self.main_window_center()
        self.set_ok_con = None

    def main_window_center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height() - size.height())/2)

    def open_porject_check_window(self):
        # check network connections before show window
        from urllib import request, error
        def internet_on():
            try:
                request.urlopen('http://www.google.com', timeout=1)
                return True
            except error.URLError as err:
                return False
        get_internet_stat = internet_on()
        if self.set_ok_con is None:
            self.reply = QMessageBox.question(self, 'Message', "量測量具還未設定", QMessageBox.Yes)
        if get_internet_stat is False:
            self.reply = QMessageBox.warning(self, 'Message', "沒有網路連線", QMessageBox.Yes)
        elif self.set_ok_con is not None and get_internet_stat is True:
            self.hide()
            sql = sql_connect.sql_connect()
            self.window = project_check_window(sql.sql_all_date("mysite_project"), self.set_ok_con)
            self.window.show()

    def send_com_signal(self):
        com = self.set_ok_con
        self.com_signal.emit(com)



    def open_tool_test(self):
        # self.hide()
        self.window = tool_test(toolconnect.com2())
        self.window.mysignal.connect(self.get_signal)
        self.window.show()
        # a = tool_test.return_port()
        # port = tool_test.return_port()
        # print(port)
        # # self.hide()
        # self.Tool_test = QtWidgets.QWidget()
        # self.tool_test_window = tool_test()
        # self.tool_test_window.setupUi(self.Tool_test)
        # self.Tool_test.show()
    # def close(self):
    #     self.hide()
    #     self.Form1 = QtWidgets.QMainWindow()
    #     self.firs_Dialog = MainWindow()
    #     self.firs_Dialog.setupUi(self.Form1)
    #     self.Form1.show()
    def closeEvent(self, QCloseEvent):
        self.reply = QMessageBox.question(self, 'Message',"確定離開量測系統?", QMessageBox.Yes, QMessageBox.No)
        if self.reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
    def get_signal(self, con):
        self.set_ok_con = con
        print(self.set_ok_con)
# 多線程失敗
# class Backendthread(QThread):
#     update_date = pyqtSignal(str)
#     def run(self):
#         while True:
#             date = QDateTime.currentDateTime()
#             currtime = date.toString('yyyy-MM-dd hh:mm:ss')
#             self.update_date.emit( str(currtime) )
#             print(date)
#             time.sleep(1)
# def iniUi(self):
    #     self.backend = Backendthread()
    #     self.backend.start()
    #
    # def hand(self, data):
    #     self.lineEdit_toolvalue.setText(data)

class tool_test(QtWidgets.QWidget,Ui_toolcheck):
    mysignal = pyqtSignal(str)
    def __init__(self, tool_com_all):
        self.tool_com_all = tool_com_all
        super(tool_test, self).__init__()
        self.ui = Ui_toolcheck()
        self.ui.setupUi(self)
        self.main_window_center()
        self.setWindowIcon(QtGui.QIcon('D:/GitHub/pythonProject/ico_1.ico'))
        for com_obj in self.tool_com_all:
            self.ui.comboBox_comname.addItem(com_obj)
        self.measure_value = measure_thread()
        self.measure_value.measure_value.connect(self.setmeasurevalue)
        self.measure_value.measure_tool_name.connect(self.setmeasuretoolname)
        self.ui.Button_tool_connect.clicked.connect(self.measure_tooltest_start)

        self.ui.Button_tool_connect_rest.clicked.connect(self.tool_rest)
        self.ui.pushButton_9.clicked.connect(self.close)
        self.ui.pushButton_10.clicked.connect(self.tool_set_ok)

    def tool_set_ok(self):
        self.measure_value.is_on =False
        self.con = self.set_con[0]
        self.mysignal.emit(self.con)
        self.hide()

    def tool_rest(self):
        self.ui.comboBox_comname.clear()
        rest_com_choose = toolconnect.com2()
        for com_obj in rest_com_choose:
            self.ui.comboBox_comname.addItem(com_obj)
        self.ui.lineEdit_toolname.setText(' ')
        self.ui.lineEdit_toolvalue.setText(' ')
        self.measure_value.is_on = False
        self.measure_value = measure_thread()
        self.measure_value.measure_value.connect(self.setmeasurevalue)
        self.measure_value.measure_tool_name.connect(self.setmeasuretoolname)
        print('self.measure_value.is_on=%s' % self.measure_value.is_on)

    def setmeasurevalue(self, value):
        self.ui.lineEdit_toolvalue.setText(value)

    def setmeasuretoolname(self, name):
        self.ui.lineEdit_toolname.setText(name)

    def closeEvent(self, QCloseEvent):
        self.measure_value.is_on = False
        print('self.measure_value.is_on=%s'%self.measure_value.is_on)
        # self.window = TOOLWindow()
        # self.window.show()

    def main_window_center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height() - size.height())/2)

    def measure_tooltest_start(self):
        self.set_con = re.findall(r"\d",self.ui.comboBox_comname.currentText())
        print('self.set_con=%s'%self.set_con[0])
        self.measure_value.is_on = True
        self.measure_value.set_port(self.set_con[0])
        self.measure_value.start()

    def close(self):
        self.hide()
        self.measure_value.is_on = False
        print('self.measure_value.is_on=%s' % self.measure_value.is_on)
        # self.window = TOOLWindow()
        # self.window.show()

class measure_thread(QThread):
    measure_value = pyqtSignal(str)
    measure_tool_name = pyqtSignal(str)
    measure_unit = pyqtSignal(str)
    def __init__(self, parent=None):
        super(measure_thread, self).__init__(parent)
        self.is_on = True
    def set_port(self, port):
        self.set_port = port
    def run(self):
        while self.is_on:
            returenlist = self.serial_test(self.set_port)
            if self.is_on == False:
                break
            self.measure_value.emit(str(returenlist[0]))
            self.measure_tool_name.emit(str(returenlist[1]))
            self.measure_unit.emit(str(returenlist[2]))

    def serial_test(self,comnumber):
        COM_PORT = ("COM%s" % comnumber)  # 指定通訊埠名稱
        BAUD_RATES = 57600  # 設定傳輸速率
        BYTE_SIZE = 8
        PARITY = 'N'
        STOP_BITS = 1
        ser = serial.Serial(COM_PORT, BAUD_RATES, BYTE_SIZE, PARITY, STOP_BITS, timeout=None)
        string_slice_start = 8
        string_slice_period = 12
        try:
            while True:
                if self.is_on==False:
                    ser.close()
                    break
                while ser.in_waiting:  # 若收到序列資料…
                    data_raw = ser.read_until(b'\r')
                    data = data_raw.decode()  # 用預設的UTF-8解碼
                    equipment_ID = data[:string_slice_start - 1]
                    altered_string = data[string_slice_start:string_slice_start + string_slice_period - 1]
                    altered_int = float(altered_string)
                    # print('接收到的原始資料：', data_raw)
                    # print('接收到的資料：', data)
                    # print('Measurement Data From : ', equipment_ID)
                    # print('Altered Data : ', altered_string)
                    # print('Altered Float : ', altered_int)
                    unit = list(data)
                    # I = ("I")
                    # if unit[-2] == I:
                    #     altered_int = ("%sin" % altered_int)
                    # else:
                    #     altered_int = ("%smm" % altered_int)
                    I = ("I")
                    if unit[-2] == I:
                        altered_unit = ("in" )
                    else:
                        altered_unit = ("mm")
                    a = []
                    a.append(altered_int)
                    a.append(equipment_ID)
                    a.append(altered_unit)
                    ser.close()
                    return a
        except:pass

if __name__ == '__main__' :
    # app = QtWidgets.QApplication(sys.argv)
    # w = TOOLWindow()
    # Form = QtWidgets.QWidget()
    # w.setupUi(Form)
    # w.show()
    # sys.exit(app.exec_())
    # the main window
    app = QtWidgets.QApplication([])
    window = TOOLWindow()
    window.show()
    sys.exit(app.exec_())
