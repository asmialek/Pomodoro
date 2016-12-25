import sys, time
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QLCDNumber,
                             QTextEdit, QPushButton, QGridLayout, QApplication)
from PyQt5.QtCore import pyqtSlot

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'Pomidorix'
        self.initUI()
        self.setTime = 10
        self.myTimer = timer.pomodoroTimer(self.setTime)
        self.timeList = ''

    def initUI(self):
        self.setWindowTitle(self.title)

        s = ':'
        self.timeList = [str(10), str(20)]
        displayTime = s.join(self.timeList)

        title = QLabel('Pomodoro timer')
        lcdClock = QLCDNumber()
        lcdClock.display(displayTime)
        buttonStart = QPushButton('Start', self)
        buttonStart.clicked.connect(self.start_on_click)
        buttonPause = QPushButton('Pause', self)
        buttonPause.clicked.connect(self.pause_on_click)
        buttonEnd = QPushButton('End', self)
        buttonEnd.clicked.connect(self.end_on_click)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(lcdClock, 0, 1)
        grid.addWidget(buttonStart, 1, 0)
        grid.addWidget(buttonPause, 1, 1)
        grid.addWidget(buttonEnd, 1, 2)

        self.setLayout(grid)

        self.setGeometry(300, 300, 300, 100)

        self.show()

    @pyqtSlot()
    def start_on_click(self):
        if self.myTimer.isOn == False:
            self.myTimer.startTime = time.time()
            self.myTimer.startTimer()
            print('Started!')
    def pause_on_click(self):
        self.myTimer.pauseTimer()
        print('Paused.')
    def end_on_click(self):
        self.myTimer.finishTimer()
        print('Finished!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())