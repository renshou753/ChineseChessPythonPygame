import pygame
from pieces import *
from config import startX, startY, cellW, white, red, pieceColor, radius

class Board:
    def __init__(self, win, rows, cols):
        self.win = win
        self.rows = rows
        self.cols = cols

        self.highlight = None
        self.select = None

        # create empty pieces for the board
        self.board = [[0 for x in range(cols)] for _ in range(rows)]

        self.board[0][0] = Chariot(self, 'b')
        self.board[0][1] = Horse(self, 'b')
        self.board[0][2] = Elephant(self, 'b')
        self.board[0][3] = Advisor(self, 'b')
        self.board[0][4] = General(self, 'b')
        self.board[0][5] = Advisor(self, 'b')
        self.board[0][6] = Elephant(self, 'b')
        self.board[0][7] = Horse(self, 'b')
        self.board[0][8] = Chariot(self, 'b')
        self.board[2][1] = Cannon(self, 'b')
        self.board[2][7] = Cannon(self, 'b')
        self.board[3][0] = Soldier(self, 'b')
        self.board[3][2] = Soldier(self, 'b')
        self.board[3][4] = Soldier(self, 'b')
        self.board[3][6] = Soldier(self, 'b')
        self.board[3][8] = Soldier(self, 'b')

        self.board[9][0] = Chariot(self, 'r')
        self.board[9][1] = Horse(self, 'r')
        self.board[9][2] = Elephant(self, 'r')
        self.board[9][3] = Advisor(self, 'r')
        self.board[9][4] = General(self, 'r')
        self.board[9][5] = Advisor(self, 'r')
        self.board[9][6] = Elephant(self, 'r')
        self.board[9][7] = Horse(self, 'r')
        self.board[9][8] = Chariot(self, 'r')
        self.board[7][1] = Cannon(self, 'r')
        self.board[7][7] = Cannon(self, 'r')
        self.board[6][0] = Soldier(self, 'r')
        self.board[6][2] = Soldier(self, 'r')
        self.board[6][4] = Soldier(self, 'r')
        self.board[6][6] = Soldier(self, 'r')
        self.board[6][8] = Soldier(self, 'r')

    # convert from matrix(indexX, indexY) to the actual position on board  
    def convert(self, inX, inY):
        return startX + inX * cellW, startY + inY * cellW

    def create(self):
        # draw 10 horizontal lines
        for i in range(self.rows):
            l1, l2 = self.convert(i, i)
            # calc x position of the last col on the board, col 9
            endX = startX + cellW * (self.cols - 1)
            pygame.draw.line(self.win, white, (startX, l1), (endX, l2), 2)

        # draw 9 vertical lines
        for i in range(self.cols):
            l1, l2 = self.convert(i, i)
            # two sides are divided by river, calculate the endY pos for each
            end1 = startY + 4 * cellW
            end2 = startY + 9 * cellW
            pygame.draw.line(self.win, white, (l1, startY), (l2, end1), 2)
            pygame.draw.line(self.win, white, (l1, end1 + cellW), (l1, end2), 2)

        # draw 4 diagonal lines
        x1 = startX + cellW * 3
        x2 = startX + cellW * 5
        y1 = startY
        y2 = startY + 2 * cellW
        y3 = startY + 7 * cellW
        y4 = startY + 9 * cellW
        pygame.draw.line(self.win, white, (x1, y1), (x2, y2), 2)
        pygame.draw.line(self.win, white, (x2, y1), (x1, y2), 2)
        pygame.draw.line(self.win, white, (x1, y3), (x2, y4), 2)
        pygame.draw.line(self.win, white, (x2, y3), (x1, y4), 2)

        # fraw each piece
        for i, row in enumerate(self.board):
            for j, piece in enumerate(row):
                if piece != 0:
                    posX, posY = self.convert(j, i)
                    pygame.draw.circle(self.win, pieceColor, (posX, posY), radius)
                    piece.drawText(posX, posY)
        
    
    def draw_text(self, size, text, color, posX, posY):
        font = pygame.font.Font("static/font.ttf", size)
        surf = font.render(text, False, color)
        self.win.blit(surf, (posX, posY))


        