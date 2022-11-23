import pygame
from pygame.sprite import Sprite

class Bullet(Sprite): #peritään Sprite-luokka

    total_number_of_bullets = 0 # class variable

    def __init__(self,ship,game):
        super().__init__() #kutsutaan Sprite-luokan __init__()
        self.screen = game.screen        
        self.rect = pygame.Rect(0,0,game.settings.bullet_width,
                                    game.settings.bullet_height)
                         #Rect(left, top, width, height)
        self.rect.midtop = ship.rect.midtop
        self.color = game.settings.bullet_color
        self.y = float(self.rect.y)
        self.settings = game.settings # updatea varten

        Bullet.total_number_of_bullets += 1
        print(Bullet.total_number_of_bullets)
        
    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        

