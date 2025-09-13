import ttkbootstrap as tb
from ui.buttons import Button
import tksheet

class DisplayFrame(tb.Frame):
    def __init__(self, parent, df):
        super().__init__(parent)
        self.pack(fill = "both", expand = True)
        self.df = df

        preview_frame = tb.Frame(self, borderwidth = 2, relief = "solid")
        preview_frame.pack(fill = "both", expand = True, padx = 25, pady = (25,0))

        preview = tksheet.Sheet(preview_frame)
        preview.pack(fill = "both", expand = True)
        preview.headers(df.columns.tolist())
        preview.set_sheet_data(df.values.tolist())
        preview.set_options(
            table_fg = "white",
            table_selected_cells_fg = "white",
            header_fg = "white",
            index_fg = "white"
        )
        preview.redraw()

        button_frame = tb.Frame(self)
        button_frame.pack(fill = "both", expand = True)

        cancel_button = Button(button_frame, text = "Cancel", command = self.cancel_click)
        cancel_button.pack(side = "left", padx = 25)
        confirm_button = Button(button_frame, text = "Confirm")
        confirm_button.pack(side = "right", padx = 25)

    def cancel_click(self):
        self.pack_forget()
        from ui.main_frame import MainFrame
        from main import initial_window
        main_frame = MainFrame(self.master)
        main_frame.pack(fill = "both", expand = True)
        self.master.update_idletasks()
        self.master.geometry(initial_window)
