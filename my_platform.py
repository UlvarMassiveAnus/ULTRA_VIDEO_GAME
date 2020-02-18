class Block:
    def __init__(self, x, y, w, h):
        self.x, self.y = x, y
        self.w, self.h = w, h

    def collision(self, other):
        x_collision = (self.w + other.w) >= max(abs(other.x + other.w - self.x), abs(self.x + self.w - other.x))
        y_collision = (self.h + other.h) >= max(abs(other.y + other.h - self.y), abs(self.y + self.h - other.y))
        return x_collision, y_collision
