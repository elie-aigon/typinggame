from Settings import *

class ANIMATE(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.image = pygame.image.load("Data/Images/"+ name + ".png") 

