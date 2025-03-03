import tkinter as tk

from core.components.utils import Menubutton


class Tab(Menubutton):
    def __init__(self, master, view, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.view = view
        self.selected = False
        
        self.config(text=view.__class__.__name__, padx=5, pady=5,
            font=("Segoe UI", 10), **self.base.theme.layout.base.content.panel.bar.tab)

        self.bind('<Button-1>', self.select)

    def deselect(self, *_):
        if self.selected:
            self.view.grid_remove()
            self.config(fg=self.base.theme.layout.base.content.panel.bar.tab.foreground)
            self.selected = False
        
    def select(self, *_):
        if not self.selected:
            self.master.set_active_tab(self)
            self.view.grid(column=0, row=1, sticky=tk.NSEW)
            self.config(fg=self.base.theme.layout.base.content.panel.bar.tab.selectedforeground)
            self.selected = True
