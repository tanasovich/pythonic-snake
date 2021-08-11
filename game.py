from tkinter import Tk
from snake import Snake
from snake_chunk import SnakeChunk


class Game:
    def __init__(self, root: Tk, width: int, height: int, cell_size: int):
        self.root = root
        self.width = width
        self.height = height

        snake_chunks: list = [
            SnakeChunk(cell_size, cell_size, cell_size),
            SnakeChunk(cell_size*2, cell_size, cell_size),
            SnakeChunk(cell_size*3, cell_size, cell_size)
        ]

        self.snake: Snake = Snake(snake_chunks)
        Snake.chunk_cell_size = 20
        self.snake.direction_vector = Snake.directions["Right"]

    def main(self):
        self.snake.move()

        if self._is_snake_touch_wall():
            self.game_over()

    def _is_snake_touch_wall(self):
        snake_head: SnakeChunk = self.snake.snake_chunks[-1]

        if snake_head.x2 > self.width or snake_head.x1 < 0 or snake_head.y1 < 0 or snake_head.y2 > self.height:
            return True
        else:
            return False

    def game_over(self):
        pass
