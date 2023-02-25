from controller import UIController
SCREEN_SCALAR = 2
'''
SCREEN SCALAR LETS YOU CHOOSE HOW BIG THE WINDOW IS WHILE DEVELOPING
    width, height
0 = 800, 480
1 = 1600, 960
2 = 2400, 1440]
'''
def main():
    c = UIController()

    c.set_screen_size(SCREEN_SCALAR)

    c.showUI()

    c.findgraphs()

if __name__ == '__main__':
    main()