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

    def render(self, level, enemies, canvas):
        for block in level + enemies:
            for bullet in self.cage:
                bullet.move()
                pygame.draw.rect(canvas, (255, 255, 0), [bullet.x, bullet.y, bullet.w, bullet.h], 0)
                if all(block.collision(bullet)):
                    self.cage.pop(self.cage.index(bullet))
                    if block.type == "enemy":
                        block.taking_damage()
                        if block.health <= 0:
                            enemies.pop(enemies.index(block))

    def recharge(self):
        if pygame.time.get_ticks() - self.start_recharge > 500:
            self.charged = True
