from tkinter import Event
from snake_chunk import SnakeChunk


class Snake:
    directions: dict = {"Left": (-1, 0), "Up": (0, -1), "Right": (1, 0), "Down": (0, 1)}
    chunk_cell_size = int()

    def __init__(self, snake_chunks: list[SnakeChunk]):
        self.snake_chunks: list = snake_chunks
        self.direction_vector = Snake.directions["Right"]

    def move(self):
        for index in range(len(self.snake_chunks) - 1):
            self.snake_chunks[index] = self.snake_chunks[index + 1]

        old_head: SnakeChunk = self.snake_chunks[-2]
        self.snake_chunks[-1] = SnakeChunk(old_head.x1 + self.direction_vector[0],
                                           old_head.y1 + self.direction_vector[1],
                                           Snake.chunk_cell_size)

    def change_direction(self, event: Event):
        if event.keysym in Snake.directions:
            if map(sum, zip(self.direction_vector, Snake.directions[event.keysym])) == [0, 0]:
                return
            else:
                self.direction_vector = Snake.directions[event.keysym]

    def add_chunk(self):
        tail = self.snake_chunks[0]
        x = tail[2] - Snake.chunk_cell_size
        y = tail[3] - Snake.chunk_cell_size
        self.snake_chunks.insert(0, (x, y, x + Snake.chunk_cell_size, y + Snake.chunk_cell_size))
