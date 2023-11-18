# Main Script for Cult Escape, currently contains class definitions and main execution.
import pygame
import sys


class Game:
    def __init__(self, width=800, height=600, border=20):
        pygame.init()
        self.window_size = (width, height)
        self.border = border
        self.screen = pygame.display.set_mode(self.window_size)
        self.clock = pygame.time.Clock()

        # Surface declarations
        self.player_surface = pygame.image.load('images/entities/cultist.png').convert_alpha()
        self.player_surface = pygame.transform.scale(self.player_surface, (100, 100))
        pygame.Surface.set_colorkey(self.player_surface,  (0, 0, 0))

        # Rectangle declarations
        self.screen_rectangle = self.screen.get_rect()
        self.player_rectangle = self.player_surface.get_rect(midtop=(width/2, height/8))

        # Scaling

    def gameloop(self):
        y_movement = (False, False)
        x_movement = (False, False)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        y_movement = (True, False)
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        y_movement = (False, True)
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        x_movement = (False, True)
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        x_movement = (True, False)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        y_movement = (False, False)
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        y_movement = (False, False)
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        x_movement = (False, False)
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        x_movement = (False, False)
            y_equation = -y_movement[0] + y_movement[1]
            x_equation = -x_movement[1] + x_movement[0]
            # All the screen updates
            self.player_rectangle[0] += x_equation
            self.player_rectangle[1] += y_equation
            pygame.draw.rect(self.screen, (105, 106, 106), self.screen_rectangle, self.border)
            pygame.draw.rect(self.screen, (37, 103, 76), (self.border, self.border,
                                                          self.screen_rectangle[2] - 2 * self.border,
                                                          self.screen_rectangle[3] - 2 * self.border))
            self.screen.blit(self.player_surface, self.player_rectangle)
            pygame.display.flip()
            self.clock.tick(60)


my_game = Game(1000, 600)
my_game.gameloop()
