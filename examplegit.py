import pygame

pygame.init()

win = pygame.display.set_mode((640, 400))
background = pygame.Surface(win.get_size()).convert()  
background.fill((255,255,255)) # fill background white
win.blit(background, (0, 0))
playtime = 0.0

pygame.draw.circle(win, (0, 0, 255), (500, 400), 20)#blue ball
pygame.draw.rect(win, (0, 0, 0), (345, 345, 67, 45))
win.blit(background, (0, 0))

clock = pygame.time.Clock()
x = 250  
y = 250

run = True
while run:
    clock.tick(30)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.circle(win, (230, 50, 230), (200,50), 35)

    pygame.draw.rect(win, (64,128,255), (50,50,69,25))

    #pygame.draw.polygon(Surface, color, pointlist, width=0): return Rect
    pygame.draw.polygon(win, (0,180,0), ((250,100),(300,0),(350,50)))
    
    pygame.draw.arc(win, (125,125,125), (400,10,150,100), 0, 3.14)

    pygame.display.update()

pygame.quit()