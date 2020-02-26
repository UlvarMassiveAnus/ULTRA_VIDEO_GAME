import pygame
from gun import Gun, Bullet


class Block:
    def __init__(self, x, y, w, h):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.type = "block"

    def collision(self, other):
        x_collision = (self.w + other.w) >= max(abs(other.x + other.w - self.x), abs(self.x + self.w - other.x))
        y_collision = (self.h + other.h) >= max(abs(other.y + other.h - self.y), abs(self.y + self.h - other.y))
        return x_collision, y_collision


class Spikes(Block):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.type = "spike"


class Enemy(Block):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.health = 25
        self.type = "enemy"
        self.gun = Gun("steve")

    def taking_damage(self):
        self.health -= 25

    def shoot(self, player):
        if self.collision(player)[1] and self.gun.charged:
            self.gun.charged = False
            b = Bullet(self.x, self.y)
            b.launch((player.x - self.x) / abs(player.x - self.x))
            self.gun.cage.append(b)
            self.gun.start_recharge = pygame.time.get_ticks()

    def render(self, level, player, canvas):
        self.shoot(player)
        self.gun.recharge()
        self.gun.render(level, [player], canvas)
        pygame.draw.rect(canvas, (255, 0, 255), [self.x, self.y, self.w, self.h], 0)

