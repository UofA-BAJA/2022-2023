
from UIController import UIController
from database_wrapper_class import Database_Wrapper
from serial.port import Port
from widgets.mainwidgets import setupApp, showapp

SCREEN_SCALAR = 0
'''
SCREEN SCALAR LETS YOU CHOOSE HOW BIG THE WINDOW IS WHILE DEVELOPING
    width, height
0 = 800, 480
1 = 1600, 960
2 = 2400, 1440]
'''

SERIAL_ADDRESS = "COM18"

def main():

    d = Database_Wrapper()

    d.create_table_if_not_exists()

    # s = Port(SERIAL_ADDRESS)

    # c = UIController()

    # c.setSerial(s)

    # s.setUIController(c)

    # c.set_screen_size(SCREEN_SCALAR)

    # c.showUI()

    # c.findgraphs()
    
    ex, app = setupApp()

    #ex.setupSerial(SERIAL_ADDRESS)

    showapp(ex, app)


if __name__ == '__main__':
    main()
    