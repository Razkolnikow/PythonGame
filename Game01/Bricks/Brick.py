from Game01.Shared import GameObject
from Game01.Shared import GameConstants


class Brick(GameObject):
    def __init__(self, position, sprite, game):
        self.__game = game
        self.__hitPoints = GameConstants.HIT_POINTS
        self.__lives = 1

        super(Brick, self).__init__(position, GameConstants.BRICK_SIZE, sprite)

    def getGame(self):
        return self.__game

    def isDestroyed(self):
        return self.__lives <= 0

    def getHitPoints(self):
        return self.__hitPoints

    def hit(self):
        self.__lives -= 1

    def getHitSound(self):
        return GameConstants.SOUND_HIT_BRICK


