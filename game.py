# Main Script for Cult Escape, currently contains class definitions and main execution.
import pygame
import sys
from spritesheet import SpriteSheet

# Class for the main game initialization and game loop
class Game:
    # Initializing class with its window size and border we want to use down the line.
    def __init__(self, width=800, height=600, border=20):
        pygame.init()
        self.window_size = (width, height)
        self.border = border
        self.screen = pygame.display.set_mode(self.window_size)
        self.screen_rectangle = self.screen.get_rect()
        self.clock = pygame.time.Clock()

    # This is the runtime game loop
    def gameloop(self, sprite_sheet):
        y_movement = (False, False)
        x_movement = (False, False)
        user_speed = 3
        while True:
            # Here we are checking for events, such as user exiting page, clicking something, etc
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

            # Equations that handle any movement in x or y direction
            x_move = -x_movement[1] + x_movement[0]
            y_move = -y_movement[0] + y_movement[1]

            # All the screen updates
            # if sprite_sheet.rect[0] < self.screen_rectangle[2]:
            right_edge = self.screen_rectangle[2] - self.border
            bottom_edge = self.screen_rectangle[3] - self.border

            # border for x-axis gameplay
            if sprite_sheet.rect.right < right_edge and sprite_sheet.rect.left > self.border:
                sprite_sheet.rect[0] += x_move * user_speed
            elif sprite_sheet.rect.right >= right_edge:
                sprite_sheet.rect[0] -= 1
            else:
                sprite_sheet.rect[0] += 1

            # border for y-axis gameplay
            if sprite_sheet.rect.bottom < bottom_edge and sprite_sheet.rect.top > self.border:
                sprite_sheet.rect[1] += y_move * user_speed
            elif sprite_sheet.rect.bottom >= bottom_edge:
                sprite_sheet.rect[1] -= 1
            else:
                sprite_sheet.rect[1] += 1

            # Refreshing the screen
            pygame.draw.rect(self.screen, (105, 106, 106), self.screen_rectangle, self.border)
            pygame.draw.rect(self.screen, (37, 103, 76), (self.border, self.border,
                                                           self.screen_rectangle[2] - 2 * self.border,
                                                           self.screen_rectangle[3] - 2 * self.border))
            self.screen.blit(sprite_sheet.surf, sprite_sheet.rect)
            pygame.display.flip()
            self.clock.tick(60)

# main execution
my_game = Game(1000, 600, 50)
sprite_sheet = SpriteSheet('images/entities/cultsman-spritesheet.png', 5, my_game.screen)
my_game.gameloop(sprite_sheet)
