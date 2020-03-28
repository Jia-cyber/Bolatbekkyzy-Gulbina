import pygame 

pygame.init()


screen = pygame.display.set_mode((500, 500))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))

for point in range(0, 500, 20):
    line1 = pygame.draw.line(background, (0, 0, 255), (0, 0), (500, point))

for point in range(0, 500, 20):
    pygame.draw.line(background, (255, 0, 255), (0, 500), (point, 0))

for point in range(0, 500, 20):
    pygame.draw.line(background, (255, 0, 0), (500, 0), (point, 500))

for point in range(0, 500, 20):
    pygame.draw.line(background, (0, 0, 0), (500, 500), (0, point))

run = True
FPS = 30
clock = pygame.time.Clock()

screen.blit(background, (0, 0))

while run:
    milliseconds = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()