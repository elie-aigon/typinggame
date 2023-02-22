from Settings import * 
from GAME import GAME

pygame.init()
screen = pygame.display.set_mode(window_size)
game = GAME(screen)

while True:
    if game.blocks_moving:
        game.sys_word_moving()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game.game_active:
            if len(game.heart_group) == 0:
                game.lose = True
                game.scorboard.update_score("".join(game.name), game.score)
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.quit_button.is_clicked(pygame.mouse.get_pos())
            if game.game_active:
                game.menu_button.is_clicked(pygame.mouse.get_pos())
            elif not game.game_active:
                game.checked_box_easy.is_clicked(pygame.mouse.get_pos())
                game.checked_box_normal.is_clicked(pygame.mouse.get_pos())
                game.checked_box_hard.is_clicked(pygame.mouse.get_pos())
                game.checkbox_en.is_clicked(pygame.mouse.get_pos())
                game.checkbox_fr.is_clicked(pygame.mouse.get_pos())
            if game.lose:
                game.win.is_clicked(pygame.mouse.get_pos())

        if event.type == pygame.KEYDOWN:
            if game.game_active:
                if game.input_char == game.split_word:
                    game.blocks_moving = True
                elif event.key in range(96, 123):                
                    if game.is_valid_letter(chr(event.key)):
                        game.input_char.append(chr(event.key))
                    else:
                        game.del_last_block()
                if game.input_char == game.split_word:
                    game.blocks_moving = True

            if not game.game_active:
                if event.key == pygame.K_BACKSPACE:
                    game.name = game.name[:-1]
                if event.key in range(96, 123):
                    game.name.append(chr(event.key))
                if event.key == pygame.K_RETURN:
                    game.game_active = True 
                    game.input_char = []
                    game.gen_lives()
                    game.score = 0
                

    game.draw_elements()
    pygame.display.update()