import pygame
from bullet import Bullet
from explosion import Explosion

class Ship:
    def __init__(self,game):     
        # haetaan pääohjelman screen-muuttuja, asetaan olion käyttöön   
        self.screen = game.screen        
        #screen_rect-muuttujaan haetaan pääohjelman screen-muuttujan
        # dimensiot (mahdollistaa mm. midbottom-käytön)
        self.screen_rect = game.screen.get_rect()
        # haetaan image-muuttujaan kuva
        # TODO: laita try:n "taakse"!
        self.image = pygame.image.load('images/ship.png').convert_alpha()
        # rect-muuttujaan asetetaan kuvan dimensiot
        self.rect = self.image.get_rect()
        #asetetaan olion suorakulmio keskelle pääohjelman ruudun alaosaa         
        self.rect.midbottom = self.screen_rect.midbottom

        #haetaan pääohjelmasta settings-olio
        self.settings = game.settings

        #haetaan pääohjelma metodeille viemistä varten
        self.game = game

        self.bullets = pygame.sprite.Group()        

        #asetetaan liikkuminen aluksi Falseksi
        self.moving_right = False
        self.moving_left = False

        #asetetaan desimaaliluku liikkumiselle
        self.x = float(self.rect.x) # 3 -> 3.0

    def fire_bullet(self):        
        if len(self.bullets) < self.settings.bullets_allowed:        
            new_bullet = Bullet(self, self.game)
            self.bullets.add(new_bullet)#lisätään new_bullets bullets-spritegrouppiin         
            self.game.stats.bullets_fired += 1      
        

    def update_bullets(self):
        self.bullets.update() #kutsuu kaikkien 
                        #bullet-instanssien update-metodia
        for b in self.bullets.copy():
            if b.rect.bottom <= 0: #osuu yläreunaan
                self.bullets.remove(b)

        # bulletin osuminen
        collision = pygame.sprite.groupcollide(self.bullets,self.game.aliens,True,True)
        if collision: # ==True
            for aliens in collision.values(): #kaikki alienit mihin osuttiin
                for alien in aliens:                    
                    explosion = Explosion(self.game)
                    explosion.set_explosion_center_and_object(alien.rect.center,'alien')
                    self.game.explosions.add(explosion)
                    self.game.stats.score += 1
            #self.game.create_alien()


    def blit(self): #blittaus on kuvien piirtämistä
        #piirretään kuva, 1.parametri on kuva, toinen on dimensio
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed           
        if self.moving_left and self.rect.left > 0: # self.screen_rect.left
            self.x -= self.settings.ship_speed

        if pygame.sprite.spritecollideany(self,self.game.aliens):
            print("CRASH")

        #napataan talteen pelkkä kokonaisluku desimaaliluvusta
        self.rect.x = self.x