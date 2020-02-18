import pygame
from player import Steve
from my_platform import Block
from gun import Bullet, Gun

pygame.init()

player = Steve(100, 100)

size = width, height = 1000, 600
screen = pygame.display.set_mode(size)


def create_level(level):
    blocked_level = []
    for i in range(24):
        for j in range(40):
            if level[i][j] == '_':
                blocked_level.append(Block(j * 25, i * 25, 25, 25))
    return blocked_level


level = create_level(
    [
        '________________________________________',
        '_                                      _',
        '_                                      _',
        '_      _______                         _',
        '_                                      _',
        '_                      ______          _',
        '_                                      _',
        '_   ______________                     _',
        '_                                      _',
        '_                                      _',
        '_             __________________________',
        '_                                      _',
        '_                                      _',
        '___________                            _',
        '_                  _____________________',
        '_                                      _',
        '_                                      _',
        '_                                      _',
        '_                                      _',
        '_      ___________                     _',
        '_                                      _',
        '_                                      _',
        '_                                      _',
        '________________________________________'
    ]
)

gun = Gun()
bullets = []
run = True
while run:
    pygame.time.delay(15)
    screen.fill((0, 0, 0))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.speed_x = -3
    if keys[pygame.K_RIGHT]:
        player.speed_x = 3
    if keys[pygame.K_UP] and player.onGround:
        player.speed_y = -10
        player.onGround = False
    if keys[pygame.K_SPACE]:
        if gun.charged:
            gun.charged = False
            gun.start_recharge = pygame.time.get_ticks()
            b = Bullet(player.x, player.y + player.w // 2)
            b.launch(player.vector)
            gun.cage.append(b)

    player.update(level)
    player.render(screen)
    player.speed_x = 0
    gun.render(level)
    if not gun.charged:
        gun.recharge()
    for bullet in gun.cage:
        pygame.draw.rect(screen, pygame.Color('red'), [int(bullet.x), int(bullet.y), int(bullet.w), int(bullet.h)], 0)
    for block in level:
        pygame.draw.rect(screen, pygame.Color('blue'), [block.x, block.y, block.w, block.h], 0)
    pygame.display.flip()

pygame.quit()
