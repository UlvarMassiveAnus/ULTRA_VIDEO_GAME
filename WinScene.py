import pygame


class WinScene:
    def __init__(self, canvas, time, deaths):
        self.canvas = canvas
        self.time = time
        self.deaths = deaths
        self.scene_image = pygame.Surface((100, 100))
        self.scene_image.fill((255, 255, 255))

    def render(self):
        self.canvas.blit(self.scene_image, (100, 100))

    def move(self):
        if any(pygame.key.get_pressed()):
            return "play"
        return ""
