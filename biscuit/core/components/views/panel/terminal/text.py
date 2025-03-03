import tkinter as tk

from core.components.utils import Text


class TerminalText(Text):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.mark_set('input', 'insert')
        self.mark_gravity('input', 'left')

        self.config(**self.base.theme.views.panel.terminal)

        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)
        
    def _proxy(self, *args):
        largs = list(args)

        if args[0] == 'insert':
            if self.compare('insert', '<', 'input'):
                self.mark_set('insert', 'end')
        elif args[0] == "delete":
            if self.compare(largs[1], '<', 'input'):
                if len(largs) == 2:
                    return
                largs[1] = 'input'
        result = self.tk.call((self._orig,) + tuple(largs))
        return result
