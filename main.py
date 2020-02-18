import pygame
from GameScene import GameScene
from MenuScene import Menu

pygame.init()
size = width, height = 800, 600
window = pygame.display.set_mode(size)
screen = pygame.Surface(size)
l_map = [
    '________________________________',
    '_                              _',
    '_                              _',
    '_                              _',
    '_                              _',
    '_                ________      _',
    '_                              _',
    '_                              _',
    '_                              _',
    '_                              _',
    '_                              _',
    '_         _______              _',
    '_                              _',
    '_                              _',
    '_                              _',
    '_               ________       _',
    '_                              _',
    '_     _____                    _',
    '_                              _',
    '_            __                _',
    '_                  ______      _',
    '_                              _',
    '_                              _',
    '________________________________'
]
game = GameScene(l_map, screen)
menu = Menu(screen, ['Play', 'Settings', 'Exit'])
current_scene = menu
run = True

while run:
    pygame.time.delay(10)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    current_scene.render(pygame.mouse.get_pos(), pygame.key.get_pressed())
    nextScene = current_scene.move(pygame.key.get_pressed())

    if nextScene == "Play":
        current_scene = game
    elif nextScene == "menu":
        current_scene = menu

    window.blit(screen, (0, 0))
    pygame.display.flip()


pygame.quit()