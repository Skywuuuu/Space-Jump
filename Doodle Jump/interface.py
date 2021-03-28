import sys
from pygame.sprite import *
import pygame
from pygame.locals import *
from config import *


class Interface(Sprite):
    """
    The interface of the game
    """
    def __init__(self, screen, type, images, blink_images_num):
        super().__init__()
        self.screen = screen
        self.alive = True
        self.type = type
        self.blink_images_num = blink_images_num
        self.images = {}

        # print(images) # For test
        for image_name, (size, location) in images.items():
            # print(image_name, size, location) # For test
            self.load_image(image_name, size, location)
        self.image = None
        self.blit_image()
        self.rect = self.image.get_rect(topleft=(0, 0))

    def blit_image(self):
        """
        The first image should be the background of this interface, the images after the first image are buttons or
        other decorations

        :return:
        """
        for i, key in enumerate(self.images.keys()):
            if i == 0:
                self.image = self.images[key][0]
            else:
                self.image.blit(self.images[key][0],
                                self.images[key][0].get_rect(center=self.images[key][2]))
    
    def load_image(self, image_name, size, location):
        """
        Load the image information and store the image into a dictionary

        :param image_name: the name of image
        :param size: the size of the image
        :param location: the location of the image in the screen
        :return:
        """
        self.images[image_name] = (pygame.transform.scale(pygame.image.load('./images/' + image_name), size), size, location)

    def mouse_on_button(self, image_name):
        """
        Determine whether the mouse is on button or not

        :param image_name: the name of the image
        :return: Boolean value
        """
        # Identify the location of mouse
        x, y = pygame.mouse.get_pos()

        # Do if the mouse on the button
        if self.images[image_name][2][0] - self.images[image_name][1][0]//2 <= x <= self.images[image_name][2][0] + self.images[image_name][1][0]//2\
                and self.images[image_name][2][1] - self.images[image_name][1][1]//2<= y <= self.images[image_name][2][1] + self.images[image_name][1][1]//2:
            self.image = self.images[image_name][0]
            self.rect = self.image.get_rect(center=(self.images[image_name][2]))
            return True
        return False

    def click_button(self, image_name):
        """
        Judge whether the mouse click or not
        :param image_name:
        :return:
        """
        buttons = pygame.mouse.get_pressed()
        if buttons[0]:  # If click the left button on the mouse, buttons[0]=True
            self.alive = False
            if image_name == 'quit.png':
                pygame.quit()
                sys.exit()

    
    def update(self):
        super().update()

        # Detect mouse clicks
        for key in list(self.images.keys())[1:1+self.blink_images_num]:
            if self.mouse_on_button(key):
                # print(key) # For test
                self.click_button(key)
                break
        else:
            self.image = list(self.images.values())[0][0]
            self.rect = self.image.get_rect(topleft=(0, 0))
