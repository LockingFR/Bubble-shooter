import pygame

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((2400, 1080))

continuer = True

while continuer:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE :
                continuer = False
    screen.fill((255, 255, 255))
    pygame.display.flip()
        
        
pygame.quit()

