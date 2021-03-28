import pygame
import random

from config import *
from bullet import Bullet
from gameobject import GameObject

class Boss(GameObject):
    def __init__(self):
        super().__init__()
        self.HP = BOSS_HP
        self.image = pygame.transform.scale(pygame.image.load('images/ufo.png'), (BOSS_WIDTH, BOSS_HEIGHT))
        self.rect = self.image.get_rect(midtop=(WIDTH/2, 0))
        self.horizontal_speed = BOSS_HORIZONTAL_SPEED

    def update(self, player_bullets, boss_bullets):
        super().update()
        bullet = self.collide_with(player_bullets)
        if bullet is not None:
            self.HP -= 1
            player_bullets.remove(bullet)

        if self.HP == 0:
            self.alive = False

        if random.randint(0, 50) == 0:
          
            boss_bullets.add(Bullet((random.randint(self.rect.left, self.rect.right), self.rect.bottom), random.randint(-5, 5), 6, 1))

        self.rect.move_ip(self.horizontal_speed, 0)
        # Keep the boss inside the screen
        if self.rect.left <= 0:
            self.rect.left = 0
            self.horizontal_speed = -self.horizontal_speed
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            self.horizontal_speed = -self.horizontal_speed