import pygame
from MenuScene import MenuPunct
import os


class SettingsScene:
    def __init__(self, canvas):
        self.canvas = canvas
        self.back = MenuPunct((0, 525, 120, 75), "Назад")
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join("data", "backgrounds", "Main_Menu.jpg")),
                                         (800, 600))

    def render(self):
        self.canvas.blit(self.bg, (0, 0))
        self.back.hover(pygame.mouse.get_pos())
        if self.back.state:
            color = (255, 255, 0)
        else:
            color = (255, 0, 0)
        pygame.draw.rect(self.canvas, color, [0, 525, 120, 75], 0)
        self.canvas.blit(self.back.text, (self.back.x + self.back.w // 2 - self.back.text.get_width() // 2,
                                          self.back.y + self.back.h // 2 - self.back.text.get_height() // 2))

    def move(self):
        keys = pygame.key.get_pressed()
        m_keys = pygame.mouse.get_pressed()
        if keys[pygame.K_BACKSPACE] or m_keys[0] and self.back.state:
            return "menu"
        return ""
