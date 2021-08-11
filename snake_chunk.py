class SnakeChunk:
    def __init__(self, x: int, y: int, size: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + size
        self.y2 = y + size
