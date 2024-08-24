import subprocess

import tkinter as tk
from tkinter import messagebox
from tkinter import font

import logging


class Column:

    def __init__(self, parent, row=0, col=0, label=""):
        self.frame = tk.Frame(parent.main_frame, bg=parent.colour_bg, bd=5, highlightbackground="black",
                              highlightthickness=1)
        self.frame.grid(row=row, column=col, sticky="nsew")
        if label:
            tk.Label(self.frame, text=label, width=10, height=2, borderwidth=3, relief="solid").grid(pady=20)


class InputBox:

    def __init__(self, parent, row=0, col=0,label="test"):
        self.frame = tk.Frame(parent.frame, bg="lightcoral", height=100)
        self.frame.grid(row=row, column=col, sticky="nsew", pady=(10, 5))  # Space above and below
        tk.Label(self.frame, text=label).grid(pady=20)

class Window(tk.Tk):

    def __init__(self):
        """On create we...."""
        #
        super().__init__()
        #
        self.colour_bg = None
        self.popup = None
        self.font = None
        #
        self.main_frame = tk.Frame(self)
        self.set_fonts()
        self.initialise()

    def initialise(self):

        self.title("UDP GUI")
        self.geometry("750x600")
        self.minsize(500, 350)
        self.colour_bg = 'light grey'
        self.configure(bg=self.colour_bg, bd=10, highlightbackground="black", highlightthickness=1)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.set_frames()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def set_frames(self):

        try:
            self.set_columns()
        except Exception as e:
            self.show_message("Error starting GUI: \n %s" % e)
            self.destroy()



    def set_columns(self):

        left_column = Column(self, 0, 0)
        center_column = Column(self, 0, 1, "sent")
        right_column = Column(self, 0, 2, "received")

        info_box = InputBox(left_column, 0, 0, "info")
        config_box = InputBox(left_column, 1, 0, "config")
        command_box = InputBox(left_column, 2, 0, "command")

        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        # Configure grid row weights within the left column to manage box spacing
        left_column.frame.grid_rowconfigure(0, weight=1)
        left_column.frame.grid_rowconfigure(1, weight=1)
        left_column.frame.grid_rowconfigure(2, weight=1)


    def show_message(self, message):
        self.popup = tk.messagebox.showerror(title="Error", message=message)
        self.focus_set()

    def set_fonts(self):
        self.font = font.nametofont("TkDefaultFont")


def start_gui():
    udp_gui = Window()
    udp_gui.mainloop()


if __name__ == "__main__":
    start_gui()
