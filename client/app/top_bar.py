"""
Top bar displaying information about round
"""
import pygame
import re
from .config import config
from .lang import sys_lang


class TopBar(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.word = ""
        self.round = 1
        self.max_round = 8
        self.round_font = pygame.font.Font('contents/font.ttf', 50)
        self.word_font = pygame.font.Font('contents/font.ttf', 30)
        self.BORDER_THICKNESS = 5
        self.time = 60
        self.drawing = False
        self.top_vowel = ['ิ', '้']
        self.bottom_vowel = ['ุ']

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height), self.BORDER_THICKNESS)

        # draw round
        __round = sys_lang.lang(config['LANGUAGE']['lang'])['6']
        __of = sys_lang.lang(config['LANGUAGE']['lang'])['7']
        txt = self.round_font.render(f"{__round} {self.round} {__of} {self.max_round}", 1, (255, 255, 255))
        win.blit(txt, (self.x + 10, self.y + self.height/2 - txt.get_height()/2))

        # draw underscores
        if self.drawing:
            wrd = self.word
        else:
            wrd = self.underscore_text(self.word)

        txt = self.word_font.render(wrd, 1, (255, 255, 255))
        if self.drawing or re.match(r'[a-zA-Z]', self.word):
            win.blit(txt, (self.x + self.width/2 - txt.get_width()/2, self.y + self.height/2 - txt.get_height()/2 + 10))
        else:
            for i, n in enumerate(wrd):
                temp_txt = self.word_font.render(n, 1, (255, 255, 255))
                vowel = self.word_font.render("_", 1, (255, 255, 255))
                if n in self.top_vowel:
                    win.blit(vowel, (self.x + self.width/2 - txt.get_width()/2 + (i-1)*5, self.y + self.height/2 - txt.get_height()/2 + 5))
                    continue
                if n in self.bottom_vowel:
                    win.blit(vowel, (self.x + self.width/2 - txt.get_width()/2 + (i-1)*5, self.y + self.height/2 - txt.get_height()/2 + 20))
                    continue
                win.blit(temp_txt, (self.x + self.width/2 - txt.get_width()/2 + (i*5), self.y + self.height/2 - txt.get_height()/2 + 10))

        pygame.draw.circle(win, (255, 255, 255), (self.x + self.width - 50, self.y + round(self.height/2)), 40, 0)
        timer = self.round_font.render(str(self.time), 1, (0, 0, 0))
        win.blit(timer, (self.x + self.width - 50 - timer.get_width()/2, self.y + self.height/2 - timer.get_height()/2))

    def underscore_text(self, text):
        new_str = ""

        accept_char = ['-', ' ']

        for char in text:
            if char not in accept_char:
                new_str += " _ " if char not in self.top_vowel + self.bottom_vowel else char
            else:
                new_str += f" {char} "

        return new_str

    def change_word(self, word):
        self.word = word

    def change_round(self, rnd):
        self.round = rnd
