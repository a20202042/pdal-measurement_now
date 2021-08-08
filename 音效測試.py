import sys
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.sound = QSound('123.wav')
        self.sound.setLoops(QSound.Infinite)                # 1

        self.play_btn = QPushButton('Play Sound', self)
        self.stop_btn = QPushButton('Stop Sound', self)
        self.play_btn.clicked.connect(self.sound.play)
        self.stop_btn.clicked.connect(self.sound.stop)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.play_btn)
        self.h_layout.addWidget(self.stop_btn)
        self.setLayout(self.h_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())