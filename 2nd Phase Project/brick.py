import pygame
import random

POOL = [
    (220, 20, 60),    # Crimson
    (70, 130, 180),   # Steel Blue
    (205, 92, 92),    # Indian Red
    (153, 50, 204),   # Dark Orchid
    (250, 128, 114),  # Salmon
    (135, 206, 235),  # Sky Blue
    (255, 182, 193),  # Light Pink
    (152, 251, 152),  # Pale Green
    (218, 112, 214),  # Orchid
    (255, 191, 0),    # Amber Yellow
    (0, 184, 148),    # Mint (Light)
    (108, 92, 231),   # Light Purple (Medium-Light)
    (142, 68, 173),   # Deep Purple (Dark)
    (253, 203, 110),  # Soft Yellow (Light)
]



class Brick(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # randomizing brick color
        color = random.choice(POOL)
        
        self.image = pygame.Surface([100, 20], pygame.SRCALPHA)
        self.create_brick(color)
        self.rect = self.image.get_rect()
        
    def create_brick(self, color):
        #brick shape
        pygame.draw.rect(self.image, color, [2, 2, 96, 16], border_radius=5)
        
        # Adding a gradient effect for aesthetics
        dark_color = (max(color[0] - 30, 0), max(color[1] - 30, 0), max(color[2] - 30, 0))
        pygame.draw.rect(self.image, dark_color, [2, 2, 96, 8], border_radius=5)

        # outine to make it sharp
        outline_color = (max(color[0] - 50, 0), max(color[1] - 50, 0), max(color[2] - 50, 0))
        pygame.draw.rect(self.image, outline_color, [0, 0, 100, 20], width=2, border_radius=5)
