import sys
import pygame 

class Game:
    def __init__(self): 
        pygame.init()

        # Title
        pygame.display.set_caption('Jump Man')

        # Setting the display
        self.screen = pygame.display.set_mode((640, 480))

        # Forcing the game to run at 60 FPS
        self.clock = pygame.time.Clock()
        
        # Putting an image on screen
        self.image = pygame.image.load('data/images/clouds/cloud_1.png')
        
        # Removing the black background
        self.image.set_colorkey((0, 0, 0))
        
        # Moving an image / element
        self.image_pos = [160, 260]
        self.movement = [False, False]
        
    def run(self):
        while True:
            self.screen.fill((14, 219, 248))
            self.image_pos[1] += (self.movement[1] - self.movement[0]) *5 # *5 is adding speed 
            self.screen.blit(self.image, self.image_pos)
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    elif event.key == pygame.K_w:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                    elif event.key == pygame.K_s:
                        self.movement[1] = True
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    elif event.key == pygame.K_w:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
                    elif event.key == pygame.K_s:
                        self.movement[1] = False
                
                
                
            pygame.display.update() 
            self.clock.tick(60)
    
Game().run()