from UIController import UIController
from database_wrapper_class import Database_Wrapper
from SerialHandler import SerialHandler


SCREEN_SCALAR = 1
'''
SCREEN SCALAR LETS YOU CHOOSE HOW BIG THE WINDOW IS WHILE DEVELOPING
    width, height
0 = 800, 480
1 = 1600, 960
2 = 2400, 1440]
'''

SERIAL_ADDRESS = "COM6"

def main():

    d = Database_Wrapper()

    d.create_table_if_not_exists()

    s = SerialHandler()

    s.start_serial_port(SERIAL_ADDRESS)

    c = UIController()

    c.set_screen_size(SCREEN_SCALAR)

    c.showUI()

    c.findgraphs()

if __name__ == '__main__':
    main()
    