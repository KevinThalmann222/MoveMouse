"""
Nutze dieses Tool um nie mehr im Skype oder Teams inaktiv zu werden.
"""
import threading
import pyautogui
import random
import time
from datetime import datetime
import tkinter as tk
from tkinter import font


class MoveingMouse:
    def __init__(self) -> None:
        """Init"""
        self.run = True
        self.screen_width, self.screen_height = pyautogui.size()
        self.pad_x = 0
        self.pad_y = 5
        self.root = tk.Tk()
        self.root.title("MoveingMouse")
        self.backgroundColor = "white"
        self.lable = tk.Label(self.root, background=self.backgroundColor)

    def start(self) -> None:
        """run init"""
        font_headline = font.Font(size=30, weight="bold", family="Roboto")
        font_standard = font.Font(size=14, family="Roboto")
        headline = tk.Label(
            self.lable,
            text="MoveMouse",
            font=font_headline,
            background=self.backgroundColor,
            foreground="#6F6F6F",
            width=20,
        )
        time = tk.Label(
            self.lable,
            font=font_standard,
            text="Endtime e.g. 16:30:00",
            background=self.backgroundColor,
            foreground="#6F6F6F",
        )
        self.input_time = tk.Text(
            self.lable,
            height=1.3,
        )
        start_button = tk.Button(
            self.lable,
            text="Start",
            font=font_standard,
            background="#fcba03",
            command=self.auto_click,
        )
        end_button = tk.Button(
            self.lable,
            text="End",
            font=font_standard,
            background="#fcba03",
            command=self.quit_programm,
        )
        self.lable.grid(
            padx=self.pad_x,
            pady=self.pad_y,
        )
        headline.grid(
            column=0,
            row=0,
            sticky=tk.EW,
            padx=self.pad_x,
            pady=self.pad_y,
        )
        time.grid(
            column=0,
            row=1,
            sticky=tk.EW,
            padx=self.pad_x,
            pady=self.pad_y,
        )
        self.input_time.grid(
            column=0,
            row=2,
            sticky=tk.EW,
            padx=self.pad_x,
            pady=self.pad_y,
        )
        start_button.grid(
            column=0,
            row=3,
            sticky=tk.EW,
            padx=self.pad_x,
            pady=self.pad_y,
        )
        end_button.grid(
            column=0,
            row=4,
            sticky=tk.EW,
            padx=self.pad_x,
            pady=self.pad_y,
        )
        self.root.mainloop()

    def print_input(self):
        inp = self.input_time.get(1.0, "end-1c")
        return inp

    def quit_programm(self):
        quit = threading.Thread(target=self.quit_programm)
        quit.start()

    def stop_moving(self):
        self.run = False
        quit()

    def auto_click(self) -> None:
        self.move = threading.Thread(target=self.starting)
        self.move.start()

    def starting(self, end_time=None) -> None:
        """Move and click the mouse automatic"""
        end_time = self.print_input()
        time.sleep(10)
        x_start = self.screen_width / 2
        y_start = self.screen_height / 2
        pyautogui.moveTo(x_start, y_start)
        while self.run:
            date_time = datetime.now()
            current_time = date_time.strftime("%H:%M:%S")
            if end_time and current_time >= end_time:
                print(f"Script ends at {current_time}")
                break
            cur_mouse_x, cur_mouse_y = pyautogui.position()
            if cur_mouse_x >= self.screen_width * 0.8 or cur_mouse_x < 100:
                x_start = self.screen_width / 2
                y_start = self.screen_height / 2
            if cur_mouse_y >= self.screen_height * 0.8 or cur_mouse_y < 100:
                x_start = self.screen_width / 2
                y_start = self.screen_height / 2
            pyautogui.moveTo(x_start, y_start)
            x_start += random.randint(-200, 200)
            y_start += random.randint(-200, 200)
            pyautogui.click()
            time.sleep(5)


if __name__ == "__main__":
    mouse = MoveingMouse()
    mouse.start()
