# interface library
import ttkbootstrap as tb
from ui.labels import H1Label, H6Label
from ui.buttons import Button

class MainFrame(tb.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand = True)

        welcome_label = H1Label(self, "Welcome")
        welcome_label.pack(pady = (50, 0))
        
        choose_label = H6Label(self, "Select a file to convert")
        choose_label.pack()

        file_button = Button(self, "Choose file", command = self.file_click)
        file_button.pack(pady = (75, 0))

    def file_click(self):
        pass