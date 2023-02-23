from Settings import *

class TIMER():
    def __init__(self):
        self.percent = 0
        self.speed = 0.1

    def update_timer(self, surface):
        self.percent += self.speed
        pygame.draw.rect(surface, grey, [0, 5, window_size[0], 20])
        pygame.draw.rect(surface, red, [0, 5, (window_size[0]//100) * self.percent, 20])

