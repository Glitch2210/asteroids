# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    dt = 0
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    #create player
    player_1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while True:
        #check for exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #local variables
        color = [0,0,0]

        #Screen Display
        screen.fill(color)
        player_1.draw(screen)

        #FPS throtal
        dt =  clock.tick(60) / 1000
        
        pygame.display.flip()
        
        

if __name__ == "__main__":
    main()