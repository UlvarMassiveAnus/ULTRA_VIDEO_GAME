import pygame
from GameScene import GameScene
from MenuScene import MenuScene
from SettingsScene import SettingsScene

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
    '_                ____@___      _',
    '_                              _',
    '_                              _',
    '_                              _',
    '_                              _',
    '_                              _',
    '_         _@_____              _',
    '_                              _',
    '_                              _',
    '_                e             _',
    '_               _____@__       _',
    '_                              _',
    '_     ____@                    _',
    '_                              _',
    '_          __@_                _',
    '_                  _@____      _',
    '_                              _',
    '_ !                            _',
    '________________________________'
]
settings = SettingsScene(screen)
menu = MenuScene(screen, ['play', 'settings', 'exit'])
current_scene = menu
run = True

while run:
    pygame.time.delay(15)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    current_scene.render()
    nextScene = current_scene.move()

    if nextScene == "play":
        game = GameScene(l_map, screen)
        current_scene = game
    elif nextScene == "menu":
        current_scene = menu
    elif nextScene == "settings":
        current_scene = settings
    elif nextScene == "exit":
        run = False

    window.blit(screen, (0, 0))
    pygame.display.flip()

pygame.quit()
