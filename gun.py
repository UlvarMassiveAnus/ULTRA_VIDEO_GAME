import pygame


class Bullet:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.w = 5
        self.h = 5
        self.speed = 0

    def launch(self, vect):
        self.speed = vect * 0.1

    def move(self):
        self.x += self.speed

    def collision(self, other):
        x_collision = (self.w + other.w) >= max(abs(other.x + other.w - self.x), abs(self.x + self.w - other.x))
        y_collision = (self.h + other.h) >= max(abs(other.y + other.h - self.y), abs(self.y + self.h - other.y))
        return x_collision, y_collision


class Gun:
    def __init__(self, enForThis, recharge_time):
        self.cage = []
        self.charged = True
        self.start_recharge = 0
        self.enForThis = enForThis
        self.recharge_time = recharge_time

    def render(self, level, enemies, canvas):
        for block in level + enemies:
            for bullet in self.cage:
                bullet.move()
                pygame.draw.rect(canvas, (255, 255, 0), [bullet.x, bullet.y, bullet.w, bullet.h], 0)
                if all(bullet.collision(block)):
                    self.cage.pop(self.cage.index(bullet))
                    if block.type == "enemy" and self.enForThis == "enemy":
                        block.taking_damage()
                        if block.health <= 0:
                            enemies.pop(enemies.index(block))
                    elif block.type == "steve" and self.enForThis == "steve":
                        block.taking_damage()

    def recharge(self):
        if pygame.time.get_ticks() - self.start_recharge > self.recharge_time:
            self.charged = True
