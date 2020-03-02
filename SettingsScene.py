import pygame
from MenuScene import MenuPunct
import os
import sqlite3


class SettingsScene:
    def __init__(self, canvas):
        self.canvas = canvas
        self.back = MenuPunct((0, 525, 120, 75), "Назад")
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join("data", "backgrounds", "Main_Menu.jpg")),
                                         (800, 600))
        print(self.data_base())

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
        f1 = pygame.font.Font(None, 30)
        f2 = pygame.font.Font(None, 42)
        text = f2.render('Статистика', 1, (180, 0, 0))
        self.canvas.blit(text, (350, 20))
        for i in range(len(self.data_base())):
            text = f1.render(self.data_base()[i], 1, (180, 0, 0))
            self.canvas.blit(text, (10, 150 + (i * 30)))

    def move(self):
        keys = pygame.key.get_pressed()
        m_keys = pygame.mouse.get_pressed()
        if keys[pygame.K_BACKSPACE] or m_keys[0] and self.back.state:
            return "menu"
        return ""

    def data_base(self):
        con = sqlite3.connect("UVG_records.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM records""").fetchall()
        con.close()
        st = []
        id = []
        levels = []
        depths = []
        time = []
        data = result
        for i in data:
            id.append(str(i[0]) + '.')
            levels.append("Уровень - " + str(i[1]))
            depths.append("Количество смертей - " + str(i[2]))
            time.append("Время прохождения - " + str(i[3]))
        for i in range(len(id)):
            st.append(id[i] + ' ' + levels[i] + ' ' + depths[i] + ' ' + time[i])
        return st
