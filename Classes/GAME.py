from Settings import *
from FELLOW import FELLOW
from BLOCK import BLOCK
from HEART import HEART

class GAME():
    def __init__(self, surface):
        self.surface = surface
        # lives
        self.lives = 3
        self.heart_group = pygame.sprite.Group()
        self.heart_group.add(HEART(), HEART(), HEART())
        self.heart_group.sprites()[1].rect.x += 65
        self.heart_group.sprites()[2].rect.x += 130
        # for element in self.heart_group:
        #     element.rect.x += self.heart_group.index(element) * 65
        # def fellow
        self.fellow = FELLOW()
        self.fellow_group = pygame.sprite.Group()
        self.fellow_group.add(self.fellow)
        # def block
        self.block = BLOCK()
        self.block_group = pygame.sprite.Group()
        self.block_group.add(self.block)
        # background
        self.background = pygame.image.load("Data/Images/background.png")
        self.background = pygame.transform.scale(self.background, window_size)  
        # word typed
        self.input_char = []

    def get_pos_rand_word(self):
        for block in self.block_group:
            first_block = self.block_group.sprites()[0]
            self.new_pos = (first_block.rect.x + 50, first_block.rect.y)
            self.split_word = first_block.split_word
            self.split_word_input = first_block.split_word
            
    def draw_word_typed(self):
        self.get_pos_rand_word()
        self.input_char_aff = font_mid.render("".join(self.input_char), True, white)
        self.surface.blit(self.input_char_aff, self.new_pos)

    def draw_elements(self):
        self.surface.blit(self.background, (0, 0))
        self.fellow_group.draw(self.surface)
        self.block_group.draw(self.surface)
        self.heart_group.draw(self.surface)
        for block in self.block_group:
            block.draw_text_block(self.surface)
            self.draw_word_typed()

    def add_block(self):
        self.new_block = BLOCK()
        self.block_group.add(self.new_block)
    
    def del_first_block(self):
        if len(self.block_group) >3:
            self.first_block = self.block_group.sprites()[0]
            self.block_group.remove(self.first_block)
            self.lives -= 1

    def del_last_block(self):
        self.last_block = self.heart_group.sprites()[-1]
        self.heart_group.remove(self.last_block)
    def blocks_moves(self):
        for block in self.block_group:
            block.rect.y += self.block.speed

    def is_valid_letter(self, char):
        
        self.new_char_index = len(self.input_char)
        if self.split_word_input[self.new_char_index] == char:
            return True
        else:
            return False