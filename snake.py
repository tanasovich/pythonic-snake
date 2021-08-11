class Snake:
    directions: dict = {"Left": (-1, 0), "Up": (0, -1), "Right": (1, 0), "Down": (0, 1)}

    def __init__(self, snake_chunks):
        self.snake_chunks = snake_chunks
        self.direction_vector = Snake.directions["Right"]

    def move(self):
        pass

    def change_direction(self):
        pass

    def add_chunk(self):
        pass
