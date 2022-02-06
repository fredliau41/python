"""
Name: frede
Filename: detect_shut.py
Date: 9/18/2021
"""
import commctrl
import win32api
import win32con
import win32gui
import time
import threading
import os

SHUT_FILE = "shut_down_success.txt"


def msgloop(shut_func, handle):
    while True:
        msg = win32gui.GetMessage(handle, 0, 0)
        print(msg)
        print(msg[1][0])
        # if msg and msg.message == win32con.WM_QUERYENDSESSION:
        #     shut_func()
        win32gui.TranslateMessage(msg[1])
        win32gui.DispatchMessage(msg[1])
        # if msg and msg.message == win32con.WM_QUIT:
        #     return msg.wparam


def handle_shutdown(signal):
    print("triggered")
    print("signal: ", signal)
    with open(SHUT_FILE, 'w') as txt:
        txt.write("shut")

class MyWindow:

    def __init__(self):
        win32gui.InitCommonControls()
        self.hinst = win32api.GetModuleHandle()
        className = 'MyWndClass'
        message_map = {
            win32con.WM_DESTROY: self.OnDestroy,
        }
        wc = win32gui.WNDCLASS()
        wc.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
        wc.lpfnWndProc = message_map
        wc.lpszClassName = className
        win32gui.RegisterClass(wc)
        style = 0
        self.hwnd = win32gui.CreateWindowEx(0,
            className,
            'My win32api app',
            style,
            300,
            300,
            300,
            300,
            0,
            0,
            self.hinst,
            None
        )
        win32gui.UpdateWindow(self.hwnd)
        win32gui.ShowWindow(self.hwnd, win32con.SW_HIDE)

    def OnDestroy(self, hwnd, message, wparam, lparam):
        win32gui.PostQuitMessage(0)
        return True

def main():
    hidden_wind = MyWindow()
    hwnd = hidden_wind.hwnd
    # wc = win32gui.WNDCLASS()
    # wc.lpszClassName = 'test_win32gui_1'
    # wc.style = win32con.CS_GLOBALCLASS | win32con.CS_VREDRAW | win32con.CS_HREDRAW
    # wc.hbrBackground = win32con.COLOR_WINDOW + 1
    # class_atom = win32gui.RegisterClass(wc)
    #
    # integer = win32gui.CreateWindow(wc,
    #                                 "winlog",
    #                                 0,
    #                                 CW_USEDEFAULT,
    #                                 CW_USEDEFAULT,
    #                                 CW_USEDEFAULT,
    #                                 CW_USEDEFAULT,
    #                                 0,
    #                                 0,
    #                                 0,
    #                                 None)
    msgloop(handle_shutdown, hwnd)
    win32gui.PumpMessages()


if __name__ == '__main__':
    main()
