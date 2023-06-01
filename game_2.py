import pygame
import random


class Ball:
    def __init__(self,x,y,radio, color, dx, dy):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.dx = dx
        self.dy = dy
    def rebotar_en_paredes(self, screen_width, screen_height):
        self.x += self.dx
        self.y += self.dy

        if self.x >= screen_width - self.radio or self.x <= self.radio:
            self.dx = -self.dx
        if self.y >= screen_height - self.radio or self.y <= self.radio:
            self.dy = -self.dy
    def draw(self, surface ):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radio)


class Bolas:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Bolas")
        self.player =  Ball(400,300,20,(255,255,255), 10,10)
        self.player1 =  Ball(700,100,10,(255,255,255),18,18)

        self.metronomo = pygame.time.Clock()
    
    def main_loop(self):
        game_over = False
        while game_over == False:
            self.metronomo.tick(20)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_over = True
            
            self.screen.fill((0,255,0))
            
            self.player.draw(self.screen)

            self.player.rebotar_en_paredes(self.screen.get_width(), self.screen.get_height())

            self.player1.draw(self.screen)

            self.player1.rebotar_en_paredes(self.screen.get_width(), self.screen.get_height())

            
            pygame.display.flip()

    
if __name__ == "__main__":
    bola = Bolas ()
    bola.main_loop()
