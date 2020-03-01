import pygame
from GameScene import GameScene
from MenuScene import MenuScene
from LevelScene import LevelScene
from SettingsScene import SettingsScene
from WinScene import WinScene

pygame.init()
size = width, height = 800, 600
window = pygame.display.set_mode(size)
screen = pygame.Surface(size)
levels = []
for i in range(3):
    with open(f"levels/level_{i + 1}.txt") as file:
        rows = list(map(lambda x: x[:32], file.readlines()))
    levels.append(rows)

settings = SettingsScene(screen)
menu = MenuScene(screen, ['play', 'settings', 'exit'])
level_menu = LevelScene(screen, ["1", "2", "3"])
current_scene = menu
run = True

while run:
    pygame.time.delay(10)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    current_scene.render()
    nextScene = current_scene.move().split("_")

    if nextScene[0] == "play":
        current_scene = level_menu
    elif nextScene[0] == "1":
        game = GameScene(levels[0], "1", screen)
        current_scene = game
    elif nextScene[0] == "2":
        game = GameScene(levels[1], "2", screen)
        current_scene = game
    elif nextScene[0] == "3":
        game = GameScene(levels[2], "3", screen)
        current_scene = game
    elif nextScene[0] == "menu":
        current_scene = menu
    elif nextScene[0] == "settings":
        current_scene = settings
    elif nextScene[0] == "exit":
        run = False
    elif nextScene[0] == "win":
        win = WinScene(screen, nextScene[2], nextScene[1], nextScene[3])
        current_scene = win

    window.blit(screen, (0, 0))
    pygame.display.flip()

pygame.quit()
