from Settings import *
import animation

class FELLOW(animation.ANIMATE):
    def __init__(self):
        super().__init__("mario_stop")
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 700
        self.speed = 50
        
    def move_left(self):
        self.rect.x -= self.speed
    def move_right(self):
        self.rect.x += self.speed