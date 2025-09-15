import ttkbootstrap as tb
from tkinter import filedialog
import pandas as pd
from ui.labels import H1Label, H6Label
from ui.buttons import Button
from ui.display_frame import DisplayFrame


class MainFrame(tb.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand = True)

        welcome_label = H1Label(self, "Welcome")
        welcome_label.pack(pady = (50, 0))
        
        choose_label = H6Label(self, "Select a file to convert")
        choose_label.pack()

        file_button = Button(self, "Choose file", command = self.file_click)
        file_button.pack(pady = (50, 0))

    def file_click(self):
        # hide the main window
        self.master.withdraw()
        file_path = filedialog.askopenfilename(
            parent = self.master,
            title = "Select a file",
            filetypes = [("CSV files", "*.csv"),("Excel files", "*.xlsx: *.xls; *.xlsm; *.xlsb")]
            )
        self.master.deiconify()
        if file_path:
            if file_path.endswith(".csv"):
                self.df = pd.read_csv(file_path)
            elif file_path.endswith(".xlsx", ".xls", ".xlsm", ".xlsb"):
                self.df = pd.read_excel(file_path)
            self.pack_forget()
            display_frame = DisplayFrame(self.master, self.df)
            # resize for display frame
            self.master.update_idletasks()
            self.master.geometry("600x450")
