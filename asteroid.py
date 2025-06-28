from circleshape import *
from constants import *
asteroid_color = [255,255,255]
class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        print("check a update")
        pygame.draw.circle(screen,asteroid_color,self.position,self.radius,2)

    def update(self,dt):
        self.position += (self.velocity * dt)