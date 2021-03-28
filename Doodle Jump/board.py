import pygame
import random
from config import *
from gameobject import GameObject


class Board(GameObject):
    num = BOARD_NUM  # Indicate the total number of the board
    vertical_speed = BOARD_VERTICAL_SPEED  # Indicate the vertical speed of the board

    def __init__(self, pos, randomly):
        super().__init__()
        self.stable = bool(random.randint(0, 5)) if randomly else True  # Indicates the board is stable or not
        self.horizontal_speed = random.randint(-1, 1) * 5 if randomly and self.stable and random.randint(0,
                                                                                                         3) == 0 else 0

        if not self.stable:
            self.image = pygame.transform.scale(pygame.image.load('images/redbroken.png'), (
                BOARD_WIDTH, BOARD_HEIGHT))  # Indicate the unstable but static board
        else:
            if self.horizontal_speed == 0:
                self.image = pygame.transform.scale(pygame.image.load('images/blue.png'), (
                    BOARD_WIDTH, BOARD_HEIGHT))  # Indicate the stable and static board
            else:
                self.image = pygame.transform.scale(pygame.image.load('images/beige.png'), (
                    BOARD_WIDTH, BOARD_HEIGHT))  # Indicate the stable and sliding board
        self.rect = self.image.get_rect(midtop=pos)

    def update(self):
        super().update()
        self.rect.move_ip(self.horizontal_speed,
                          Board.vertical_speed)  # Move the board down in order to make the player feel like jumping

        # Keep the sliding board inside the screen
        if self.rect.left <= 0:
            self.rect.left = 0
            self.horizontal_speed = -self.horizontal_speed
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            self.horizontal_speed = -self.horizontal_speed