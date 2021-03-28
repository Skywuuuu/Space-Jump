import pygame
from config import *

class ScoreBoard(pygame.sprite.Sprite):
    '''
    Define the score you get in the game
    '''
    def __init__(self):
        super().__init__()
        self.score = INITIAL_SCORE
        self.font = pygame.font.Font("./fonts/arista.ttf", 48)
        self.image = self.font.render(str(self.score), True, WHITE)
        self.rect = self.image.get_rect(topleft=(10, 10))
        self.alive = True

    def update(self, scores):
        for score in scores:
            self.score += score
        if len(scores) == 0:
            self.rect = self.image.get_rect(center=(WIDTH/2,HEIGHT/10))
            self.image = self.font.render('Your final score is '+str(self.score)+'!', True, WHITE)
        else:
            self.image = self.font.render(str(self.score), True, WHITE)
