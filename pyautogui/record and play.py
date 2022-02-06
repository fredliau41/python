"""
Name: frede
Filename: record and play.py
Date: 8/15/2021
"""
import threading

import pyautogui
import time
from pynput.mouse import Button, Controller, Listener
import pynput.keyboard as keyb
import os
import sys

RESOLUTION = 0.1
SPEED = 1.5
EXECUTE_RES = RESOLUTION / SPEED
END_PROCESS_CLICK_OFFSET = -11


def rec(temp=None):
    """ Records mouse movement and clicks into string delimited by , <996:775,Left_click,996:775> """
    global string
    string = ""

    def on_click(x, y, button, pressed):
        """ record pressed clicks """
        global string
        if button == Button.left and pressed:
            print("Left_click", end=",")
            string += "Left_click,"
        if button == Button.left and not pressed:
            print("Left_rel", end=",")
            string += "Left_rel,"

    listener = Listener(on_click=on_click)
    listener.start()

    # record mouse position
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = f"{x}:{y}"
            print(positionStr, end=",")
            string += positionStr + ","
            time.sleep(RESOLUTION)

    except KeyboardInterrupt:
        print('\n')

    # saves it into backup and recorded file
    finally:
        if not os.path.isfile("backup.txt"):
            with open("backup.txt", 'w') as create:
                None

        with open("recorded.txt", 'w') as rec:
            rec.write(string)
        with open("backup.txt", 'r+') as backup:
            data = backup.readlines()
            num = 1 + len(data)
            backup.write(backup.read() + f"{num} ." + string + '\n')


def execute(num=1):
    """ Executes recorded movements in recorded.txt, num is times we repeat the recorded set """
    try:

        def move():

            for _ in range(num):
                with open("recorded.txt", 'r') as rec:
                    string = rec.read()
                    lst = string.split(',')[:END_PROCESS_CLICK_OFFSET]

                    for obj in lst:
                        global stop
                        stop = False

                        def on_press(key):
                            global stop
                            if str(key) == r"'\x03'":
                                print('captured')
                                stop = not stop

                        key_listen = keyb.Listener(on_press=on_press)
                        key_listen.start()
                        time.sleep(EXECUTE_RES)
                        key_listen.stop()
                        if stop:
                            break
                        if obj[0].isdigit():
                            x, y = tuple(obj.split(":"))
                            Controller().position = (int(x), int(y))
                        if obj == "Left_click":
                            Controller().press(Button.left)
                        if obj == "Left_rel":
                            Controller().release(Button.left)

        move()

    except KeyboardInterrupt:
        print('Keyboard interrupted')
    finally:
        print("process ended")


MODE = execute


def main():
    # if execute, it takes 1 integer into its parameter; defines loops
    MODE(1)


if __name__ == '__main__':
    main()
