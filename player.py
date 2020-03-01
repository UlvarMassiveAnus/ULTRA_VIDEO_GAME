import pygame
from my_platform import Block
from gun import Gun, Bullet
from Mob_Animation import AnimatedSprite


class Steve:
    def __init__(self, x=100, y=100):
        self.spawn_x, self.spawn_y = x, y
        self.w, self.h = 23, 23
        self.x, self.y = self.spawn_x, self.spawn_y
        self.speed_x, self.speed_y = 0, 0
        self.onGround = False
        self.vector = 1
        self.health = 10000
        self.type = "steve"
        self.gun = Gun("enemy", 500)
        self.live = pygame.time.get_ticks()
        self.deaths = 0

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
            collision = self.collision(block)
            if collision[0] and collision[1]:
                if block.type == "spike" and all(self.collision(Block(block.x, block.y - 5, block.w, block.h - 20))):
                    self.respawn()
                    break
                if all(self.collision(Block(block.x + 3, block.y, block.w - 6, block.h - 20))):
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

    def respawn(self):
        self.x, self.y = self.spawn_x, self.spawn_y
        self.health = 100
        self.deaths += 1

    def render(self, surface):
        pygame.draw.rect(surface, pygame.Color('gray'), [self.x, self.y, self.w, self.h], 0)

    def collision(self, other):
        x_collision = (self.w + other.w) >= max(abs(other.x + other.w - self.x), abs(self.x + self.w - other.x))
        y_collision = (self.h + other.h) >= max(abs(other.y + other.h - self.y), abs(self.y + self.h - other.y))
        return x_collision, y_collision

    def taking_damage(self):
        self.health -= 25
        if self.health <= 0:
            self.respawn()

    def shoot(self):
        self.gun.charged = False
        b = Bullet(self.x, self.y)
        b.launch(self.vector)
        self.gun.cage.append(b)
        self.gun.start_recharge = pygame.time.get_ticks()


class Enemy:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.health = 25
        self.type = "enemy"
        self.gun = Gun("steve", 1000)
        self.animation = AnimatedSprite(["left_enemy_waiting_sheets", "right_enemy_waiting_sheets",
                                         "left_enemy_shooting_sheets", "right_enemy_shooting_sheets"], (self.w + 25, self.h))

    def taking_damage(self):
        self.health -= 25

    def shoot(self, player):
        if player.x != self.x:
            enemy_vector = (player.x - self.x) / abs(player.x - self.x)
        else:
            enemy_vector = 1
        if self.collision(player)[1] and self.gun.charged:
            if enemy_vector == 1:
                self.animation.start(3)
            elif enemy_vector == -1:
                self.animation.start(2)
            self.gun.charged = False
            b = Bullet(self.x, self.y + 5)
            b.launch(enemy_vector)
            self.gun.cage.append(b)
            self.gun.start_recharge = pygame.time.get_ticks()
        elif not self.collision(player)[1]:
            if enemy_vector == 1:
                self.animation.start(1)
            elif enemy_vector == -1:
                self.animation.start(0)

    def render(self, level, player, canvas):
        self.shoot(player)
        self.animation.next()
        self.gun.recharge()
        self.gun.render(level, [player], canvas)
        if self.animation.cur_anim == 0 or self.animation.cur_anim == 2:
            canvas.blit(self.animation.cur_frame, (self.x - (self.animation.cur_frame.get_width() - self.w), self.y))
        else:
            canvas.blit(self.animation.cur_frame, (self.x, self.y))

    def collision(self, other):
        x_collision = (self.w + other.w) >= max(abs(other.x + other.w - self.x), abs(self.x + self.w - other.x))
        y_collision = (self.h + other.h) >= max(abs(other.y + other.h - self.y), abs(self.y + self.h - other.y))
        return x_collision, y_collision
