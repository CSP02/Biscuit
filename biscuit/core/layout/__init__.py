import tkinter as tk

from .menubar import Menubar
from .base import BaseFrame
from .statusbar import Statusbar
from core.components.utils import Frame


class Root(Frame):
    """
    Root frame holds Menubar, BaseFrame, and Statusbar
    .
    App
    └── Root
        ├── Menubar
        ├── BaseFrame
        └── StatusBar
    """
    def __init__(self, base, *args, **kwargs):
        super().__init__(base, *args, **kwargs)
        self.config(bg=self.base.theme.border)

        grip_n = tk.Frame(self, bg=self.base.theme.biscuit, cursor='top_side')
        grip_n.bind("<B1-Motion>", lambda e: self.base.resize('n'))
        grip_n.pack(fill=tk.X)

        self.menubar = Menubar(self)
        self.menubar.pack(fill=tk.BOTH)

        self.baseframe = BaseFrame(self)
        self.baseframe.pack(fill=tk.BOTH, expand=True, pady=(1,0))

        self.statusbar = Statusbar(self)
        self.statusbar.pack(fill=tk.X, pady=(1,0))

        grip_s = tk.Frame(self, bg=self.base.theme.biscuit, cursor='bottom_side')
        grip_s.bind("<B1-Motion>", lambda e: self.base.resize('s'))
        grip_s.pack(fill=tk.X)
