# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)

    dt = 0
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    #create objects
    player_1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    print(drawable)
    print(updatable)
    while True:
        #check for exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #local variables
        color = [0,0,0]

        #Screen Display
        screen.fill(color)
        updatable.update(dt)

        #draw loop
        for d in drawable:
            d.draw(screen)

        #FPS throtal
        dt =  clock.tick(60) / 1000
        
        pygame.display.flip()
        
        

if __name__ == "__main__":
    main()