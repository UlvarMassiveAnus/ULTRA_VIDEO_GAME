import pygame
from player import Steve
from my_platform import Enemy
from my_platform import Block, Spikes
from gun import Gun, Bullet


class GameScene:
    def __init__(self, l_map, canvas):
        self.canvas = canvas
        self.level = Level(l_map)
        self.player = Steve(self.level.steve_spawn[1], self.level.steve_spawn[0])
        self.gun = Gun("enemy")

    def render(self):
        keys = pygame.key.get_pressed()
        self.canvas.fill((0, 0, 0))
        if keys[pygame.K_a]:
            self.player.speed_x = -2
        if keys[pygame.K_d]:
            self.player.speed_x = 2
        if keys[pygame.K_w] and self.player.onGround:
            self.player.speed_y = -10
            self.player.onGround = False
        if keys[pygame.K_SPACE] and self.gun.charged:
            self.gun.charged = False
            b = Bullet(self.player.x, self.player.y)
            b.launch(self.player.vector)
            self.gun.cage.append(b)
            self.gun.start_recharge = pygame.time.get_ticks()

        self.canvas.blit(self.level.level_canvas, (0, 0))

        self.player.update(self.level.level + self.level.enemies)
        self.player.render(self.canvas)
        self.player.speed_x = 0

        self.gun.recharge()
        self.gun.render(self.level.level, self.level.enemies, self.canvas)

        for enemy in self.level.enemies:
            enemy.render(self.level.level, self.player, self.canvas)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_BACKSPACE]:
            return "menu"


class Level:
    def __init__(self, l_map):
        self.map = l_map
        self.level = []
        self.level_spikes = []
        self.steve_spawn = None
        self.level_canvas = pygame.Surface((800, 600))
        self.enemies = []
        self.create_level()

    def create_level(self):
        w, h = len(self.map[0]), len(self.map)
        for i in range(h):
            for j in range(w):
                if self.map[i][j] == "_":
                    self.level.append(Block(j * 25, i * 25, 25, 25))
                elif self.map[i][j] == "@":
                    self.level_spikes.append(Spikes(j * 25, i * 25, 25, 25))
                elif self.map[i][j] == "!":
                    self.steve_spawn = (i * 25 + 1, j * 25 + 1)
                elif self.map[i][j] == "e":
                    self.enemies.append(Enemy(j * 25, i * 25, 25, 25))

        self.level = self.level_spikes + self.level

        for elem in self.level:
            color = (0, 0, 0)
            if elem.type == "spike":
                color = (255, 0, 0)
            elif elem.type == "block":
                color = (0, 0, 255)
            pygame.draw.rect(self.level_canvas, color, [elem.x, elem.y, elem.w, elem.h], 0)
