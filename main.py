import tkinter

FIELD_WIDTH: int = 800
FIELD_HEIGHT: int = 600
CELL_SIZE: int = 20

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Pythonic Snake")

    canvas = tkinter.Canvas(root, width=FIELD_WIDTH, height=FIELD_WIDTH, background="blue")

    canvas.grid()

    canvas.focus_set()  # focus to canvas for keypressing catch

    root.mainloop()
