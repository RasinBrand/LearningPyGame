import sys
import pygame 

pygame.init()

# Setting the display
screen = pygame.display.set_mode((640, 480))

# Forcing the game to run at 60 FPS
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
    
    pygame.display.update() 
    clock.tick(60)
    