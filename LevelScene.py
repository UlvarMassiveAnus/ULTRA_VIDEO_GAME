import pygame
from MenuScene import MenuPunct
import os


class LevelScene:
    def __init__(self, canvas, puncts_names):
        self.puncts = []
        self.puncts_names = puncts_names
        self.canvas = canvas
        self.create_menu()
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join("data", "backgrounds", "Main_Menu.jpg")),
                                         (800, 600))

    def render(self):
        mouse_coords = pygame.mouse.get_pos()
        self.canvas.blit(self.bg, (0, 0))
        for punct in self.puncts:
            punct.hover(mouse_coords)
            if punct.state:
                pygame.draw.rect(self.canvas, pygame.Color('yellow'), punct.position, 0)
            else:
                pygame.draw.rect(self.canvas, pygame.Color('red'), punct.position, 0)
            self.canvas.blit(punct.text, (punct.x + punct.w // 2 - punct.text.get_width() // 2,
                                          punct.y + punct.h // 2 - punct.text.get_height() // 2))

    def move(self):
        m_keys = pygame.mouse.get_pressed()
        if m_keys[0]:
            for p in self.puncts:
                if p.pname == "назад" and p.state:
                    return "menu"
                if p.state:
                    return p.pname
        return ""

    def create_menu(self):
        width, height = 100, 100
        for i, elem in enumerate(self.puncts_names):
            coords = width * i + 20 * (i + 1), 20, width, height
            p = MenuPunct(coords, elem)
            self.puncts.append(p)
        self.puncts.append(MenuPunct((0, 525, 120, 75), "назад"))
