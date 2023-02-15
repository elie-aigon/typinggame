from Settings import * 
from GAME import GAME

pygame.init()
# state 
blocks_moving = False
count = 0
screen = pygame.display.set_mode(window_size)
game = GAME(screen)

while True:
    if blocks_moving:
        count += 1
        game.blocks_moves()
        if count == 14:
            game.input_char = []
            game.add_block()
            game.del_first_block()
            count = 0
            blocks_moving = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.del_last_block()
            if event.key == pygame.K_LEFT:
                game.fellow.move_left()
            if event.key == pygame.K_RIGHT:
                game.fellow.move_right()
            if event.key == pygame.K_RETURN:
                blocks_moving = True
            if event.key == pygame.K_BACKSPACE:
                game.input_char = game.input_char[-1]
            if event.key in range(96, 123):
                if game.is_valid_letter(chr(event.key)):
                    game.input_char.append(chr(event.key))
                    if game.input_char == game.split_word:
                        blocks_moving = True
                else:
                    game.del_last_block()
    game.draw_elements()
    pygame.display.update()