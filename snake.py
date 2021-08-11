class Snake:
    directions: dict = {"Left": (-1, 0), "Up": (0, -1), "Right": (1, 0), "Down": (0, 1)}
    chunk_cell_size: int = 0

    def __init__(self, snake_chunks):
        self.snake_chunks = snake_chunks
        self.direction_vector = Snake.directions["Right"]

    def move(self):
        for index in range(len(self.snake_chunks)-1):
            self.snake_chunks[index] = self.snake_chunks[index+1]

        x1, y1, x2, y2 = self.snake_chunks[-2]
        self.snake_chunks[-1] = (x1+self.direction_vector[0]*Snake.chunk_cell_size,
                                 y1+self.direction_vector[1]*Snake.chunk_cell_size,
                                 x2+self.direction_vector[0]*Snake.chunk_cell_size,
                                 y1+self.direction_vector[1]*Snake.chunk_cell_size)

    def change_direction(self):
        pass

    def add_chunk(self):
        pass
