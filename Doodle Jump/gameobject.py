from pygame.sprite import *
from config import *

class GameObject(Sprite):
    def __init__(self):
        super().__init__()
        self.alive = True           # Represent that the object is alive
        self.acceleration = 1       # Acceleration in physics
        self.vertical_speed = 0     # Vertical_speed
        self.horizontal_speed = 0

    def collide_with(self, group) -> Sprite:
        """
        Handle the object collide with other object

        :param group:
        :return Sprite Object:
        """
        return spritecollideany(self, group)

    def get_platform(self, boards):
        """
        Get the board

        :param boards:
        :return platform:
        """
        for board in boards:
            # Determine whether or not the object collides with the platform
            if self.rect.right >= board.rect.left and self.rect.left <= board.rect.right:
                if board.rect.top == self.rect.bottom or self.rect.bottom - (self.vertical_speed - self.acceleration) <= board.rect.top <= self.rect.bottom:
                    return board
        return None

    def update(self):
        if self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.alive = False