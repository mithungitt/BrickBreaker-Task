import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick

#to start
pygame.init()

#Organising the Display for Game Window
LENGTH= 800
HEIGHT= 700

screen = pygame.display.set_mode((LENGTH,HEIGHT))
pygame.display.set_caption('The Breaker Of Bricks')

background_image = pygame.image.load("background.jpg")  # Replace with your image path
background_image = pygame.transform.scale(background_image, (LENGTH, HEIGHT))

# Attributes for Various Components(later on discarded during UI adjustment)
RED= (255,0,0)
WHITE=(250,250,250)
BLACK= (0,0,0)
GREEN=(0,255,0)
BLUE= (0,0,255)
GRAY= (128,128,128)

#initializing the paddle
paddle=Paddle()
paddle.rect.x = (LENGTH/2)-60   #initial x coord
paddle.rect.y = (HEIGHT)-60     #initial y coord

#initializing the ball
ball = Ball()
ball.initialPosition()

#sprite groups(here we add elements one by one)
allsprites=pygame.sprite.Group()
allsprites.add(paddle)
allsprites.add(ball)

#group of bricks
allbricks = pygame.sprite.Group()

#instantiate bricks
def inst_bricks(c,r):
    for i in range(c):
        for j in range(r):
            brick= Brick()
            brick.rect.x=20 + i*110
            brick.rect.y=20 + j*30
            allbricks.add(brick)
            allsprites.add(brick)
        
inst_bricks(7,8)

#regenarating bricks after every round(3lives)
def removeBricks():
    for brick in allbricks:
        brick.kill()
        
#sounds for various events
brickbreaking=pygame.mixer.Sound('brick-dropped-on-other-bricks-14722.mp3')
paddletapping=pygame.mixer.Sound('tennis-ball-hit-151257.mp3')
losingTheBall=pygame.mixer.Sound('fail-144746.mp3')
gameOver=pygame.mixer.Sound('game-over-arcade-6435.mp3')
game_over_sound_played = False
victoryTheme=pygame.mixer.Sound('brass-fanfare-with-timpani-and-winchimes-reverberated-146260.mp3')
victory_sound_played = False

        
#running loop/MAIN loop
score=0
lives=3

start=False
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False 
            
    # setting the background image
    screen.blit(background_image, (0, 0))
    
    # initial message to start game
    if not start and lives > 0:
        # main message 
        title_font = pygame.font.Font(None, 80)  
        title_text = title_font.render("Ready or Not?", True, (200,0,15))  
        title_rect = title_text.get_rect(center=(LENGTH // 2 +13, HEIGHT // 2 + 94))
        
        # Shadow for the main message
        shadow_text = title_font.render("Ready or Not?", True, (0, 0, 0))  
        shadow_rect = shadow_text.get_rect(center=(LENGTH // 2 +17 , HEIGHT // 2 + 97))
        
        # blinking message
        subtitle_font = pygame.font.Font(None, 40) 
        subtitle_text = subtitle_font.render("[press space to start]", True, (255, 185, 0))
        subtitle_rect = subtitle_text.get_rect(center=(LENGTH // 2 + 5, HEIGHT // 2 + 140))
        
        screen.blit(shadow_text, shadow_rect)
        screen.blit(title_text, title_rect)
        if pygame.time.get_ticks() % 2000 < 1500:
            screen.blit(subtitle_text, subtitle_rect)

        
    #moving the paddle with keys
    arrows =pygame.key.get_pressed()
    if arrows[pygame.K_RIGHT]:
        paddle.move_right()
    if arrows[pygame.K_LEFT]:
        paddle.move_left()
        
     # space bar is pressed to start or restart
    if arrows[pygame.K_SPACE]:
        start = True
        ball.reset()    # Reset the ball position and velocity
        paddle.reset()  # Reset the paddle position
        
    
    #score and lives
    font = pygame.font.Font(None,35)
    text = font.render(f'SCORE: {score}', 1, (0, 190, 60) )
    screen.blit(text, (20, HEIGHT-30))
        
    font = pygame.font.Font(None,35)
    text = font.render(f'LIVES: {lives}', 1, (230,40,60))
    screen.blit(text, (LENGTH-120, HEIGHT-30))
            
    if lives==0:
        
        if not game_over_sound_played:
            gameOver.play()  # game over music
            game_over_sound_played = True

        largeFont= pygame.font.Font(None, 80)
        smallFont =pygame.font.Font(None, 40)
        textColor1 =(150,0,24)
        textColor2= (255,140,0) 
        shadowColor = (0,0,0)
        highlightColor = (218, 112, 214)

        text_surface = largeFont.render("GAME OVER", True, shadowColor)
        screen.blit(text_surface, (238, 303))

        text_surface = largeFont.render("GAME OVER", True, textColor1)
        screen.blit(text_surface, (235, 300))

        text_surface = smallFont.render("(JUST TAKE THE L)", True, shadowColor)
        screen.blit(text_surface, (296, 390))

        text_surface = smallFont.render("(JUST TAKE THE L)", True, textColor2)
        screen.blit(text_surface, (293, 387))

        text_surface = smallFont.render("PRESS SPACE TO PLAY AGAIN", True, shadowColor)
        screen.blit(text_surface, (203, 431))

        text_surface = smallFont.render("PRESS SPACE TO PLAY AGAIN", True, highlightColor)
        screen.blit(text_surface, (200, 430))
        ball.game_over()
        
        
    if start:
        #update sprites
        allsprites.update()
        
        #reseting values
        if lives==0:
            lives=3
            score=0
            removeBricks()
            inst_bricks(7,8)
            game_over_sound_played = False 
            victory_sound_played = False
            
        #wall bouncing
        if ball.rect.right >= LENGTH or ball.rect.left <= 0:
            ball.bounceX()
        if ball.rect.top <= 0:
            ball.bounceY()
        if ball.rect.y >= HEIGHT - 40:
            losingTheBall.play()
            ball.initialPosition()
            lives-=1
            start = False
            
            
        #collisions from paddle(as they come after the bounce)
        if ball.rect.colliderect(paddle.rect):
            
            if abs(paddle.rect.top - ball.rect.bottom) < 9:
                ball.bounceY()
                paddletapping.play()
            if abs(paddle.rect.left - ball.rect.right) < 9 or abs(paddle.rect.right - ball.rect.left) <9:
                ball.bounceX()
                paddletapping.play()
                
        #collision with bricks
        ballWalls = pygame.sprite.spritecollide(ball,allbricks,False)
        for brick in ballWalls:
            ball.bounceY()
            brickbreaking.play()
            brick.kill()
            score+=1
            
            #victory condition message
            if len(allbricks)==0:
                if not victory_sound_played:
                    victoryTheme.play()
                    victory_sound_played = True

                # colors for message
                wonText = pygame.font.Font(None, 120)
                GOLD = (255, 215, 0)  
                shadowWon = (139, 69, 19)  
                outlineColor = (255, 255, 255) 

                # Render the main text surface and get its dimensions
                text_surface = wonText.render("YOU WON!!", True, GOLD)
                text_rect = text_surface.get_rect(center=(LENGTH // 2, HEIGHT // 2 - 50))  
                shadow_surface = wonText.render("YOU WON!!", True, shadowWon)
                shadow_rect = shadow_surface.get_rect(center=(text_rect.centerx + 5, text_rect.centery + 5))
                
                screen.blit(shadow_surface, shadow_rect)
                screen.blit(text_surface, text_rect)

                # sparkling outline effect from gpt
                for i in range(-2, 3):
                    for j in range(-2, 3):
                        if abs(i) == 2 or abs(j) == 2:
                            sparkle_surface = wonText.render("YOU WON!!", True, outlineColor)
                            sparkle_rect = sparkle_surface.get_rect(center=(text_rect.centerx + i, text_rect.centery + j))
                            screen.blit(sparkle_surface, sparkle_rect)

                subtitle_font = pygame.font.Font(None, 50)
                subtitle_text = subtitle_font.render("CONGRATULATIONS!", True, GOLD)
                subtitle_rect = subtitle_text.get_rect(center=(LENGTH // 2, HEIGHT // 2 + 60))
                screen.blit(subtitle_text, subtitle_rect)
                
                subtitle_font2 = pygame.font.Font(None, 40)
                second_line_text = subtitle_font2.render("YOU'VE MADE US ALL PROUD! (not really.)", True, (230,60,250))
                second_line_rect = second_line_text.get_rect(center=(LENGTH // 2, HEIGHT // 2 + 110))  
                screen.blit(second_line_text, second_line_rect)
                                
                pygame.display.update()  # Update and keep for 2seconds
                pygame.time.delay(2000)
                
                #reset the score and lives
                score = 0
                lives = 3
                
                ball.initialPosition()
                removeBricks()
                inst_bricks(7,8)
                start=False
                #reset the score and lives
                score = 0
                lives = 3
        
    #drawing a boundary on score and lives
    pygame.draw.line(screen, BLACK, [0, HEIGHT-35], [LENGTH, HEIGHT-35],5)
    
    #drawing sprites
    allsprites.draw(screen)
            
    #update the display
    pygame.display.update()
    #clock tick setting
    pygame.time.Clock().tick(650)  


#to close program
pygame.quit()