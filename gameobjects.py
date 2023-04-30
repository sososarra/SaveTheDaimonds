
import pygame,random

class GameObject(pygame.sprite.Sprite):
    def __init__(self,x,y,img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()  
        self.rect.center = (x,y)

        self.rand_xd = random.choice([-1,1])
        self.rand_yd = random.choice([-1,1])

    def update(self):
       self.rect = self.rect.move(self.rand_xd*self.speed,self.rand_yd*self.speed)


class Diamond(GameObject):
    def __init__(self,screen_rect):
        rand_x = random.randint(100,screen_rect.width - 100) 
        rand_y = random.randint(100,screen_rect.height - 100)
        super().__init__(rand_x,rand_y,"diamond.png" )
        self.speed = 5
        self.status = "no"
    def update(self,screen_rect):
        self.rect = self.rect.move(self.rand_xd*self.speed,self.rand_yd*self.speed)

        if self.rect.left < 150 and self.rand_xd < 0 or self.rect.right > screen_rect.width - 150 and self.rand_xd > 0:
            self.rand_xd = -self.rand_xd
        if self.rect.top < 0 or self.rect.bottom > screen_rect.height:
            self.rand_yd =- self.rand_yd

class panelDiamond(GameObject):
    def __init__(self, screen_rect):
        rand_x =random.randint(screen_rect.left + 20, screen_rect.right - 20)
        rand_y = random.randint(screen_rect.top + 20, screen_rect.bottom - 20)
        super().__init__(rand_x, rand_y, "diamond.png")

class Recte():
    def __init__(self, l,t,w,h):
        self.rect = pygame.Rect(l, t, w, h)
        self.image = pygame.Surface((w, h))
    def drawRect(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)  
    def draws(self,diamond_image):
        x = random.randint(0, 20)
        y = random.randint(0, 600)
        self.image.blit(diamond_image, (x,y)) 
          
class Spaceship(GameObject):
    def __init__(self, screen_rect):
        super().__init__(screen_rect.centerx, screen_rect.centery, 'spaceship.png')
        self.speed = 2
        self.status = "no"

    def update(self,screen_rect):
        # Move the spaceship
        self.rect = self.rect.move(self.rand_xd*self.speed, self.rand_yd*self.speed)
        
        # Check if spaceship hits the edges of the panel and update direction accordingly
        if self.rect.left < 150 or self.rect.right > screen_rect.width - 150:
            self.rand_xd = -self.rand_xd
        if self.rect.top < 0 or self.rect.bottom > screen_rect.height:
            self.rand_yd = -self.rand_yd
    