from board import Board
from config import fontSize, windowH, windowW, bgC, fps, black, red
import pygame



def main():
    pygame.font.init()
    win = pygame.display.set_mode((windowW, windowH))
    clock = pygame.time.Clock()
    board = Board(win, 10, 9)  # 10 cols, 9 rows in a typical chinese chess board
    turn = red
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or turn == "End":
                return pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                turn = board.mouse_click(turn)
        
        win.fill(bgC)
        
        board.create()
        board.hover_mouse()

        pygame.display.flip()
        clock.tick(fps)

if __name__ == "__main__":
    main()