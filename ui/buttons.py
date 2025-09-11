from tkinter import ttk
import ttkbootstrap as tb

class Button(tb.Button):
    def __init__(self, root, text, **kwargs):
        super().__init__(
            root,
            text = text, 
            bootstyle = "success",
            padding = (50, 10),
            **kwargs
            )