import pygame
from my_platform import Block


class Steve:
    def __init__(self, x=100, y=100):
        self.w, self.h = 23, 23
        self.x, self.y = x, y
        self.speed_x, self.speed_y = 0, 0
        self.onGround = False
        self.vector = 1

    def update(self, level):
        self.speed_y += 0.3  # is gravity
        self.x += self.speed_x
        self.move(level, 1)
        self.y += self.speed_y
        self.move(level, 0)
        if self.speed_x > 0:
            self.vector = 1
        elif self.speed_x < 0:
            self.vector = -1

    def move(self, level, k):
        for block in level:
            collision = block.collision(self)
            if collision[0] and collision[1]:
                if block.enemy and all(Block(block.x, block.y - 5, block.w, block.h - 20).collision(self)):
                    self.x, self.y = 100, 100
                    break
                if all(Block(block.x + 3, block.y, block.w - 6, block.h - 20).collision(self)):
                    self.onGround = True
                if k:
                    if self.speed_x > 0:
                        self.x = block.x - self.w - 1
                    elif self.speed_x < 0:
                        self.x = block.x + block.w + 1
                else:
                    if self.speed_y > 0:
                        self.speed_y = 0
                        self.y = block.y - self.h - 1
                    elif self.speed_y < 0:
                        self.speed_y = 0
                        self.y = block.y + block.h + 1

    def render(self, surface):
        pygame.draw.rect(surface, pygame.Color('gray'), [self.x, self.y, self.w, self.h], 0)
