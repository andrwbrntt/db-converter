import ttkbootstrap as tb

class H1Label(tb.Label):
    def __init__(self, root, text):
        super().__init__(
            root, 
            text = text, 
            bootstyle = "success",
            font = ("Helvetica", 28, "bold")
            )

class H6Label(tb.Label):
    def __init__(self, root, text):
        super().__init__(
            root, 
            text = text,
            font  = ("Helvetica", 10)
            )
