import pygame
from math import sqrt

pygame.init()
pygame.font.init()
game = pygame.display.set_mode((567, 630))
clock = pygame.time.Clock()
white = (250, 250, 250)
red = (255, 0, 0)
bg1 = (109, 90, 46)
p_color = (255, 128, 0)
blue = (0, 0, 255)
green = (0, 255, 0)


class Board:
    def __init__(self):
        self.highlight = None
        self.selected = None
        self.events = pygame.event.get()
        '''-------Board layout------'''
        self.pieces = [[R(self, blue), H(self, blue), E(self, blue), A(self, blue), G(self, blue), A(self, blue), E(self, blue), H(self, blue), R(self, blue)],
                       [None, None, None, None, None, None, None, None, None],
                       [None, C(self, blue), None, None, None, None, None, C(self, blue), None],
                       [S(self, blue), None, S(self, blue), None, S(self, blue), None, S(self, blue), None, S(self, blue)],
                       [None, None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None, None],
                       [S(self, red), None, S(self, red), None, S(self, red), None, S(self, red), None, S(self, red)],
                       [None, C(self, red), None, None, None, None, None, C(self, red), None],
                       [None, None, None, None, None, None, None, None, None],
                       [R(self, red), H(self, red), E(self, red), A(self, red), G(self, red), A(self, red), E(self, red), H(self, red), R(self, red)]]

    def add_text(self, size, text, color, posx, posy):
        myfont = pygame.font.Font("static/font.ttf", size)
        surf = myfont.render(text, False, color)
        game.blit(surf, (posx, posy))

    def to_board(self, coordx, coordy):
        return coordx // 62, coordy // 62

    def to_px(self, indx, indy):
        return 31 + indx * 62, 31 + indy * 62

    def createBoard(self):
        for i in range(10):
            al1, al2 = self.to_px(i, i)
            pygame.draw.line(game, white, (31, al1), (528, al1), 2)
        for i in range(9):
            al1, al2 = self.to_px(i, i)
            end1 = 31 + 4 * 62
            end2 = end1 + 62 + 4 * 62
            pygame.draw.line(game, white, (al1, 31), (al1, end1), 2)
            pygame.draw.line(game, white, (al1, end1 + 62), (al1, end2), 2)

        x1 = 3 * 62 + 31
        x2 = x1 + 62*2
        y1, y2, y3 = 31, 2 * 62 + 31, x1 * 2 + 31
        y4 = y3 + 2 * 62
        pygame.draw.line(game, white, (x1, y1), (x2, y2), 2)
        pygame.draw.line(game, white, (x1, y2),(x2, y1),2)
        pygame.draw.line(game, white, (x1, y3),(x2, y4),2)
        pygame.draw.line(game, white, (x1, y4),(x2, y3),2)

        for i1, val1 in enumerate(self.pieces):
            for i2, val2 in enumerate(val1):
                if val2:
                    al1, al2 = self.to_px(i2, i1)
                    pygame.draw.circle(game, p_color, self.to_px(i2, i1), 29)
                    val2.display(al1, al2)
                    val2.create_move()

    def hover_mouse(self):
        m_x, m_y = pygame.mouse.get_pos()
        tob_x, tob_y = self.to_board(m_x, m_y)
        if 0 <= tob_x <= 8 and 0 <= tob_y <= 9:
            top_x, top_y = self.to_px(tob_x, tob_y)
            self.t_x, self.t_y = top_x, top_x
            if sqrt((m_x - top_x) ** 2 + (m_y - top_y) ** 2) <= 32:
                pygame.draw.circle(game, white, (top_x, top_y), 25, 2)
                self.highlight = (tob_x, tob_y)
                self.highlighted = self.pieces[tob_y][tob_x]

    def mouse_click(self):
        if not self.highlight:
            return
        clicked = self.pieces[self.highlight[1]][self.highlight[0]]
        if not self.selected and clicked:
            self.selected = self.highlight
        elif self.selected:
            selected_piece = self.pieces[self.selected[1]][self.selected[0]]
            if self.highlight != self.selected:
                if self.highlight in selected_piece.valid_move:
                    self.pieces[self.selected[1]][self.selected[0]] = None
                    self.pieces[self.highlight[1]][self.highlight[0]] = selected_piece
            self.selected = None
# Source: Vladislav Zorov

class Piece:
    '''Pieces super class.
    S:soldier, C:cannon, R:rook, H:horse, E:elephant, A:adviser, G:general'''

    def __init__(self, board, txt_color):
        self.board = board
        self.txt_color = txt_color

    '''Piece current position'''

    def my_pos(self):
        for i1, val1 in enumerate(self.board.pieces):
            for i2, val2 in enumerate(val1):
                if val2 == self:
                    return (i2, i1)


class S(Piece):
    '''SOLDIER.'''

    def __init__(self, board, txt_color):
        Piece.__init__(self, board, txt_color)
        self.txt_color = txt_color
        self.valid_move = []

    def display(self, al1, al2):
        self.board.add_text(25, '卒', self.txt_color, al1 - 12, al2 - 12)

    def create_move(self):
        # i2 is x, and i1 is y
        pos = self.my_pos()
        del self.valid_move[:]
        if self.txt_color == (0, 0, 255):
            self.valid_move.append((pos[0], pos[1] + 1))
            if pos[1] > 4:
                self.valid_move.append((pos[0] + 1, pos[1]))
                self.valid_move.append((pos[0] - 1, pos[1]))
        else:
            self.valid_move.append((pos[0], pos[1] - 1))
            if pos[1] < 5:
                self.valid_move.append((pos[0] + 1, pos[1]))
                self.valid_move.append((pos[0] - 1, pos[1]))


class R(Piece):
    '''ROOK.'''

    def __init__(self, board, txt_color):
        Piece.__init__(self, board, txt_color)
        self.txt_color = txt_color
        self.valid_move = []

    def display(self, al1, al2):
        self.board.add_text(25, '车', self.txt_color, al1 - 12, al2 - 12)

    def create_move(self):
        del self.valid_move[:]
        pos = self.my_pos()
        # left
        for i in range(pos[0] - 1, -1, -1):
            if self.board.pieces[pos[1]][i] and self.board.pieces[pos[1]][i].txt_color != self.txt_color:
                self.valid_move.append((i, pos[1]))
                break
            if self.board.pieces[pos[1]][i]:
                break
            self.valid_move.append((i, pos[1]))
        # right
        for i in range(pos[0] + 1, 9, 1):
            if self.board.pieces[pos[1]][i] and self.board.pieces[pos[1]][i].txt_color != self.txt_color:
                self.valid_move.append((i, pos[1]))
                break
            if self.board.pieces[pos[1]][i]:
                break
            self.valid_move.append((i, pos[1]))
        # top
        for i in range(pos[1] - 1, -1, -1):
            if self.board.pieces[i][pos[0]] and self.board.pieces[i][pos[0]].txt_color != self.txt_color:
                self.valid_move.append((pos[0], i))
                break
            if self.board.pieces[i][pos[0]]:
                break
            self.valid_move.append((pos[0], i))
        # bottom
        for i in range(pos[1] + 1, 10, 1):
            if self.board.pieces[i][pos[0]] and self.board.pieces[i][pos[0]].txt_color != self.txt_color:
                self.valid_move.append((pos[0], i))
                break
            if self.board.pieces[i][pos[0]]:
                break
            self.valid_move.append((pos[0], i))


class C(Piece):
    '''CANNON.'''

    def __init__(self, board, txt_color):
        Piece.__init__(self, board, txt_color)
        self.txt_color = txt_color
        self.valid_move = []

    def display(self, al1, al2):
        self.board.add_text(25, '炮', self.txt_color, al1 - 12, al2 - 12)

    def create_move(self):
        del self.valid_move[:]
        pos = self.my_pos()
        left, right, top, bot = None, None, None, None
        # left
        for i in range(pos[0] - 1, -1, -1):
            if self.board.pieces[pos[1]][i]:
                left = i
                break
            self.valid_move.append((i, pos[1]))
        # right
        for i in range(pos[0] + 1, 9, 1):
            if self.board.pieces[pos[1]][i]:
                right = i
                break
            self.valid_move.append((i, pos[1]))
        # top
        for i in range(pos[1] - 1, -1, -1):
            if self.board.pieces[i][pos[0]]:
                top = i
                break
            self.valid_move.append((pos[0], i))
        # bottom
        for i in range(pos[1] + 1, 10, 1):
            if self.board.pieces[i][pos[0]]:
                bot = i
                break
            self.valid_move.append((pos[0], i))

            # work with left,right,top,bot
            # to check whether an enemy is on the other side
        # left
        if left:
            for i in range(left - 1, -1, -1):
                if self.board.pieces[pos[1]][i] and self.board.pieces[pos[1]][i].txt_color != self.txt_color:
                    self.valid_move.append((i, pos[1]))
                    break
        # right
        if right:
            for i in range(right + 1, 9, 1):
                if self.board.pieces[pos[1]][i] and self.board.pieces[pos[1]][i].txt_color != self.txt_color:
                    self.valid_move.append((i, pos[1]))
                    break
        # top
        if top:
            for i in range(top - 1, -1, -1):
                if self.board.pieces[i][pos[0]] and self.board.pieces[i][pos[0]].txt_color != self.txt_color:
                    self.valid_move.append((pos[0], i))
                    break
        # bottom
        if bot:
            for i in range(bot + 1, 10, 1):
                if self.board.pieces[i][pos[0]] and self.board.pieces[i][pos[0]].txt_color != self.txt_color:
                    self.valid_move.append((pos[0], i))
                    break


class H(Piece):
    '''HORSE.'''

    def __init__(self, board, txt_color):
        Piece.__init__(self, board, txt_color)
        self.txt_color = txt_color
        self.valid_move = []

    def display(self, al1, al2):
        self.board.add_text(25, '马', self.txt_color, al1 - 12, al2 - 12)

    def move_gen(self,inx, iny, outx, outy, landx1, landy1, landx2, landy2):
        pos = self.my_pos()
        b_pos = self.board.pieces
        # Virtual extra border, you saved my day. You sir deserve a cookie.
        b_pos.append([None,None,None,None,None,None,None,None,None,None])
        for i in range(10):
            b_pos[i].append(None)

        if not b_pos[pos[1]+iny][pos[0]+inx] and not b_pos[pos[1]+outy][pos[0]+outx]:
            if not b_pos[pos[1]+landy1][pos[0]+landx1] or b_pos[pos[1]+landy1][pos[0]+landx1].txt_color != self.txt_color:
                self.valid_move.append((pos[0]+landx1, pos[1]+landy1))
            if not b_pos[pos[1]+landy2][pos[0]+landx2] or b_pos[pos[1]+landy2][pos[0]+landx2].txt_color != self.txt_color:
                self.valid_move.append((pos[0]+landx2, pos[1]+landy2))

    '''    (x-1,y-2) (x+1,y-2)
    (x-2,y-1)       |       (x+2,y-1)         
              ------+------
    (x-2,y+1)       |       (x+2,y+1)
           (x-1,y+2) (x+1,y-2)
    '''
    def create_move(self):
        pos = self.my_pos()
        self.move_gen(-1,0,-2,0,-2,-1,-2,1)
        self.move_gen(1,0,2,0,2,-1,2,1)
        self.move_gen(0,-1,0,-2,-1,-2,1,-2)
        self.move_gen(0,1,0,2,-1,2,1,2)

class E(Piece):
    '''ELEPHANT.'''

    def __init__(self, board, txt_color):
        Piece.__init__(self, board, txt_color)
        self.txt_color = txt_color
        self.valid_move = []

    def display(self, al1, al2):
        self.board.add_text(25, '相', self.txt_color, al1 - 12, al2 - 12)

    def move_gen(self, inx, iny, outx, outy):
        pos = self.my_pos()
        if not self.board.pieces[pos[1] + iny][pos[0] + inx]:
            board_pos = self.board.pieces[pos[1] + outy][pos[0] + outx]
            if not board_pos or board_pos.txt_color != self.txt_color:
                self.valid_move.append((pos[0] + outx, pos[1] + outy))

    def create_move(self):
        del self.valid_move[:]
        pos = self.my_pos()
        # blue
        if pos[1] < 5:
            self.move_gen(-1, 1, -2, 2) # SW
            self.move_gen(-1, -1, -2, -2) # NW
            if pos[0] < 8:
                self.move_gen(1, -1, 2, -2) # NE
                self.move_gen(1, 1, 2, 2) # SE
        # red
        # this part is kinda messy
        if pos[1] >= 5:
            if pos[1] < 9:
                self.move_gen(-1, 1, -2, 2) # SW
                if pos[0] < 8:
                    self.move_gen(1, 1, 2, 2)  # SE
            if pos[1] <= 9:
                self.move_gen(-1, -1, -2, -2) # NW
                if pos[0] < 8:
                    self.move_gen(1, -1, 2, -2) # NE

class A(Piece):
    '''ADVISER.'''

    def __init__(self, board, txt_color):
        Piece.__init__(self, board, txt_color)
        self.txt_color = txt_color
        self.valid_move = []

    def display(self, al1, al2):
        self.board.add_text(25, '士', self.txt_color, al1 - 12, al2 - 12)

    def move_gen(self, x, y):
        pos = self.my_pos()
        if not self.board.pieces[pos[1]+y][pos[0]+x]:
            if not self.board.pieces[pos[1]+y][pos[0]+x] or self.board.pieces[pos[1]+y][pos[0]+x].txt_color != self.txt_color:
                if 3<=pos[0]+x<=5 and 0<=pos[1]+y<=2:
                    self.valid_move.append((pos[0]+x, pos[1]+y))

    def create_move(self):
        del self.valid_move[:]
        self.move_gen(-1,-1)
        self.move_gen(1,-1)
        self.move_gen(1,1)
        self.move_gen(-1,1)

class G(Piece):
    '''GENERAL.'''

    def __init__(self, board, txt_color):
        Piece.__init__(self, board, txt_color)
        self.txt_color = txt_color
        self.valid_move = []

    def display(self, al1, al2):
        self.board.add_text(25, '将', self.txt_color, al1 - 12, al2 - 12)

    def move_gen(self, x, y):
        pos = self.my_pos()
        if not self.board.pieces[pos[1]+y][pos[0]+x]:
            if not self.board.pieces[pos[1]+y][pos[0]+x] or self.board.pieces[pos[1]+y][pos[0]+x].txt_color != self.txt_color:
                if 3<=pos[0]+x<=5 and 0<=pos[1]+y<=2:
                    self.valid_move.append((pos[0]+x, pos[1]+y))

    def create_move(self):
        del self.valid_move[:]
        self.move_gen(-1,0)
        self.move_gen(0,-1)
        self.move_gen(1,0)
        self.move_gen(0,1)

# -------------------Main-----------------
board = Board()
def main():
    while True:
        eve = pygame.event.get()
        for event in eve:
            if event.type == pygame.QUIT:
                return pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.mouse_click()

        game.fill(bg1)

        board.createBoard()
        board.hover_mouse()

        pygame.display.flip()
        clock.tick(60)

main()