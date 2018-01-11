import pygame
from Game01.Scenes.Scene import Scene
from Game01.Shared.GameConstants import *


class PlayingGameScene(Scene):
    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)

    def render(self):
        super(PlayingGameScene, self).render()

        game = self.getGame()
        pad = game.getPad()
        for ball in game.getBalls():

            for brick in game.getLevel().getBricks():
                if ball.intersects(brick) and not brick.isDestroyed():
                    brick.hit()
                    ball.changeDirection(brick)
                    break

            if ball.intersects(pad):
                ball.changeDirection(pad)

            ball.updatePosition()

            game.screen.blit(ball.getSprite(), ball.getPosition())

        for brick in game.getLevel().getBricks():
            if not brick.isDestroyed():
                game.screen.blit(brick.getSprite(), brick.getPosition())

        pad.setPosition((pygame.mouse.get_pos()[0], pad.getPosition()[1]))
        game.screen.blit(pad.getSprite(), pad.getPosition())

        self.clearText()
        self.addText("Your score: " + str(game.getScore()),
                     x = 0,
                     y = GameConstants.SCREEN_SIZE[1] - 60, size = 30)

    def handleEvents(self, events):
        super(PlayingGameScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for ball in self.getGame().getBalls():
                    ball.setMotion(1)