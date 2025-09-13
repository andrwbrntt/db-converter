import ttkbootstrap as tb
from ui.main_frame import MainFrame

# global var for initial window size
initial_width = 450
initial_height = 325
initial_window = f"{initial_width}x{initial_height}"

def main():
    root = tb.Window(themename = "darkly")
    root.title("Quick DB")
    width, height = 450, 325
    # center window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (initial_width // 2)
    y = (screen_height // 2) - (initial_height // 2)
    root.geometry(f'{initial_window}+{x}+{y}')

    main_frame = MainFrame(root)
    root.mainloop()

if __name__=="__main__":
    main()