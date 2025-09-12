import ttkbootstrap as tb
from ui.main_frame import MainFrame

def main():
    root = tb.Window(themename = "darkly")
    root.title("Quick DB")
    width, height = 450, 325
    # center window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

    main_frame = MainFrame(root)
    root.mainloop()

if __name__=="__main__":
    main()