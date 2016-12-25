import time
from threading import Timer

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
        self.currentTime = time.time() - (self.startTime - self.pauseTime)
        print(self.currentTime)
        if self.currentTime <= self.setTime and self.isOn == True:
            timer = Timer(1.0, self.tickTock)
            self.seconds += 1
            if self.seconds >= 60:
                self.seconds = 0
                self.minutes += 1
            timer.start()

    def startTimer(self):
        if self.isOn == False:
            self.isOn = True
            self.tickTock()

    def pauseTimer(self):
        if self.isOn == True:
            self.isOn = False
            self.pauseTime = self.currentTime
            print('Paused at:', self.pauseTime, '.')

    def finishTimer(self):
        if self.isOn == True:
            self.isOn = False

if __name__ == '__main__':
    timeList = [0,0]
    t = pomodoroTimer(10)
    t.startTime = time.time()
    t.startTimer()
