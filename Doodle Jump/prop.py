import pygame
import random
from gameobject import GameObject
from board import Board
from config import *

class Prop(GameObject):
    def __init__(self, board):
        super().__init__()
        self.board = board
        self.type = random.randint(0, 2)  # 0 represents poison, 1 represents jetpack, 2 represents shield
        if self.type == 0:
            self.image = pygame.transform.scale(pygame.image.load('images/poison.png'), (POISON_WIDTH, POISON_HEIGHT))
        elif self.type == 1:
            self.image = pygame.transform.scale(pygame.image.load('images/jetpack.png'), (JETPACK_WIDTH, JETPACK_HEIGHT))
        elif self.type == 2:
            self.image = pygame.transform.scale(pygame.image.load('images/shield.png'), (SHIELD_WIDTH, SHIELD_HEIGHT))
        self.rect = self.image.get_rect(midbottom=board.rect.midtop)

    def update(self, boards):
        super().update()

        # Keep the prop moving the same speed of the board
        if self.get_platform(boards):
            self.rect.move_ip(self.get_platform(boards).horizontal_speed, Board.vertical_speed)
        else:
            self.vertical_speed += self.acceleration
            self.rect.move_ip(0, self.vertical_speed)