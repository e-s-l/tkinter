import queue

import logging
import signal

import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk, VERTICAL, HORIZONTAL, N, S, E, W

from borrowed import ConsoleUi, Clock, QueueHandler


class TestUi:

    def __init__(self, frame):
        self.frame = frame
        ttk.Label(self.frame, text='nada').grid(column=0, row=1, sticky=W)
        ttk.Label(self.frame, text='nada').grid(column=0, row=4, sticky=W)
        ttk.Label(self.frame, text='nada').grid(column=0, row=7, sticky=W)


class ConfigUi:

    def __init__(self, frame):
        self.frame = frame
        ttk.Label(self.frame, text='nada').grid(column=0, row=1, sticky=W)


class CommandUi:

    def __init__(self, frame):
        self.frame = frame
        ttk.Label(self.frame, text='nada').grid(column=0, row=1, sticky=W)




class App:

    def __init__(self, root):
        self.receivedConsoleUi = None
        self.sentConsoleUi = None
        self.commandUi = None
        self.configUi = None
        self.test = None
        self.root = root
        #
        root.title('HSU UDP')
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.geometry("750x600")
        root.minsize(500, 350)
        #
        self.colour_bg = 'light grey'
        #
        self.create_panes()
        # clock for testing
        self.clock = Clock()
        self.clock.start()
        # kill the program
        self.root.protocol('WM_DELETE_WINDOW', self.quit)
        self.root.bind('<Control-q>', self.quit)
        signal.signal(signal.SIGINT, self.quit)

    def create_panes(self):
        #
        vertical_pane = ttk.PanedWindow(self.root, orient=VERTICAL)
        vertical_pane.grid(row=0, column=0, sticky="nsew")
        #
        top_frame = ttk.Frame(vertical_pane)
        vertical_pane.add(top_frame, weight=1)
        #
        self.test = TestUi(top_frame)

        #
        main_pane = ttk.PanedWindow(vertical_pane, orient=HORIZONTAL)
        vertical_pane.add(main_pane, weight=4)

        left_frame = ttk.PanedWindow(vertical_pane, orient=VERTICAL)
        config_frame = ttk.Labelframe(left_frame, text="Configuration")
        command_frame = ttk.Labelframe(left_frame, text="Command")
        left_frame.add(config_frame, weight=1)
        left_frame.add(command_frame, weight=1)
        #
        self.configUi = ConfigUi(config_frame)
        self.commandUi = CommandUi(command_frame)
        #
        middle_frame = ttk.Frame(main_pane, padding=10)
        right_frame = ttk.Frame(main_pane, padding=10)
        #
        main_pane.add(left_frame, weight=1)
        main_pane.add(middle_frame, weight=1)
        main_pane.add(right_frame, weight=1)
        #
        ttk.Label(middle_frame, text="Column 2").pack(pady=10, padx=10, fill='x')
        ttk.Label(right_frame, text="Column 3").pack(pady=10, padx=10, fill='x')
        #
        self.sentConsoleUi = ConsoleUi(middle_frame)
        self.receivedConsoleUi = ConsoleUi(right_frame)
        #
        bottom_frame = ttk.Labelframe(vertical_pane)
        vertical_pane.add(bottom_frame, weight=1)
        #
        self.test = TestUi(bottom_frame)

    def quit(self, *args):
        self.clock.stop()
        self.root.destroy()
