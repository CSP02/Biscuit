import tkinter as tk

from .slot import Slot
from .item import MenuItem

from core.components.utils import Frame


class Slots(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.config(width=150, **self.base.theme.layout.base.sidebar.slots)

        self.slots = []
        self.active_slot = None

        self.menus = []
        self.add_menus()
        
    # --- SLOTS ---
    def add_slot(self, view):
        slot = Slot(self, view)
        slot.pack(fill=tk.Y)
        self.slots.append(slot)
    
    def toggle_first_slot(self):
        self.slots[0].toggle()
    
    def set_active_slot(self, selected_slot):
        self.active_slot = selected_slot
        for slot in self.slots:
            if slot != selected_slot:
                slot.disable()

    # --- MENUS ---
    def add_menus(self):
        self.add_settings_menu()
    
    def add_settings_menu(self):
        file_menu = self.add_menu("settings-gear", "manage")
        file_menu.add_item("Command Palette", lambda *_: self.base.palette.show_prompt(">"))
        file_menu.add_separator()
        file_menu.add_item("Settings", self.base.open_settings)

    def add_menu(self, icon, text):
        new_menu = MenuItem(self, icon, text)
        new_menu.pack(side=tk.BOTTOM, fill=tk.X, padx=0)
        self.menus.append(new_menu.menu)
        
        return new_menu.menu

    def close_all_menus(self, *_):
        for menu in self.menus:
            menu.hide()

    def switch_menu(self, menu):
        active = False
        for i in self.menus:
            if i.active:
                active = True
            if i != menu:
                i.hide()
        
        if active:
            menu.show()
