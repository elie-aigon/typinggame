from Settings import *
import animation

class BLOCK(animation.ANIMATE):
    def __init__(self):
        super().__init__("block")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(200,600)
        self.rect.y = -200
        self.speed = 20
        self.lang_fr = True
        if self.lang_fr:
            self.random_word = random.choice(word_list["francais"])
        else:
            self.random_word = random.choice(word_list["anglais"])
        self.split_word = [char for char in self.random_word]

    def draw_text_block(self, surface):
        self.text_block = font_mid.render(self.random_word, True, grey)
        surface.blit(self.text_block, (self.rect.x + 50, self.rect.y))

