from Settings import *
import animation

class FELLOW(animation.ANIMATE):
    def __init__(self):
        super().__init__("mario_stop")
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.speed = 50
        
