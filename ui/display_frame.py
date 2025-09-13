import ttkbootstrap as tb
from tkinter import filedialog
from ttkbootstrap.dialogs import Messagebox
from ui.buttons import Button
import tksheet
import sqlite3

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
        preview.header_align("w")
        preview.set_sheet_data(df.values.tolist())
        preview.set_options(
            table_bg = "white",
            table_fg = "black",
            table_selected_cells_bg = "#198754",
            table_selected_cells_fg = "white",
            header_bg = "white",
            header_fg = "black",
            index_bg = "white",
            index_fg = "black"
        )
        preview.redraw()

        button_frame = tb.Frame(self)
        button_frame.pack(fill = "both", expand = True)

        cancel_button = Button(button_frame, text = "Cancel", command = self.cancel_click)
        cancel_button.pack(side = "left", padx = 25)
        confirm_button = Button(button_frame, text = "Confirm", command = self.confirm_click)
        confirm_button.pack(side = "right", padx = 25)

    def cancel_click(self):
        self.pack_forget()
        from ui.main_frame import MainFrame
        from main import initial_window
        main_frame = MainFrame(self.master)
        main_frame.pack(fill = "both", expand = True)
        self.master.update_idletasks()
        self.master.geometry(initial_window)

    def confirm_click(self):
        save_path = filedialog.asksaveasfilename(
            parent = self.master,
            title = "Quick DB",
            defaultextension = ".db",
            filetypes = [("SQLite DB","*.db")]
        )
        if save_path:
            conn = sqlite3.connect(save_path)
            self.df.to_sql("data", conn, if_exists = "replace", index = False)
            conn.close()
            Messagebox.show_info(f"File converted successfully!", "Quick DB", parent=self.master)
            self.master.destroy()
