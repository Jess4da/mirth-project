"""
Shows the main menu for the game, gets the user name before starting
"""
import pygame
from app.network import Network
from app.game import Game
from app.player import Player
from app.config import config
from app.lang import sys_lang
from moviepy.editor import VideoFileClip
import PIL


class MainMenu:
    BG = pygame.image.load('contents/bg.png')
    BG = pygame.transform.scale(BG, (1300, 1000))

    def __init__(self):
        self.WIDTH = 1300
        self.HEIGHT = 1000
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.name = ""
        self.waiting = False
        self.name_font = pygame.font.Font('contents/font.ttf', 80)
        self.title_font = pygame.font.Font('contents/font.ttf', 80)
        self.enter_font = pygame.font.Font('contents/font.ttf', 60)
        self.language = 'English'
        self.__click = False

    def draw(self):
        self.win.blit(self.BG, (0, 0))
        title = self.title_font.render(sys_lang.lang(self.language)['1'], 1, (255, 255, 255))
        self.win.blit(title, (self.WIDTH/2 - title.get_width()/2, 20))

        name = self.name_font.render(sys_lang.lang(self.language)['2'] + ": " + self.name, 1, (255, 255, 255))
        self.win.blit(name, (100, 400))

        # Lang button
        ButtonText = self.enter_font.render("Language " + self.language, 1, (255, 255, 255))
        languageButton = pygame.Rect((self.WIDTH/2 + 270, self.HEIGHT/2 + 50), (130, 100))
        self.win.blit(ButtonText, (self.WIDTH/2, self.HEIGHT/2 + 50))

        pos = pygame.mouse.get_pos()

        if languageButton.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.__click == False:
                self.language = "Thai" if self.language == "English" else "English"
                self.__click = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.__click = False

        if self.waiting:
            enter = self.enter_font.render(sys_lang.lang(self.language)['3'] + "...", 1, (255, 255, 255))
            self.win.blit(enter, (self.WIDTH - enter.get_width(), 900))
        else:
            enter = self.enter_font.render(sys_lang.lang(self.language)['4'] + "...", 1, (255, 255, 255))
            self.win.blit(enter, (self.WIDTH - enter.get_width(), 900))

        try:
            if self.n.status() == 0:
                self.waiting = False
                enter = self.enter_font.render(sys_lang.lang(self.language)['5'] + "...", 1, (255, 255, 255))
                self.win.blit(enter, (self.WIDTH - enter.get_width(), 800))
        except Exception:
            pass

        pygame.display.flip()

        pygame.display.update()

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(30)
            self.draw()

            if self.waiting and self.n.status():
                response = self.n.send({-1: []})
                # name&score
                if response:
                    run = False
                    g = Game(self.win, self.n)
                    g.set_lang(self.language)
                    for player in response:
                        p = Player(player)
                        g.add_player(p)
                    g.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                if self.waiting == False:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            if len(self.name) > 1:
                                self.n = Network(self.name)
                                self.waiting = True
                        else:
                            # gets the key name
                            key_name = pygame.key.name(event.key)

                            # converts to uppercase the key name
                            key_name = key_name.lower()
                            self.type(key_name)

    def type(self, char):
        if char == "backspace":
            if len(self.name) > 0:
                self.name = self.name[:-1]
        elif char == "space":
            self.name += " "
        elif len(char) == 1:
            self.name += char

        if len(self.name) >= 6:
            self.name = self.name[:6]


if __name__ == "__main__":
    clip = VideoFileClip('contents/intro.mp4')
    clip = clip.resize((1300, 1000))
    pygame.display.set_caption('How to win lord demon!')
    clip.preview()
    pygame.font.init()
    main = MainMenu()
    main.run()
