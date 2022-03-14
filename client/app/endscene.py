"""
Shows the main menu for the game, gets the user name before starting
"""
import pygame
from .player import Player


class Endscene:
    BG = pygame.image.load('contents/end.png')
    BG = pygame.transform.scale(BG, (1300, 1000))

    def __init__(self):
        self.WIDTH = 1300
        self.HEIGHT = 1000
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.scoreboard = []
        self.title_font = pygame.font.Font('contents/font.ttf', 100)
        self.rank_font = pygame.font.Font('contents/font.ttf', 70)
        self.name_font = pygame.font.Font('contents/font.ttf', 60)

    def draw(self):
        self.win.blit(self.BG, (0, 0))
        title = self.title_font.render("WINNER", 1, (255, 255, 255))
        self.win.blit(title, (self.WIDTH/2 - title.get_width()/2, 50))

        scores = [(player.name, player.score) for player in self.scoreboard]
        scores.sort(key=lambda x: x[1], reverse=True)

        try:
            self.draw_rank("#1", scores[0][0], "Score : " + str(scores[0][1]), self.WIDTH/2, 200, self.name_font)

            self.draw_rank("#2", scores[1][0], "Score : " + str(scores[1][1]), 325, 400, self.name_font)

            self.draw_rank("#3", scores[2][0], "Score : " + str(scores[2][1]), 975, 400, self.name_font)

            self.draw_rank("#4", scores[3][0], "Score : " + str(scores[3][1]), self.WIDTH/2, 800, self.name_font)
        except:
            pass

        pygame.display.flip()

        pygame.display.update()

    def draw_rank(self, ranktext, nametext, sctext, width, height, font):

        rank = self.rank_font.render(ranktext, 1, (255, 255, 255))
        name = font.render(nametext, 1, (255, 255, 255))
        sc = font.render(sctext, 1, (255, 255, 255))

        pygame.draw.rect(self.win, [255, 255, 255], (width - rank.get_width()/2 - name.get_width()/2 - sc.get_width()/2,
                         height, rank.get_width()+name.get_width()+sc.get_width(), rank.get_height()+sc.get_height()), 5)
        #pygame.draw.rect(self.win, [100, 100, 100],(width - sc.get_width()/2 ,height + rank.get_height() - 5, sc.get_width(), sc.get_height()-5))

        self.win.blit(rank, (width - rank.get_width()/2 - name.get_width()/2, height))
        self.win.blit(name, (width - name.get_width()/2 + rank.get_width()/2, height))
        self.win.blit(sc, (width - sc.get_width()/2, height + rank.get_height()))

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(30)
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
