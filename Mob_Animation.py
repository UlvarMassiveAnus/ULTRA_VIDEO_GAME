import os
import pygame

FPS = 5
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, sheet_list, columns_list, size, coords,
                 speed):  # На вход подается список из ссылок на анимации,список с количеством спрайтов в анимации,размер,начальные координаты и скорость.
        super().__init__(all_sprites)
        self.alive = True
        self.step = 0
        self.frames = []
        self.size = size
        self.speed = speed
        self.coords = coords
        self.target = coords
        self.position = coords
        for i in range(len(sheet_list)):  # Создаю список списков с анимациями.
            self.frames.append(self.cut_sheet(sheet_list[i], columns_list[i], 1))
        self.cur_frame = 0  # Номер текущего кадра в анимации.
        self.cur_action = 0  # Номер текущей анимации.
        self.image = self.frames[self.cur_action][self.cur_frame]
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.rect.move(self.coords)

    def cut_sheet(self, sheet, columns, rows):
        frames = []
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))
        return frames

    def move(self, target):
        if self.alive:
            self.cur_action = 1
            self.target = target

    def shoot(self):
        if self.alive:
            self.cur_action = 2

    def die(self):
        self.cur_action = 3
        self.alive = False

    def update(self):
        if self.alive:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames[self.cur_action])
            self.image = self.frames[self.cur_action][self.cur_frame % len(self.frames[self.cur_action])]
            self.image = pygame.transform.scale(self.image, self.size)
            if self.cur_action == 1:
                if self.coords[0] < self.target:
                    self.rect = self.rect.move(self.speed, 0)
                    self.coords = (self.coords[0] + self.speed, self.coords[1])
                else:
                    self.cur_action = 0
        else:
            if self.cur_frame < len(self.frames[-1]) - 1:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames[self.cur_action])
                self.image = self.frames[self.cur_action][self.cur_frame % len(self.frames[self.cur_action])]
                self.image = pygame.transform.scale(self.image, self.size)
            else:
                self.image = self.frames[-1][-1]
                self.image = pygame.transform.scale(self.image, self.size)


enemy = AnimatedSprite([load_image("standing.jpg", -1),load_image("walking.jpg", -1),load_image("shooting.jpg", -1),load_image("dying.jpg", -1)], [1,6,4,5], (100, 100), (0, 0), 10)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[2]:
                enemy.shoot()
            elif pygame.mouse.get_pressed()[0]:
                enemy.move((100))
            elif pygame.mouse.get_pressed()[1]:
                enemy.die()
    screen.fill(pygame.Color("black"))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
