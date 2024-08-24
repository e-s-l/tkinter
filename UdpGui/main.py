
import logging

import tkinter as tk

from classes import App

#
logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)
    root = tk.Tk()
    app = App(root)
    app.root.mainloop()


if __name__ == '__main__':
    main()
