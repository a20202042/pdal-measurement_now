import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        self.initUI()
    def initUI(self):
        #设置标题与初始大小
        self.setWindowTitle('QTableWidget例子')
        self.resize(600,800)

        ##水平布局
        layout=QHBoxLayout()
        #实例化表格视图（30*4）
        tablewidget=QTableWidget(30,4)
        layout.addWidget(tablewidget)

        for i in range(30):
            for j in range(4):
                itemContent='(%d,%d)'%(i,j)
                #为每个表格内添加数据
                tablewidget.setItem(i,j,QTableWidgetItem(itemContent))

        self.setLayout(layout)

        #遍历表格查找对应项
        text='(10,1)'
        items=tablewidget.findItems(text,Qt.MatchExactly)
        item=items[0]
        print(str(item))
        #选中单元格
        item.setSelected(True)
        #设置单元格的背脊颜色为红
        item.setForeground(QBrush(QColor(255,0,0)))
        print(tablewidget.currentRow())
        # row=item.row()
        # 通过鼠标滚轮定位，快速定位到第十一行
        # tablewidget.verticalScrollBar().setSliderPosition(10)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    table=Table()
    table.show()
    sys.exit(app.exec_())