from Settings import *
from FELLOW import FELLOW
from BLOCK import BLOCK
from HEART import HEART
from BUTTON import BUTTON
from SCORBOARD import SCOREBOARD
from CHECKBOX import CHECKBOX
from CHECKBOX_LANG import CHECKBOX_LANG

class GAME():
    def __init__(self, surface):
        self.surface = surface
        # buttons
        self.menu_button = BUTTON(self.surface, font_small, grey, 1200, 800, 150, 80, "MENU", "Data/Images/green_button/gree_normal.png", lambda: self.button_menu_action())
        self.quit_button = BUTTON(self.surface, font_small, grey, 1400, 800, 150, 80, "QUIT", "Data/Images/red/red_normal.png", lambda: self.button_quit_action())
        # scorboard
        self.scorboard = SCOREBOARD(self.surface, (1150, 70))
        # title
        self.title = font_title.render("TYPING GAME", True, grey)
        # state
        self.game_active = False
        self.blocks_moving = False
        self.count = 0
        # lives
        self.lives = 3
        self.heart_group = pygame.sprite.Group()
        self.heart_group.add(HEART(), HEART(), HEART())
        self.heart_group.sprites()[1].rect.x += 65
        self.heart_group.sprites()[2].rect.x += 130
        # for element in self.heart_group
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
        # checkbox lvl
        self.checked_box_easy = CHECKBOX(self.surface, font_mid, grey, 80, 400, 100, 90, "EASY", "Data/images/unchecked_box.png", lambda: self.easy_clicked())
        self.checked_box_normal = CHECKBOX(self.surface, font_mid, grey, 80, 520, 100, 90, "Normal", "Data/images/unchecked_box.png", lambda: self.normal_clicked())
        self.checked_box_hard = CHECKBOX(self.surface, font_mid, grey, 80, 640, 100, 90, "hard", "Data/images/unchecked_box.png", lambda: self.hard_clicked())
        self.checked_box_easy.state = True
        # checkbox lang
        self.checkbox_fr = CHECKBOX_LANG(self.surface, font_mid, grey, 50, 30, 80, 80, "FR", "Data/Images/yellow/yellow_normal.png", lambda: self.fr_clicked())
        self.checkbox_en = CHECKBOX_LANG(self.surface, font_mid, grey, 150, 30, 80, 80, "EN", "Data/Images/yellow/yellow_normal.png", lambda: self.en_clicked())
        self.checkbox_fr.state = True
        # name init
        self.name = []
    
    # checkbox org
    def easy_clicked(self):
        self.checked_box_easy.state = True
        self.checked_box_normal.state = False
        self.checked_box_hard.state = False
    
    def normal_clicked(self):
        self.checked_box_easy.state = False
        self.checked_box_normal.state = True
        self.checked_box_hard.state = False
    
    def hard_clicked(self):
        self.checked_box_easy.state = False
        self.checked_box_normal.state = False
        self.checked_box_hard.state = True
    # checkbox lang org
    def fr_clicked(self):
        self.checkbox_fr.state = True
        self.checkbox_en.state = False
    def en_clicked(self):
        self.checkbox_fr.state = False
        self.checkbox_en.state = True
    # basics button org
    def button_menu_action(self):
        self.game_active = False
        self.name = []

    def button_quit_action(self):
        pygame.quit()
        sys.exit()
    
    # word render   
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
        self.quit_button.draw_button()
        if not self.game_active:
            self.instructions = font_mid.render("Type your name : ", True, white)
            self.name_aff = font_mid.render("".join(self.name), True, white)
            self.surface.blit(self.name_aff, (380, 120))
            self.start_instruc = font_small.render("Click the difficulty, the lang then Press 'ENTER' to start playing : ", True, white)
            self.surface.blit(self.start_instruc, (30, 210))
            self.surface.blit(self.title, (window_size[0] //2 - self.title.get_width()// 2, 30))
            self.checked_box_easy.draw_button()
            self.checked_box_normal.draw_button()
            self.checked_box_hard.draw_button()
            self.checkbox_en.draw_button()
            self.checkbox_fr.draw_button()
            self.scorboard.draw_scoreboard()
        if self.game_active:
            self.menu_button.draw_button()
            self.fellow_group.draw(self.surface)
            self.block_group.draw(self.surface)
            self.heart_group.draw(self.surface)
            for block in self.block_group:
                block.draw_text_block(self.surface)
                self.draw_word_typed()

    # word organisation
    def sys_word_moving(self):
        self.count += 1
        self.blocks_moves()
        if self.count == 14:
            self.input_char = []
            self.add_block()
            self.del_first_block()
            self.count = 0
            self.blocks_moving = False
    
    def add_block(self):
        self.new_block = BLOCK()
        self.block_group.add(self.new_block)
    
    def del_first_block(self):
        if len(self.block_group) >3:
            self.first_block = self.block_group.sprites()[0]
            self.block_group.remove(self.first_block)
            self.lives -= 1

    def blocks_moves(self):
        for block in self.block_group:
            block.rect.y += self.block.speed

    # check input 
    def is_valid_letter(self, char):
        self.new_char_index = len(self.input_char)
        if self.split_word_input[self.new_char_index] == char:
            return True
        else:
            return False

    # del lives if wrong
    def del_last_block(self):
        self.last_block = self.heart_group.sprites()[-1]
        self.heart_group.remove(self.last_block)