from core import Menu


class ActionbarMenu(Menu):
    def get_coords(self):
        return (self.master.winfo_rootx() + self.master.winfo_width(), 
            self.master.winfo_rooty() + self.master.winfo_height() - self.winfo_height())
