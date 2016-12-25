import sys, time
from threading import Timer
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QLCDNumber,
                             QTextEdit, QPushButton, QGridLayout, QApplication)

timeList = [str(10), str(20)]

class pomodoroTimer():
    def __init__(self, setTime):
        self.isOn = False
        self.setTime = setTime
        self.startTime = 0
        self.currentTime = 0
        self.pauseTime = 0
        self.minutes = 0
        self.seconds = 0

    def tickTock(self):
        global timeList
        self.currentTime = time.time() - (self.startTime - self.pauseTime)
        print(self.currentTime)
        if self.currentTime <= self.setTime and self.isOn is True:
            timer = Timer(1.0, self.tickTock)
            self.seconds += 1
            if self.seconds >= 60:
                self.seconds = 0
                self.minutes += 1
            timer.start()
        elif self.currentTime > self.setTime:
            self.currentTime = 0
        timeList[0] = str(self.minutes)
        timeList[1] = str(self.seconds)
        print(timeList)

    def startTimer(self):
        if self.isOn is False:
            self.isOn = True
            self.tickTock()

    def pauseTimer(self):
        if self.isOn is True:
            self.isOn = False
            self.pauseTime = self.currentTime
            print('Paused at:', self.pauseTime, '.')

    def finishTimer(self):
        if self.isOn is True:
            self.isOn = False


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'Pomidorix'
        self.initUI()
        self.setTime = 10
        self.myTimer = pomodoroTimer(self.setTime)
        self.lcdClock

    def initUI(self):
        self.setWindowTitle(self.title)

        title = QLabel('Pomodoro timer')
        self.lcdClock = QLCDNumber()
        self.updateTimeList()

        buttonStart = QPushButton('Start', self)
        buttonStart.clicked.connect(self.start_on_click)
        buttonPause = QPushButton('Pause', self)
        buttonPause.clicked.connect(self.pause_on_click)
        buttonEnd = QPushButton('End', self)
        buttonEnd.clicked.connect(self.end_on_click)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.lcdClock, 0, 1)
        grid.addWidget(buttonStart, 1, 0)
        grid.addWidget(buttonPause, 1, 1)
        grid.addWidget(buttonEnd, 1, 2)

        self.setLayout(grid)

        self.setGeometry(300, 300, 300, 100)

        self.show()

    def updateTimeList(self):
        global timeList
        s = ':'
        displayTime = s.join(timeList)
        self.lcdClock.display(displayTime)
        timer = Timer(0.5, self.updateTimeList)
        timer.start()


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