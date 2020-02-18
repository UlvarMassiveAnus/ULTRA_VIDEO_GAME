import pygame


class Bullet:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.w = 30
        self.h = 2
        self.speed = 0

    def launch(self, vect):
        self.speed = vect * 0.1

    def move(self):
        self.x += self.speed


class Gun:
    def __init__(self):
        self.cage = []
        self.charged = True
        self.start_recharge = 0

    def render(self, level):
        for block in level:
            for bullet in self.cage:
                bullet.move()
                if all(block.collision(bullet)):
                    self.cage.pop(self.cage.index(bullet))

    def recharge(self):
        if pygame.time.get_ticks() - self.start_recharge > 500:
            self.charged = True
