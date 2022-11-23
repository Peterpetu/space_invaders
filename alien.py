import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load("images/alien.png").convert_alpha()
        self.rect = self.image.get_rect()
        
        self.rect.midtop = self.screen_rect.midtop 
        # self.rect.x = self.rect.width #60 pikseliä vasemmasta reunasta oikealle
        # self.rect.y = self.rect.height #58 pikseliä yläreunasta alas
        # (eli kuvan leveyden ja korkeuden verran (60x58) )
        self.x = float(self.rect.x)
        self.direction = 1        
        self.game=game

    def blit(self):
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        if self.rect.right >= self.screen_rect.right or self.rect.left <=0:
            return True

    def update(self):        
        if self.direction==1 and self.rect.right <= self.screen_rect.right:        
            self.x += self.game.settings.alien_speed
        elif self.direction==-1 and self.rect.left >=self.screen_rect.left:            
             self.x -= self.game.settings.alien_speed        

        self.rect.x = self.x


