import pygame
import random

class Bolas:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Bolas")

        # Variable de player = pelota
        self.player = Ball(400, 300, 30 )
        self.player2 = Ball(200, 200, 30 , (30, 5, 6))

        self.metronomo = pygame.time.Clock()

    def main_loop(self):
        game_over = False
        dy = 10 # Delta de y que va a ser 10
        dx = 10
        ay = 10
        ax = 10
        while game_over == False:
            self.metronomo.tick(30)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_over = True

            self.screen.fill ((0, 255, 0))
            
            self.player.draw(self.screen)
            self.player2.draw(self.screen)            
            self.player.x += dx
            self.player.y += dy
            self.player2.x += ax
            self.player2.y += ay

            if self.player.y >= 600 - self.player.radio or self.player.y <= 30:
                dy = -dy
            
            if self.player.x >= 800 - self.player.radio or self.player.x <= 30:
                dx = -dx
          
            if self.player2.y >= 600 - self.player2.radio or self.player2.y <= 30:
                ay = -ay
            
            if self.player2.x >= 800 - self.player2.radio or self.player2.x <= 30:
                ax = -ax

            if self.player.x + self.player.radio == self.player2.x + self.player2.radio and self.player2.y + self.player2.radio == self.player.y + self.player.radio:
                dy = 60
                dx = 60
                ay = 80
                ax = 80


            pygame.display.flip()

class Ball:
    def __init__(self, x, y, radio, color = (255, 255, 255)):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radio)
        

if __name__ == "__main__":
    bola = Bolas()
    bola.main_loop()