import tkinter
import game

FIELD_WIDTH: int = 800
FIELD_HEIGHT: int = 600
CELL_SIZE: int = 20

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Pythonic Snake")

    score_text = tkinter.StringVar(root, "Score: 0")
    root.score_text = score_text
    score_label = tkinter.Label(root, textvariable=score_text)
    score_label.pack(side="top")

    canvas = tkinter.Canvas(root, width=FIELD_WIDTH, height=FIELD_WIDTH, background="#444941")

    canvas.pack()

    canvas.focus_set()  # focus to canvas for keypressing catch

    game = game.Game(canvas, width=FIELD_WIDTH, height=FIELD_HEIGHT, cell_size=CELL_SIZE)

    canvas.bind("<KeyPress>", game.snake.change_direction)
    canvas.bind("<Return>", game.toggle_pause)

    game.main()

    root.mainloop()
