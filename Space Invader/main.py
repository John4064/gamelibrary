#This is the initalization and startup for pygame
#Setting some global variables
import pygame
pygame.init()
winHeight=720
winWidth = 720
win = pygame.display.set_mode((winHeight,winWidth),display=1)
pygame.display.set_caption("Space Invader")
temp = pygame.time.get_ticks()
class game():
    #Convert input to player

    def __init__(self):
        run = True
        player = spaceship(300, 600, 80, 80)
        self.clock = pygame.time.Clock()
        lasers = laser(200,200,8)
        while run:
            self.clock.tick(60)
            keys = pygame.key.get_pressed()
            player.input(keys,game)
            self.redrawGame(win,player,lasers)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

    def redrawGame(self,win,player,laser):
        win.blit(pygame.image.load('bg.png'), (0, 0))
        #man.draw(win)
        #Update this in morning
        laser.draw(win)
        player.draw(win,player.x,player.y)
        pygame.display.update()
class laser(pygame.sprite.Sprite):
    def draw(self,win):
        pygame.draw.circle(win, (255,255,12), (self.x,self.y), 10)
    def __init__(self,x,y,vel):
        self.x =x
        self.y =y
        #vel = Velocity
        self.vel =vel

class spaceship(pygame.sprite.Sprite):
    def input(self,keys,game):
        global winHeight,winWidth,temp
        if (keys[pygame.K_a] or keys[pygame.K_LEFT])and self.x>(0):
            self.x-=self.vel
        elif (keys[pygame.K_d] or keys[pygame.K_RIGHT])and self.x<(winWidth-self.width):
            self.x+=self.vel
        elif(keys[pygame.K_SPACE] and pygame.time.get_ticks()>temp+500):
            temp = pygame.time.get_ticks()
            print(temp)
        return
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