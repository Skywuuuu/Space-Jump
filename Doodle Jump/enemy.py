import pygame
import random
from gameobject import GameObject
from board import Board
from config import *

class Enemy(GameObject):
    def __init__(self, board):
        super().__init__()
        self.board = board
        self.image = pygame.transform.scale(pygame.image.load('images/enemy'+str(random.randint(1, 5))+'.png'), (ENEMY_WIDTH, ENEMY_HEIGHT))
        self.rect = self.image.get_rect(midbottom=board.rect.midtop)

    def update(self, boards, player_bullets):
        super().update()
        bullet = self.collide_with(player_bullets)
        if bullet is not None:  # If the enemy collides with bullets
            self.alive = False
            bullet.alive = False

        # Keep the enemy moving the same speed of the boards
        if self.get_platform(boards):
            self.rect.move_ip(self.get_platform(boards).horizontal_speed, Board.vertical_speed)
        else:
            self.vertical_speed += self.acceleration
            self.rect.move_ip(0, self.vertical_speed)