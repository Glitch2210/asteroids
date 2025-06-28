import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen,ASTEROID_COLOR,self.position,self.radius,2)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            split_angle = random.uniform(20,50)
            split_radius = self.radius -ASTEROID_MIN_RADIUS
            asteroid_new_1 = Asteroid(self.position.x,self.position.y,split_radius)
            asteroid_new_2 = Asteroid(self.position.x,self.position.y,split_radius)            
            
            asteroid_new_1.velocity = self.velocity.rotate(split_angle) * ASTEROID_SPLIT_VELOCITY
            asteroid_new_2.velocity  = self.velocity.rotate(-split_angle) * ASTEROID_SPLIT_VELOCITY
        
        self.kill()
