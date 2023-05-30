import pygame 
pygame.init()
pantalla = pygame.display.set_mode((800,600))
pygame.display.set_caption("Hola mundo")

metronomo = pygame.time.Clock()

game_over = False
azul = 0
while game_over == False:
    ms = metronomo.tick(60)
    print(ms)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True
    
    azul = azul + 1
    if azul > 255:
        azul = 0 

    pantalla.fill((0,0,azul))
    pygame.display.flip()