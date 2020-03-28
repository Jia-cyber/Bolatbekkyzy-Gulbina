import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
white = (255,255,255)
screen.fill(white)
for point in range(0,256,10): 
    pygame.draw.line(screen, (0,point,point), (0,0), (640, point), 1)
    pygame.draw.line(screen, (point,0,point), (0,0), (point, 480), 1)

clock = pygame.time.Clock()

running = True 

while running:
    milliseconds = clock.tick(30) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False   
   
    pygame.display.flip()

pygame.display.update()