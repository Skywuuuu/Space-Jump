import pygame
from pygame.locals import *
import time

from config import *
from gameobject import GameObject
from board import Board
from bullet import Bullet


class Player(GameObject):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('images/player.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.image.get_rect(midbottom=(WIDTH / 2, HEIGHT * 2 / 3))
        self.init_speed = -PLAYER_VERTICAL_SPEED
        self.horizontal_speed = PLAYER_HORIZONTAL_SPEED
        self.shot_time = time.time()
        self.shot_period = PLAYER_SHOOT_PERIOD
        self.dizzy = False
        self.dizzy_time = time.time()
        self.flying = False
        self.flying_time = time.time()
        self.protected = False


    def update(self, pressed_keys, boards, player_bullets, boss_bullets, enemies, props):
        super().update()

        # Check whether player hit the prop
        prop = self.collide_with(props)
        if prop is not None:
            prop.alive = False
            # 0 stands for poison
            if prop.type == 0:
                self.dizzy = True
                self.dizzy_time = time.time()

            # 1 stands for the jetpack
            elif prop.type == 1:
                self.flying = True
                self.flying_time = time.time()
                Board.vertical_speed = 15
            # 2 stands for the shield
            elif prop.type == 2:
                self.protected = True

        # Check whether the player hit the bullets of boss
        bullet = self.collide_with(boss_bullets)
        if  not self.flying :          
           if bullet is not None and not self.protected  :
               self.alive = False
               bullet.alive = False
           if bullet is not None and self.protected:
               self.protected = False
               bullet.alive = False

        # Check whether the player hit the enemy
        enemy = self.collide_with(enemies)
        if  not self.flying : 
           if enemy is not None and not self.protected  :
               self.alive = False
               enemy.alive = False
           if enemy is not None and self.protected:
               self.protected = False
               enemy.alive = False
            
            

        if self.flying and self.dizzy and self.protected:
                self.image = pygame.transform.scale(pygame.image.load('images/player_dizzy_shield_rocket.png'),
                                                (PLAYER_WIDTH, PLAYER_HEIGHT))
        elif self.protected and self.flying:
                self.image = pygame.transform.scale(pygame.image.load('images/player_shield_rocket.png'),
                                                (PLAYER_WIDTH, PLAYER_HEIGHT))
        elif self.protected and self.dizzy:  
                self.image = pygame.transform.scale(pygame.image.load('images/player_dizzy_shield.png'),
                                                (PLAYER_WIDTH, PLAYER_HEIGHT))
        elif self.flying and self.dizzy:  
                self.image = pygame.transform.scale(pygame.image.load('images/player_dizzy_rocket.png'),
                                                (PLAYER_WIDTH, PLAYER_HEIGHT))
        elif self.protected:
                self.image = pygame.transform.scale(pygame.image.load('images/player_shield.png'),
                                                (PLAYER_WIDTH, PLAYER_HEIGHT))
        elif self.dizzy:
                 self.image = pygame.transform.scale(pygame.image.load('images/player_dizzy.png'),
                                                (PLAYER_WIDTH, PLAYER_HEIGHT))
        elif self.flying:
                 self.image = pygame.transform.scale(pygame.image.load('images/player_rocket.png'),
                                                (PLAYER_WIDTH, PLAYER_HEIGHT))      
        else:
            self.image = pygame.transform.scale(pygame.image.load('images/player.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))

        # Adjust the dizzy status if the dizzy time is over
        if time.time() - self.dizzy_time > PLAYER_DIZZY_PERIOD:
            self.dizzy = False

        # Adjust the flying status if the flying time is over
        if time.time() - self.flying_time > PLAYER_FLYING_PERIOD:
            self.flying = False
            Board.vertical_speed = 3

        if not self.flying:
            board = self.get_platform(boards)
            if board:
                if pressed_keys[K_UP]:  # The UP KEY is pressed
                    self.vertical_speed = self.init_speed  # Give an initial speed
                    self.rect.move_ip(0, self.vertical_speed)
                if self.vertical_speed > 0:  # Player drop to board from the air
                    self.vertical_speed = 0
                    self.rect.bottom = board.rect.top
                if self.vertical_speed == 0:  # Player stay on the board
                    self.rect.move_ip(self.get_platform(boards).horizontal_speed, Board.vertical_speed)
                if not board.stable: # If the player touch the unstable board, it will jump automatically
                    self.vertical_speed = self.init_speed
                    board.alive = False
            else:  # Player is not on the board
                self.vertical_speed += self.acceleration
                self.rect.move_ip(0, self.vertical_speed)




        if pressed_keys[K_DOWN]:  # Press the DOWN KEY to shoot the bullet
            if time.time() - self.shot_time > self.shot_period:
                player_bullets.add(Bullet(self.rect.midtop, 0, -BULLET_SPEED,0))
                self.shot_time = time.time()

        if pressed_keys[K_LEFT]:  # Press the LEFT KEY to move the player to the left
            if not self.dizzy:
                self.rect.move_ip(-self.horizontal_speed, 0)
            else:
                self.rect.move_ip(self.horizontal_speed, 0)

        if pressed_keys[K_RIGHT]:  # Press the RIGHT KEY to move the player to the right
            if not self.dizzy:
                self.rect.move_ip(self.horizontal_speed, 0)
            else:
                self.rect.move_ip(-self.horizontal_speed, 0)
        
        # Keep the player in the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0