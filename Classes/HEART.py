from Settings import *
import animation
class HEART(animation.ANIMATE):
    def __init__(self):
        super().__init__("red_heart")
        self.image = pygame.transform.scale(self.image, (60, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 30