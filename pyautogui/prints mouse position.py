"""
Name: frede
Filename: prints mouse position.py
Date: 8/15/2021
"""
import pyautogui
import time


def rec():
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            time.sleep(0.2)
            print('\b' * len(positionStr), end='', flush=True)

    except KeyboardInterrupt:
        print('\n')


MODE = rec

def main():
    MODE


if __name__ == '__main__':
    main()
