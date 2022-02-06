"""
Name: frede
Filename: google forms tab.py
Date: 8/7/20    21
"""
import pyautogui as key
import time
import random

WAITING_TIME = 0.5
NO_OF_TABS = 22
TIME_INTERVAL_BTW = 0.1
# LOWER_LIMIT = random.randint(2, 3)
# UPPER_LIMIT = random.randint(4, 4)
LOWER_LIMIT = 2
UPPER_LIMIT = 4
print("Lower limit: ", LOWER_LIMIT)
print("Upper limit: ", UPPER_LIMIT)

def main():
    time.sleep(WAITING_TIME)
    for _ in range(NO_OF_TABS):
        left_presses = random.randint(LOWER_LIMIT, UPPER_LIMIT) # (start, stop+1)
        key.press('tab')
        # print('tab')
        time.sleep(TIME_INTERVAL_BTW)
        # print(f"pressed left {left_presses}")
        key.press('left', presses=left_presses)


if __name__ == '__main__':
    main()
