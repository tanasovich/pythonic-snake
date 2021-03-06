import random
import tkinter.messagebox

from tkinter import Canvas
from tkinter import Event
from snake import Snake
from snake_chunk import SnakeChunk
from apple import Apple


class Game:
    def __init__(self, canvas: Canvas, width: int, height: int, cell_size: int):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.score: int = 0
        self.is_paused: bool = False

        snake_chunks: list = [
            SnakeChunk(cell_size, cell_size, cell_size),
            SnakeChunk(cell_size*2, cell_size, cell_size),
            SnakeChunk(cell_size*3, cell_size, cell_size)
        ]

        self.snake: Snake = Snake(snake_chunks)
        Snake.chunk_cell_size = 20
        self.snake.direction_vector = Snake.directions["Right"]

        self.apple = self.spawn_apple()

    def main(self):
        if self.is_paused:
            return

        self.snake.move()

        if self._is_snake_touch_wall() or self._is_snake_eats_itself():
            self.game_over()
            exit()

        if self._is_snake_eats_apple():
            self.snake.add_chunk()
            self.score += 1
            self.canvas.master.score_text.set(f"Score: {self.score}")
            self.apple = self.spawn_apple()

        self.draw()

        self.canvas.after(150, self.main)

    def game_over(self):
        answer: str = tkinter.messagebox.showerror("Game over!", f"Your score: {self.score}")

        if answer:
            self.canvas.master.destroy()

    def toggle_pause(self, event: Event):
        if not self.is_paused:
            self.is_paused = True
            self.canvas.master.score_text.set("PAUSE")
        else:
            self.is_paused = False
            self.canvas.master.score_text.set(f"Your score: {self.score}")
            self.main()

    def spawn_apple(self) -> Apple:
        while True:
            x = self.cell_size * random.randint(1, (self.width-self.cell_size) // self.cell_size)
            y = self.cell_size * random.randint(1, (self.height-self.cell_size) // self.cell_size)

            if self._is_apple_grown_on_snake(x, y):
                continue
            else:
                return Apple(x, y, self.cell_size)

    def draw(self):
        self.canvas.delete("all")
        self._draw_snake()
        self._draw_apple()

    def _draw_snake(self):
        for chunk in self.snake.snake_chunks:
            self.canvas.create_rectangle(chunk.x1, chunk.y1, chunk.x2, chunk.y2, fill="#7FC8A9", outline="#444941")

    def _draw_apple(self):
        self.canvas.create_oval(self.apple.x1, self.apple.y1, self.apple.x2, self.apple.y2, fill="#D5EEBB", outline="#444941")

    def _is_snake_touch_wall(self) -> bool:
        snake_head: SnakeChunk = self.snake.snake_chunks[-1]

        if snake_head.x2 > self.width or snake_head.x1 < 0 or snake_head.y1 < 0 or snake_head.y2 > self.height:
            return True
        else:
            return False

    def _is_snake_eats_apple(self) -> bool:
        snake_head: SnakeChunk = self.snake.snake_chunks[-1]

        if snake_head.x1 == self.apple.x1 and snake_head.y1 == self.apple.y1:
            return True
        else:
            return False

    def _is_snake_eats_itself(self) -> bool:
        snake_head: SnakeChunk = self.snake.snake_chunks[-1]

        for chunk in self.snake.snake_chunks[:-1]:
            if snake_head.x1 == chunk.x1 and snake_head.y1 == chunk.y1:
                return True
        return False

    def _is_apple_grown_on_snake(self, x: int, y: int) -> bool:
        for chunk in self.snake.snake_chunks:
            if chunk.x1 == x and chunk.y1 == y:
                return True
        return False
