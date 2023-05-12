import pygame as pg
import bubble

pg.init()

WIDTH, HEIGHT = pg.display.get_desktop_sizes()[0]

clock = pg.time.Clock()

screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)

bubble1 = bubble.Boules(2,2,'red', 'bubble')
continuer = True

while continuer:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            continuer = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                continuer = False
    screen.fill((255, 255, 255))
    #bubble1.lancer(screen)
    pg.display.flip()

pg.quit()
