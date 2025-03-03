import tkinter as tk

from core.components.utils import Shortcut, Frame


class Shortcuts(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.row = 0

    def add_shortcut(self, name, value):
        name = tk.Label(self, text=name, font=("Segoi UI", 10), anchor=tk.E, **self.base.theme.editors.labels)
        value = Shortcut(self, shortcuts=value, **self.base.theme.editors)
        
        name.grid(row=self.row, column=0, sticky=tk.EW, pady=5, padx=5)
        value.grid(row=self.row, column=1, sticky=tk.EW, pady=5, padx=5)

        self.row += 1