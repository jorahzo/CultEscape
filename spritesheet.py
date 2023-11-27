import pygame


class SpriteSheet:
    # Constructor
    def __init__(self, img_to_load, scale, screen):
        # Image surface declarations
        self.img_to_load = img_to_load
        self.scale = scale
        self.surf = pygame.image.load(self.img_to_load).convert_alpha()
        self.surf = pygame.transform.scale(self.surf,
        (self.surf.get_width() * self.scale, self.surf.get_height() * self.scale))
        self.surf.set_colorkey((0, 0, 0))
        # Image rectangle declaration
        self.rect = self.surf.get_rect(midtop=(screen.get_width()/2,
                                               screen.get_height()/8))

    # method to provide user with a frame from the spritesheet
    def get_img(self, frame, width, height):
        """This method will parse the Sprite Sheet for a given frame
        and draw it to the passed screen"""
        self.surf.blit(self.surf, (0, 0), ((frame * width), 0, width, height))
        return self.surf

