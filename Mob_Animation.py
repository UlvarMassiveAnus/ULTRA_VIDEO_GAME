import os
import pygame


class AnimatedSprite:
    def __init__(self, sheet_list, size):
        self.sheet_list = sheet_list
        self.frames = []
        self.size = size
        self.frames_creator()
        self.cur_anim = 0
        self.cur_anim_len = 1
        self.cur_frame = self.frames[self.cur_anim][0]
        self.secs_anim = 0

    def start(self, start_anim):
        self.secs_anim = pygame.time.get_ticks()
        self.cur_anim = start_anim
        self.cur_anim_len = len(self.frames[start_anim])

    def next(self):
        self.cur_frame = self.frames[self.cur_anim][
            ((pygame.time.get_ticks() - self.secs_anim) // 250) % self.cur_anim_len]

    def load_image(self, name, dir, color_key=None):
        fullname = os.path.join('data', dir, name)
        try:
            image = pygame.image.load(fullname).convert()
        except pygame.error as message:
            print('Cannot load image:', name)
            raise SystemExit(message)

        if color_key is not None:
            if color_key == -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key)
        else:
            image = image.convert_alpha()

        image = pygame.transform.scale(image, self.size)
        return image

    def frames_creator(self):
        simple_anim = []
        for dir in self.sheet_list:
            for file_name in os.listdir("data/" + dir):
                simple_anim.append(self.load_image(file_name, dir))
            self.frames.append(simple_anim)
            simple_anim = []
