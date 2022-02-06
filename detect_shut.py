"""
Name: frede
Filename: detect_shut.py
Date: 9/18/2021
"""
import win32api
from win32con import *
import time
import threading
import os

SHUT_FILE = "shut_down_success.txt"

def shut_handler(func):
    result = win32api.SetConsoleCtrlHandler(func, True)
    print(result)
    return result


def detect_shut(signal):
    print("triggered")
    print("signal", signal)
    if signal == CTRL_SHUTDOWN_EVENT:
        with open(SHUT_FILE , 'w') as txt:
            txt.write("shut")


def main():
    if os.path.isfile(SHUT_FILE):
        os.remove(SHUT_FILE )
    shut_handler(detect_shut)



if __name__ == '__main__':
    main()
