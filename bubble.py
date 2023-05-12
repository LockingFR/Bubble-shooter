import pygame as pg

pg.init()
WIDTH, HEIGHT = pg.display.get_desktop_sizes()[0]


class Boules(pg.sprite.Sprite):

    def __init__(self, x, y, color, type_bubble):
        """pg.sprite.Sprite.__init__(self)

        dico_image = {
            'red': 'red.png',
            'orange': 'orange.png',
            'yellow': 'yellow.png',
            'green': 'green.png',
            'blue': 'blue.png',
            'purple': 'purple.png',
            'bomb': 'bomb.png',
            'rocket': 'rocket.png'
        }
        self.coordonnees = (x, y)
        self.type = type_bubble
        if type == 'bubble':
            self.image = dico_image[color]
        elif type == 'bomb':
            self.image = dico_image['bomb']
        elif type == 'rocket':
            self.image = dico_image['rocket']

        self.v = pg.math.Vector2(0, 0)"""

        print("c tou goud")

    def lancer(self, screen):
        self.x, self.y = (WIDTH / 2), HEIGHT - 20
        screen.blit(self.image)
