import gui, sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = gui.Example()

    sys.exit(app.exec_())