import pygame


class Ball:
    def __init__(self,x,y,radio, color=(255,255,255)):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
    def draw(self, surface ):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radio)


class Bolas:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Bolas")
        self.player =  Ball(400,300,20)
        self.player1 =  Ball(400,300,10)

        self.metronomo = pygame.time.Clock()
    
    def main_loop(self):
        game_over = False
        dy = 10
        dx = 15
        px=90
        py=46
        while game_over == False:
            self.metronomo.tick(20)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_over = True
            
            self.screen.fill((0,255,0))
            
            self.player.draw(self.screen)
            self.player.x += dx
            self.player.y += dy
            if self.player.x == 800 - self.player.radio:
                dx = -dx
            if self.player.y == 600 - self.player.radio:
                dy = -dy
            if self.player.x == 20:
                 dx = 16
            if self.player.y == 20:
                dy = 143
           
            self.player1.draw(self.screen)
            self.player1.x +=px 
            self.player1.y += py 
            if self.player1.x >= 800 - self.player1.radio:
                px = -px
            if self.player1.y >= 600 - self.player1.radio:
                py = -py
            if self.player1.x <= self.player1.radio:
                 px = 40
            if self.player1.y <= self.player1.radio:
                py = 40
           
           
            pygame.display.flip()
    
if __name__ == "__main__":
    bola = Bolas ()
    bola.main_loop()
