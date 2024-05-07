#!/usr/bin/python

#################
# GUI Interface for the Watch Dog in TKinter

# TO DO:
# Error and exception handling
# Focus
# Actual valid button combs (on + exp + tl only or just on)
# maybe need to be able to identify if already running?
# set minimum sizes (and maximum)
# make check box ticks larger


##################

import tkinter as tk
import subprocess

##################


##################

class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.on = False
        self.state_label_text = "OFF"
        self.title("Watch Dog GUI")
        self.geometry("600x600")
        self.configure(bg='light grey')
        
         ############
        # Main Frame
        self.main_frame = tk.Frame(self, bg='light grey', bd=4)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        
        ############
        # MAIN BUTTON:
        self.button_frame = tk.LabelFrame(self.main_frame, bg='light grey', bd=4)
        # BUTTON
        self.button = tk.Button(self.button_frame, text="Turn On Watchdog", bg="green", fg="white", font=('consolas', 20, "bold"), command=self.toggle_pause, bd=3,relief=tk.RAISED)
        self.button.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        self.button.pack(padx=20, pady=40, fill=tk.BOTH, expand=True)
        
        ############
        # MAIN LABEL:
        self.state_label = tk.Label(self.button_frame, font=('consolas', 16), bg='light grey', fg="blue", bd=3)
        self.state_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.state_label.pack(padx=2, pady=4, fill=tk.BOTH, expand=True)
        self.button_frame.pack(padx=20, pady=25, fill=tk.BOTH, expand=True)
        
        ############
        # LOG MONITOR OPTION:
        self.log_frame = tk.LabelFrame(self, bg='light grey', bd=4, text = "Monitor Log", font=('consolas', 10))
        # CHECK BUTTON:
        self.state_var = tk.IntVar()
        self.check_button = tk.Checkbutton(self.log_frame, text="Log Errors", fg="blue", font=('consolas', 12, "bold"), selectcolor="green", relief=tk.RAISED, command=self.run_script, variable=self.state_var, bd=3)
        self.check_button.flash()
        self.check_button.pack(padx=4, pady=8, side=tk.LEFT, expand=True)
        
        # FILE INPUT
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.log_frame, textvariable=self.entry_var, bd=3)
        self.entry.config(width=8)
        self.entry.pack(padx=4, pady=8, side=tk.LEFT, expand=True)
        self.log_frame.pack(padx=20, pady=20)
        
        #######
        # TELE SELECTION:
        self.tele_frame = tk.LabelFrame(self.log_frame, bg='light grey',borderwidth = 0, highlightthickness = 0)#, bd=4)
        self.check_nn = tk.Checkbutton(self.tele_frame, text="NN", fg="blue", font=('consolas', 12, "bold"), selectcolor="green", relief=tk.RAISED, bd=3)
        self.check_ns = tk.Checkbutton(self.tele_frame, text="NS", fg="blue", font=('consolas', 12, "bold"), selectcolor="green", relief=tk.RAISED, bd=3)
        self.check_nn.pack(padx=10, pady=10, side=tk.TOP, expand=True)
        self.check_ns.pack(padx=10, pady=10, side=tk.TOP, expand=True)
        self.check_nn.flash()
        self.check_ns.flash()
        self.tele_frame.pack(padx=20, pady=20, side=tk.LEFT, expand=True)
        
        ############
        # RELOAD TEXT ELEMENTS
        self.load_text()
        
     
    #####################   
        
    def run_script(self):
        if self.on and self.state_var.get() == 1 and not self.entry_var.get():
             # Flash the entry box
            self.entry.config(bg="pink")
            self.entry.after(500, self.reset_entry_bg)
        else:
            parameter = self.entry_var.get()
           # subprocess.run(['./your_script.sh', parameter])
      
    def reset_entry_bg(self):
        # Reset background color to white
        self.entry.config(bg="white")


    #####################

    def toggle_pause(self):
        self.on = not self.on  # Toggle on/off
        if self.on:
            self.button.config(bg="red", text="Turn Off Watchdog")
            self.state_label_text = "ON"
            # subprocess.run(['./script_off.sh'])
        else:
            self.button.config(bg="green", text="Turn On Watchdog")
            # subprocess.run(['./script_on.sh'])
            self.state_label_text = "OFF"
        
        self.load_text()
       
    
    def load_text(self):
        self.state_label.config(text="Watch Dog is {}".format(self.state_label_text))
    
##################

if __name__ == "__main__":
    
    gui = Window()
    gui.mainloop()
