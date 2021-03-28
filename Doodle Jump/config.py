# The configuration of the game
# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
SAND = (244, 164, 96)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)

# Screen
WIDTH = 600
HEIGHT = 800
FPS = 30

# Board
BOARD_WIDTH = 60
BOARD_HEIGHT = 10
BOARD_NUM = 30
BOARD_VERTICAL_SPEED = 3

# Score board
INITIAL_SCORE = 0

# Bullet
BULLET_WIDTH = 20
BULLET_HEIGHT = 20
BULLET_SPEED = 12

# Player
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_VERTICAL_SPEED = 18
PLAYER_HORIZONTAL_SPEED = 7
PLAYER_SHOOT_PERIOD = 0.3
PLAYER_DIZZY_PERIOD = 5
PLAYER_FLYING_PERIOD = 5

# Enemy
ENEMY_PROB = 10
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 40

# Prop
PROPS_PROB = 10 
POISON_WIDTH = 30
POISON_HEIGHT = 30
JETPACK_WIDTH = 30
JETPACK_HEIGHT = 30
SHIELD_WIDTH = 30
SHIELD_HEIGHT = 30

# Boss
BOSS_HP = 10
BOSS_WIDTH = 300
BOSS_HEIGHT = 50
BOSS_HORIZONTAL_SPEED = 2
BOSS_REFRESH_PERIOD = 20

# Interface
RESTART_BUTTON_WIDTH = int(2.25*70)
RESTART_BUTTON_HEIGHT = 1*70
RESTART_BUTTON_TOP = HEIGHT*2//3
RESTART_BUTTON_LEFT = WIDTH//5
RESTART_BUTTON_BOTTOM = RESTART_BUTTON_HEIGHT + RESTART_BUTTON_TOP
RESTART_BUTTON_RIGHT = RESTART_BUTTON_LEFT + RESTART_BUTTON_WIDTH
RESTART_BUTTON_CENTERX = RESTART_BUTTON_WIDTH//2 + RESTART_BUTTON_LEFT
RESTART_BUTTON_CENTERY = RESTART_BUTTON_HEIGHT//2 + RESTART_BUTTON_TOP

QUIT_BUTTON_WIDTH = int(2.25*50)
QUIT_BUTTON_HEIGHT = 1*50
QUIT_BUTTON_TOP = RESTART_BUTTON_TOP+10
QUIT_BUTTON_LEFT = RESTART_BUTTON_LEFT+250
QUIT_BUTTON_BOTTOM = QUIT_BUTTON_HEIGHT + QUIT_BUTTON_TOP
QUIT_BUTTON_RIGHT = QUIT_BUTTON_LEFT + QUIT_BUTTON_WIDTH
QUIT_BUTTON_CENTERX = QUIT_BUTTON_WIDTH//2 + QUIT_BUTTON_LEFT
QUIT_BUTTON_CENTERY = QUIT_BUTTON_HEIGHT//2 + QUIT_BUTTON_TOP

START_BUTTON_WIDTH = int(2.25*50)
START_BUTTON_HEIGHT = 1*50
START_BUTTON_TOP = HEIGHT//2
START_BUTTON_LEFT = WIDTH*5//8
START_BUTTON_BOTTOM = RESTART_BUTTON_HEIGHT + RESTART_BUTTON_TOP
START_BUTTON_RIGHT = RESTART_BUTTON_LEFT + RESTART_BUTTON_WIDTH
START_BUTTON_CENTERX = START_BUTTON_WIDTH//2 + START_BUTTON_LEFT
START_BUTTON_CENTERY = START_BUTTON_HEIGHT//2 + START_BUTTON_TOP

# The quit image must be called as "quit.png" in order to use the quit function in the interface
END_IMAGES = {'gameover.jpg' : ((WIDTH, HEIGHT), (0,0)),
              'replay.png' : ((RESTART_BUTTON_WIDTH, RESTART_BUTTON_HEIGHT), (RESTART_BUTTON_CENTERX, RESTART_BUTTON_CENTERY)),
              'quit.png' : ((QUIT_BUTTON_WIDTH, QUIT_BUTTON_HEIGHT), (QUIT_BUTTON_CENTERX, QUIT_BUTTON_CENTERY)),
              'replaywhite.png' : ((RESTART_BUTTON_WIDTH, RESTART_BUTTON_HEIGHT), (RESTART_BUTTON_CENTERX, RESTART_BUTTON_CENTERY)),
              'quitwhite.png' : ((QUIT_BUTTON_WIDTH, QUIT_BUTTON_HEIGHT), (QUIT_BUTTON_CENTERX, QUIT_BUTTON_CENTERY))
              }
END_BLINK_IMAGES_NUM = 2

START_IMAGES = {'start.png': ((WIDTH, HEIGHT), (0,0)),
                'play.png': ((START_BUTTON_WIDTH, START_BUTTON_HEIGHT), (START_BUTTON_CENTERX, START_BUTTON_CENTERY)),
                'playwhite.png': ((START_BUTTON_WIDTH, START_BUTTON_HEIGHT), (START_BUTTON_CENTERX, START_BUTTON_CENTERY))
                }
START_BLINK_IMAGES_NUM = 1