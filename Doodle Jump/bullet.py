import pygame

from config import *
from gameobject import GameObject

class Bullet(GameObject):
    def __init__(self, pos, horizontal_speed, vertical_speed, type ): #BOSS.tpye=1 Player.type=0
        super().__init__()
        self.type=type
        if self.type:
             
             self.image = pygame.transform.scale(pygame.image.load('images/bullet_enemy.png'), (BULLET_WIDTH, BULLET_HEIGHT))
        else:
           self.image = pygame.transform.scale(pygame.image.load('images/bullet.png'), (BULLET_WIDTH, BULLET_HEIGHT)) 
        self.rect = self.image.get_rect(midbottom=pos)
        self.horizontal_speed = horizontal_speed
        self.vertical_speed = vertical_speed

    def update(self):
        super().update()
        self.rect.move_ip(self.horizontal_speed, self.vertical_speed)   # The speed of the bullet

        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.horizontal_speed = -self.horizontal_speed