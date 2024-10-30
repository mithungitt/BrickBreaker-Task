import pygame
import random

RED = (255, 50, 50)
DARK_RED = (250, 0, 0)
LIGHT_RED = (255, 150, 150) 
OUTLINE_COLOR = (100, 0, 0)
LENGTH = 800
HEIGHT = 700

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Create a larger ball surface with transparency
        self.image = pygame.Surface([30, 30], pygame.SRCALPHA)
        self.create_ball()
        self.rect = self.image.get_rect()
        
        # Initialize ball movement
        self.initial_speed = 1  # Starting speed
        self.current_speed = self.initial_speed  # Current speed that changes each round
        self.velocity = self.generate_initial_velocity()
        self.speed_increment = 0.1
    
    def create_ball(self):
        # shape of sphere
        pygame.draw.circle(self.image, RED, (15, 15), 15)  
        pygame.draw.circle(self.image, DARK_RED, (15, 15), 13)

        # light spot
        pygame.draw.circle(self.image, LIGHT_RED, (10, 10), 6)

        # outline
        pygame.draw.circle(self.image, OUTLINE_COLOR, (15, 15), 15, width=2)
    
    # Generate a non-zero x and y velocity to ensure diagonal movement
    def generate_initial_velocity(self):        
        while True:
            x_velocity = random.choice([-1, 1]) * self.current_speed
            y_velocity = random.choice([1, 2]) * self.current_speed  # ensures downward movement
            if x_velocity != 0 and y_velocity != 0:
                return [x_velocity, y_velocity]
        
    def reset(self):
        # Sets the initial position and velocity of the ball
        self.rect.x = LENGTH / 2
        self.rect.y = HEIGHT / 2
        self.velocity = self.generate_initial_velocity()
        
    def game_over(self):
        # Resets the speed when the game is over
        self.current_speed = self.initial_speed
        self.reset()
                
    def initialPosition(self):
        self.rect.x = LENGTH / 2
        self.rect.y = HEIGHT / 2
            
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
            
    def bounceX(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[0] += self.speed_increment if self.velocity[0] > 0 else -self.speed_increment
         
    def bounceY(self):
        self.velocity[1] = -self.velocity[1]
        self.velocity[1] += self.speed_increment if self.velocity[1] > 0 else -self.speed_increment
