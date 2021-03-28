import sys
import random
import time
import pygame
from pygame.locals import *

from config import *
from board import Board
from player import Player
from enemy import Enemy
from scoreboard import ScoreBoard
from prop import Prop
from boss import Boss
from interface import Interface


def create_new(groups):
    """
    Create new board, enemy and props.

    :return:
    """
    if len(groups['boards']) < Board.num:
        board = Board(pos=(random.randint(0, WIDTH), 0), randomly=True)
        groups['boards'].add(board)
        random_num = random.randint(1, 100)
        if random_num <= ENEMY_PROB:
            groups['enemies'].add(Enemy(board))
        if random_num >= 100 - PROPS_PROB:
            groups['props'].add(Prop(board))

    if len(groups['boss']) == 0 and time.time() - boss_dead_time > BOSS_REFRESH_PERIOD:
        groups['boss'].add(Boss())


def remove_dead(group):
    """
    Remove the everything that are outside the screen.

    :param group:
    :return:
    """
    for sprite in group:
        if not sprite.alive:
            group.remove(sprite)


def init_group():
    player = pygame.sprite.GroupSingle(Player())
    boss = pygame.sprite.Group()
    player_bullets = pygame.sprite.Group()
    boss_bullets = pygame.sprite.Group()
    scoreboard = pygame.sprite.GroupSingle(ScoreBoard())
    enemies = pygame.sprite.Group()
    boards = pygame.sprite.Group()
    props = pygame.sprite.Group()

    # Initialize the boards
    for i in range(Board.num):
        boards.add(Board((random.randint(0, WIDTH), random.randint(0, HEIGHT)), True))
    boards.add(Board((WIDTH / 2, HEIGHT * 2 / 3), False))

    return {'player': player, 'boss': boss, 'player_bullets': player_bullets, 'boss_bullets': boss_bullets,
            'scoreboard': scoreboard, 'enemies': enemies, 'boards': boards, 'props': props}


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Space Jump")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    background = pygame.image.load('images/background.jpg')
    end_interface = Interface(screen, type='end', images=END_IMAGES, blink_images_num=END_BLINK_IMAGES_NUM)
    start_interface = Interface(screen, type='start', images=START_IMAGES, blink_images_num=START_BLINK_IMAGES_NUM)
    boss_dead_time = time.time()
    clock = pygame.time.Clock()
    
    #load music
    pygame.mixer.music.load(r"sound_track.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.play(loops=-1)

    # Initialize the player, player_bullets, enemies, boards, props and scoreboard.
    groups = init_group()
    create_new(groups)

    while True:
        # Close the window of the game and end the program
        for event in pygame.event.get():
            if event.type == QUIT or pygame.key.get_pressed()[K_ESCAPE]:
                pygame.quit()
                sys.exit()

        clock.tick(FPS)
        pygame.display.flip()
        # The start page
        if start_interface.alive:
            screen.blit(start_interface.image, start_interface.rect)
            start_interface.update()
            if start_interface.alive == False:
                continue

        # If player is alive
        elif len(groups['player']) == 1:
            screen.blit(background, background.get_rect())

            # Draw all the objects
            for group in groups.values():
                group.draw(screen)

            # Record temporary number of objects
            temp_boards_num = len(groups['boards'])
            temp_enemies_num = len(groups['enemies'])
            temp_boss_num = len(groups['boss'])

            # Delete the boards or player_bullets off the screen and the dead enemies
            for group in groups.values():
                remove_dead(group)

            # Update all the objects
            groups['player'].update(pygame.key.get_pressed(), groups['boards'], groups['player_bullets'], groups['boss_bullets'], groups['enemies'], groups['props'])
            groups['boss'].update(groups['player_bullets'], groups['boss_bullets'])
            groups['player_bullets'].update()
            groups['boss_bullets'].update()
            groups['enemies'].update(groups['boards'], groups['player_bullets'])
            groups['props'].update(groups['boards'])
            groups['boards'].update()
            groups['scoreboard'].update([temp_boards_num - len(groups['boards']), (temp_enemies_num - len(groups['enemies'])) * 10,
                               (temp_boss_num - len(groups['boss'])) * 1000])

            # Boss is dead
            if temp_boss_num != len(groups['boss']):
                boss_dead_time = time.time()

            # Create new boards, enemy and boss if the number of them is not enough
            create_new(groups)
        else:  # If player is dead, display the ending interface
            screen.blit(end_interface.image, end_interface.rect)
            end_interface.update()
            groups['scoreboard'].draw(screen)
            groups['scoreboard'].update([])
            # If the click restart, reinitialize the game.
            if end_interface.alive == False:
                # Clear the screen
                for group in groups.values():
                    group.empty()
                # Initialize the game
                groups = init_group()
                boss_dead_time = time.time()
                end_interface.alive = True

