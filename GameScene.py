import pygame
from player import Steve, Enemy
from my_platform import Block, Spikes


class GameScene:
    def __init__(self, l_map, name, canvas):
        self.canvas = canvas
        self.level = Level(l_map, name)
        self.player = Steve(self.level.steve_spawn[1], self.level.steve_spawn[0])

    def render(self):
        keys = pygame.key.get_pressed()
        self.canvas.fill((0, 0, 0))
        if keys[pygame.K_a]:
            self.player.speed_x = -1.5
        if keys[pygame.K_d]:
            self.player.speed_x = 1.5
        if keys[pygame.K_w] and self.player.onGround:
            self.player.speed_y = -10
            self.player.onGround = False
        if keys[pygame.K_SPACE] and self.player.gun.charged:
            self.player.shoot()

        self.canvas.blit(self.level.level_canvas, (0, 0))

        self.player.update(self.level.level + self.level.enemies)
        self.player.render(self.canvas)
        self.player.speed_x = 0

        self.player.gun.recharge()
        self.player.gun.render(self.level.level, self.level.enemies, self.canvas)

        for enemy in self.level.enemies:
            enemy.render(self.level.level, self.player, self.canvas)

    def move(self):
        keys = pygame.key.get_pressed()
        if len(self.level.enemies) == 0:
            return  f"win_{self.player.deaths}_{pygame.time.get_ticks() - self.player.live}"
        elif keys[pygame.K_BACKSPACE]:
            return "play"
        elif keys[pygame.K_r]:
            return self.level.name
        return ""


class Level:
    def __init__(self, l_map, name):
        self.spike_image = pygame.Surface((25, 25))
        self.block_image = pygame.Surface((25, 25))
        self.spike_image.fill(pygame.Color("red"))
        self.block_image.fill(pygame.Color("yellow"))
        self.name = name
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
            if elem.type == "spike":
                self.level_canvas.blit(self.spike_image, (elem.x, elem.y))
            elif elem.type == "block":
                self.level_canvas.blit(self.block_image, (elem.x, elem.y))
