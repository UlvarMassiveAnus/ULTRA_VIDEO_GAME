import pygame


class Menu:
    def __init__(self, canvas, puncts_names):
        self.puncts = []
        self.puncts_names = puncts_names
        self.canvas = canvas
        self.create_menu()

    def render(self):
        mouse_coords = pygame.mouse.get_pos()
        self.canvas.fill((100, 100, 0))
        for punct in self.puncts:
            punct.hover(mouse_coords)
            if punct.state:
                pygame.draw.rect(self.canvas, pygame.Color('yellow'), punct.position, 0)
            else:
                pygame.draw.rect(self.canvas, pygame.Color('red'), punct.position, 0)

    def move(self):
        m_keys = pygame.mouse.get_pressed()
        if m_keys[0]:
            for p in self.puncts:
                if p.state:
                    return p.pname

    def create_menu(self):
        w, h = self.canvas.get_width(), self.canvas.get_height()
        width, height = 400, 100
        for i, elem in enumerate(self.puncts_names):
            coords = w // 2 - width // 2, height + 150 * i + 50, width, height
            p = MenuPunct(coords, elem)
            self.puncts.append(p)


class MenuPunct:
    def __init__(self, coords, pname):
        self.position = self.x, self.y, self.w, self.h = coords
        self.pname = pname
        self.state = False

    def hover(self, mouse_coords):
        pos = mouse_coords
        if pos[0] < self.x + self.w and pos[0] > self.x and pos[1] < self.y + self.h and pos[1] > self.y:
            self.state = True
        else:
            self.state = False
        return self.state
