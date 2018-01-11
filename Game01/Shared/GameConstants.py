import os


class GameConstants:
    SCREEN_SIZE = [800, 600]
    BRICK_SIZE = [100, 30]
    BALL_SIZE = [16, 16]
    PAD_SIZE = [139, 13]
    BALL_SPEED = 3
    HIT_POINTS = 100
    START_LIVES = 5

    SPRITE_BALL = os.path.join("Assets", "ball.png")
    SPRITE_BRICK = os.path.join("Assets", "standard.png")
    SPRITE_SPEED_BRICK = os.path.join("Assets", "speed.png")
    SPRITE_LIFE_BRICK = os.path.join("Assets", "life.png")
    SPRITE_PAD = os.path.join("Assets", "pad.png")

    #SOUND_HIT_WALL = os.path.join("Assets", )
