class Block:
    def __init__(self, x, y, w, h):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.type = "block"


class Spikes(Block):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.type = "spike"
