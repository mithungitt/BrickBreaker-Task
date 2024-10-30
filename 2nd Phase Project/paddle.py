import pygame

# Color definitions
BLACK = (0, 0, 0)
DARK_GREY = (50, 50, 50)
LIGHT_GREY = (200, 200, 200)
OUTLINE_COLOR = (100, 100, 100)

LENGTH = 800
HEIGHT = 700

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Create the main paddle surface with transparency (alpha)
        self.image = pygame.Surface([120, 20], pygame.SRCALPHA)
        self.create_paddle()
        self.rect = self.image.get_rect()
        self.reset()
        
    def create_paddle(self):
        # Draw the base paddle shape with rounded corners
        pygame.draw.rect(self.image, LIGHT_GREY, [2, 2, 116, 16], border_radius=8)
        
        # Draw a gradient effect (a second rectangle with a slightly darker color on the top half)
        pygame.draw.rect(self.image, DARK_GREY, [2, 2, 116, 8], border_radius=8)

        # Draw a border around the paddle
        pygame.draw.rect(self.image, OUTLINE_COLOR, [0, 0, 120, 20], width=2, border_radius=8)

    def reset(self):
        # Sets the initial position of the paddle
        self.rect.x = (LENGTH / 2) - 60
        self.rect.y = HEIGHT - 60

    def move_right(self):
        self.rect.x += 5
        if self.rect.x >= (LENGTH - 120):
            self.rect.x = LENGTH - 120

    def move_left(self):
        self.rect.x -= 5
        if self.rect.x < 0:
            self.rect.x = 0
