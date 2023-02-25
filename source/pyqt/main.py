import sys
from PyQt5.QtWidgets import QApplication

from widgets import App

SCREEN_SCALAR = 2
'''
SCREEN SCALAR LETS YOU CHOOSE HOW BIG THE WINDOW IS WHILE DEVELOPING
    width, height
0 = 800, 480
1 = 1600, 960
2 = 2400, 1440
'''
def main():
    app = QApplication(sys.argv)
    ex = App()
    ex.set_screen_size(SCREEN_SCALAR)
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()