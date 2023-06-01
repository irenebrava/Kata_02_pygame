import pygame


class Ball:
    def __init__(self,x,y,radio, color, dx, dy):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.dx = dx
        self.dy = dy
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

            self.player.x += self.player.dx
            self.player.y += self.player.dy

            if self.player.x >= 800 - self.player.radio or self.player.x <= self.player.radio:
                self.player.dx = -self.player.dx
            if self.player.y >= 600 - self.player.radio or self.player.y <= self.player.radio:
                self.player.dy = -self.player.dy


            self.player1.draw(self.screen)

            self.player1.x += self.player1.dx
            self.player1.y += self.player1.dy

            if self.player1.x >= 800 - self.player1.radio or self.player1.x <= self.player1.radio:
                self.player1.dx = -self.player1.dx
            if self.player1.y >= 600 - self.player1.radio or self.player1.y <= self.player1.radio:
                self.player1.dy = -self.player1.dy
            
            pygame.display.flip()

    
if __name__ == "__main__":
    bola = Bolas ()
    bola.main_loop()
