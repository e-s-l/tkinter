import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter import font

import logging

logfilename = "/var/log/test.log"
# Create logger
logger = logging.getLogger(__name__)
logfmt = logging.Formatter("%(asctime)s %(message)s", "%Y-%m-%d %H:%M:%S")

#logfile_handler = logging.FileHandler(logfilename)
#logfile_handler.setFormatter(logfmt)
#logger.addHandler(logfile_handler)

logger.setLevel(logging.DEBUG)

class Column1:

    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(parent, bg='light grey', bd=5)
        self.frame.pack(side="left", fill=tk.Y)
        tk.Label(self.frame, text="LEFT").pack(pady=20)

class Column2:

    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(parent, bg='light grey', bd=5)
        self.frame.pack(side="left", fill=tk.BOTH)
        tk.Label(self.frame, text="MIDDLE").pack(pady=20)


class Column3:

    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(parent, bg='light grey', bd=5)
        self.frame.pack(side="left",fill=tk.Y)
        tk.Label(self.frame, text="RIGHT").pack(pady=20)

############3

class ConfigFrame:

    def __init__(self, parent):
        self.parent = parent
        self.config_frame = tk.Frame(parent, bg='light grey', bd=5)
        self.config_frame.pack(fill=tk.BOTH, expand=True)



class CommandFrame:


    def __init__(self, parent):
        self.parent = parent

class InfoFrame:

    def __init__(self, parent):
        self.parent = parent


class WatchDogFrame:
    # the button and text and container components
    def __init__(self, parent):
        self.parent = parent
        self.state_label = None
        self.button = None
        self.button_frame = None
        self.state_label_text = None
        self.on = None
        self.turn_on_msg = "Turn On Watchdog"
        self.turn_off_msg = "Turn Off Watchdog"
        #
        self.get_watchdog_state()
        self.watchdog_frame = tk.Frame(parent, bg='light grey', bd=5)
        self.make_watchdog_button()
        self.watchdog_frame.pack(fill=tk.BOTH, expand=True)


    def get_watchdog_state(self):
        # COME BACK TO THIS....
        self.on = False  # Watchdog State
        self.state_label_text = "OFF"

    def make_watchdog_button(self):

        # CONTAINER:
        self.button_frame = tk.LabelFrame(self.watchdog_frame, bg='light grey', bd=5,
                                          highlightbackground="#6c6c6c")
        self.button_frame.pack(padx=20, pady=25, fill=tk.BOTH, expand=True)
        # BUTTON:
        self.button = tk.Button(self.button_frame, text=self.turn_on_msg, bg="#394dcd", fg="white",  # "#008080"
                                font=(self.parent.font, 24, "bold"), command=self.toggle_state, bd=6, relief=tk.RAISED,
                                activebackground="#008080")
        self.button.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        self.button.pack(padx=20, pady=40, fill=tk.BOTH, expand=True)
        # LABEL:
        self.state_label = tk.Label(self.button_frame, font=(self.parent.font, 18), bg='light grey', fg="#000080", bd=5)
        self.state_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.state_label.pack(padx=2, pady=4, fill=tk.BOTH, expand=True)
        self.load_text()

    def toggle_state(self):
        # what happens when the button is pressed
        try:
            self.on = not self.on  # Toggle on/off
            if self.on:
                self.button.config(bg="#e52e2e", text=self.turn_off_msg)
                self.state_label_text = "ON "
                self.parent.run_script('watchdog_on')
            else:
                self.button.config(bg="#394dcd", text=self.turn_off_msg)
                self.state_label_text = "OFF"
                self.parent.run_script('watchdog_off')
            self.load_text()
        except Exception as e:
            self.parent.show_message("Error Toggling States: \n %s" % e)

    def load_text(self):
        self.state_label.config(text="Watch Dog is %s" % self.state_label_text)


class Window(tk.Tk):
    # the window that holds the component frames
    def __init__(self):

        super().__init__()
        self.column1 = None
        self.column2 = None
        self.column3 = None
        self.popup = None
        self.title("UDP GUI")
        self.geometry("750x600")
        self.minsize(500, 350)
        self.configure(bg='light grey')
        self.set_fonts()
     #   self.bind_all("<Button-1>", self.focus_set())

        self.set_frames()

    def set_frames(self):
        try:
            print('setting frames')
            self.column1 = Column1(self)
            self.column2 = Column2(self)
            self.column3 = Column3(self)
        except Exception as e:
            self.show_message("Error starting GUI: \n %s" % e)
            self.destroy()

    def show_message(self, message):
        self.popup = tk.messagebox.showerror(title="Error", message=message)
        self.focus_set()


    def run_script(self, script):
        try:
            subprocess.run([script])
        except Exception as e:
            self.show_message("Error running script: \n %s" % e)

    def set_fonts(self):
        self.font = font.Font(family='Helvetica', size=12, weight='bold')

        if self.font not in font.families():
            self.font = 'Arial'

        if self.font not in font.families():
            self.font = font.nametofont("TkDefaultFont")

        print(self.font)


if __name__ == "__main__":
    udp_gui = Window()
    udp_gui.mainloop()
