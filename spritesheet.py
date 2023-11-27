import pygame


class SpriteSheet:
    def __init__(self, img_to_load, scale, screen):
        # Image surface declarations
        self.img_to_load = img_to_load
        self.surf = pygame.image.load(self.img_to_load).convert_alpha()
        self.surf = pygame.transform.scale(self.surf,
        (self.surf.get_width() * scale, self.surf.get_height() * scale))
        self.surf.set_colorkey((0, 0, 0))
        # Image rectangle declaration
        self.rect = self.surf.get_rect(midtop=(screen.get_width()/2,
                                               screen.get_height()/8))

