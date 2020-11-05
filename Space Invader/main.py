#This is the initalization and startup for pygame
#Setting some global variables
import pygame
pygame.init()
winHeight=720
winWidth = 720
win = pygame.display.set_mode((winHeight,winWidth),display=1)
count = 0
pygame.display.set_caption("Space Invader")
clock = pygame.time.Clock()
class game():
    def input(self,keys,player):
        global winHeight,winWidth,count
        if (keys[pygame.K_a] or keys[pygame.K_LEFT])and player.x>(0):
            player.x-=player.vel
        elif (keys[pygame.K_d] or keys[pygame.K_RIGHT])and player.x<(winWidth-player.width):
            player.x+=player.vel
        elif(keys[pygame.K_SPACE]):
            count+=1
            print(count)
        return
    def __init__(self):
        run = True

        player = spaceship(300, 600, 80, 80)
        while run:
            clock.tick(60)
            keys = pygame.key.get_pressed()
            self.input(keys,player)
            self.redrawGame(win,player)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

    def redrawGame(self,win,player):
        win.blit(pygame.image.load('bg.png'), (0, 0))
        #man.draw(win)
        player.draw(win,player.x,player.y)
        pygame.display.update()
class spaceship(pygame.sprite.Sprite):
    def draw(self,win,x,y):
        self.x = x
        self.y =y
        #pygame.draw.rect(win,(255,0,0),(self.x,self.y,self.width,self.height))
        self.image = pygame.image.load('spaceship.png')
        self.rect = self.image.get_rect()
        win.blit(self.image,(self.x,self.y))
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7
        #self.image.fill((0,255,255))
class meteor():
    def __init__(self):
        print(1)
if __name__ == '__main__':
    mainGame = game()