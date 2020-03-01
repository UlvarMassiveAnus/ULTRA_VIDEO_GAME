import pygame
import sqlite3


class WinScene:
    def __init__(self, canvas, time, deaths, lvl):
        self.canvas = canvas
        self.lvl = lvl
        self.time = int(time) / 1000
        self.deaths = deaths
        self.scene_image = pygame.Surface((500, 500))
        self.scene_image.fill((255, 255, 255))

    def render(self):
        time_text = f"TIME: {self.time} secs"
        deaths_text = f"DEATHS: {self.deaths}"
        font = pygame.font.Font(None, 45)
        time_text = font.render(time_text, 1, (0, 0, 0))
        deaths_text = font.render(deaths_text, 1, (0, 0, 0))
        message = font.render("Чтобы продолжить нажми ЛКМ", 1, (0, 0, 0))
        self.change_database()
        self.scene_image.blit(time_text, (0, 0))
        self.scene_image.blit(deaths_text, (0, 50))
        self.scene_image.blit(message, (10, 400))
        self.canvas.blit(self.scene_image, (150, 50))

    def change_database(self):
        conn = sqlite3.connect("UVG_records.db")
        cursor = conn.cursor()
        cursor.execute(f"""UPDATE records SET time = {self.time}, deaths = {self.deaths} WHERE level == {self.lvl}""")
        conn.commit()
        conn.close()

    def move(self):
        if pygame.mouse.get_pressed()[0]:
            return "play"
        return ""
