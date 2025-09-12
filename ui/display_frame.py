import ttkbootstrap as tb
from tkinter import ttk
from ui.buttons import Button

class DisplayFrame(tb.Frame):
    def __init__(self, parent, df):
        super().__init__(parent)
        self.pack(fill = "both", expand = True)
        self.df = df

        preview_frame = tb.Frame(self)
        preview_frame.pack(fill = "both", expand = True)

        # build a treeview
        preview = ttk.Treeview(preview_frame)
        preview.grid(row = 0, column = 0, sticky = "nsew")

        # grid ends up being better for scrollbars than pack
        v_scroll = ttk.Scrollbar(preview_frame, orient = "vertical", command = preview.yview)
        v_scroll.grid(row = 0, column = 1, sticky = "ns")
        preview.configure(yscrollcommand = v_scroll.set)

        h_scroll = ttk.Scrollbar(preview_frame, orient = "horizontal", command = preview.xview)
        h_scroll.grid(row = 1, column = 0, sticky = "ew")
        preview.configure(xscrollcommand = h_scroll.set)

        preview_frame.grid_rowconfigure(0, weight = 1)
        preview_frame.grid_columnconfigure(0, weight = 1)

        preview["columns"] = list(self.df.columns)
        preview["show"] = "headings"

        for col in self.df.columns:
            preview.heading(col, text = col)
            preview.column(col, anchor = "center")
        
        for _, row in self.df.iterrows():
            preview.insert("", "end", values = list(row))
        
        
        button_frame = tb.Frame(self)
        button_frame.pack(fill = "x")

        confirm_button = Button(button_frame, text = "Confirm")
        confirm_button.pack(side = "right", pady = 10, padx = 10)

        cancel_button = Button(button_frame, text = "Cancel")
        cancel_button.pack(side = "left", pady = 10, padx = 10)