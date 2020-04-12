import pygame
import random  
pygame.init()

pygame.display.set_caption('Move the ball!')

screen = pygame.display.set_mode((640, 400))
screenrect = screen.get_rect()
background = pygame.Surface(screen.get_size()).convert()  
background.fill((255, 255, 255)) #fill background white
screen.blit(background, (0, 0))


ball_surface = pygame.Surface((50,50)) 
ball_surface.set_colorkey((0,0,0)) 
pygame.draw.circle(ball_surface, (255,0,0), (25,25),25) 
ball_surface = ball_surface.convert_alpha()        # for faster blitting. because transparency, use convert_alpha()
ballrect = ball_surface.get_rect()

clock = pygame.time.Clock()

FPS = 60
playtime = 0
x=25 
y=25
speedx = 20
speedy = 20
screen.blit(ball_surface, (x, y))  #blit the ball surface on the screen (on top of background)

running = True

left = False
right = False
down = False
up = False

while running:
    milliseconds = clock.tick(FPS)  # milliseconds passed since last frame
    seconds = milliseconds / 1000.0
    playtime += seconds
    #screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>0:
        x -= speedx
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x + ballrect.width < screenrect.width:
        x += speedx
        left = False
        right = True
    elif keys[pygame.K_DOWN] and y + ballrect.height < screenrect.height:
        y += speedy
        up = False
        down = True 
    elif keys[pygame.K_UP] and y>0:
        y -= speedy
        up = True
        down = False 

    # paint the ball    
    screen.blit(ball_surface, (x,y))

    pygame.display.update()

pygame.quit()