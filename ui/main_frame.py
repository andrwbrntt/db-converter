# interface library
import ttkbootstrap as tb
from ui.labels import H1Label, H6Label
from ui.buttons import Button

class MainFrame():
    def __init__(self):
        self.root = tb.Window(themename = "darkly")
        self.root.title("Quick DB")
        width, height = 600, 400
        # center window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

        welcome_label = H1Label(self.root, "Welcome")
        welcome_label.pack(pady = (50, 0))
        
        choose_label = H6Label(self.root, "Choose file type")
        choose_label.pack()

        csv_button = Button(self.root, text = "csv")
        csv_button.pack(pady = (50, 0))

        excel_button = Button(self.root, "xlsx")
        excel_button.pack(pady = (25, 0))

    def run(self):
        self.root.mainloop()