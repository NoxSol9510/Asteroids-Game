#asteroid
from circleshape import *

class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        def __init__(self, x, y, radius):
            CircleShape.__init__(self, x, y, radius)
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            self.rect = self.image.get_rect(center=(x, y))
            pygame.draw.circle(self.image, (128, 128, 128), (radius, radius), radius, 2)  # Gray with a width of 2

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = (int(self.position.x), int(self.position.y))

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)