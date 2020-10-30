#This is the initalization and startup for pygame
#Setting some global variables
import pygame
pygame.init()
win = pygame.display.set_mode((720,720))
pygame.display.set_caption("Space Invader")
clock = pygame.time.Clock()

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
class game():
    def __init__(self):
        run = True

        player = spaceship(50, 100, 50, 100)
        while run:
            keys = pygame.key.get_pressed()
            clock.tick(60)
            self.redrawGame(win,player)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

    def redrawGame(self,win,player):
        win.blit(pygame.image.load('bg.png'), (0, 0))
        #man.draw(win)
        player.draw(win)
        pygame.display.update()
class spaceship():
    def draw(self,win):
        pygame.draw.rect(win,(255,0,0),(50,100,50,100))
    def __init__(self,x,y,width,height):
        print(1)
class meteor():
    def __init__(self):
        print(1)
if __name__ == '__main__':
    mainGame = game()