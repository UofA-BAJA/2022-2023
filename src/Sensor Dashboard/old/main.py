from UIController import UIController
from database_wrapper_class import Database_Wrapper
from serial.port import Port

SCREEN_SCALAR = 2
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

    s = Port(SERIAL_ADDRESS)

    c = UIController()

    c.setSerial(s)

    s.setUIController(c)

    c.set_screen_size(SCREEN_SCALAR)

    c.showUI()

    c.findgraphs()

if __name__ == '__main__':
    main()
    