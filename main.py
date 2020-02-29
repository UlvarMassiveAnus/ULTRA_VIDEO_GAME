import pygame
from GameScene import GameScene, Level
from MenuScene import MenuScene
from LevelScene import LevelScene
from SettingsScene import SettingsScene

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
    nextScene = current_scene.move()

    if nextScene == "play":
        current_scene = level_menu
    elif nextScene == "1":
        game = GameScene(levels[0], "1", screen)
        current_scene = game
    elif nextScene == "2":
        game = GameScene(levels[1], "2", screen)
        current_scene = game
    elif nextScene == "3":
        game = GameScene(levels[2], "3", screen)
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
