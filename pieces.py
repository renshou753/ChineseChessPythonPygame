from config import fontSize, black, red, textMove

class Piece:
    # super class
    def __init__(self, board, clr):
        self.board = board
        self.pieces = board.board
        if clr == 'b':
            self.clr = black
        else:
            self.clr = red
    
    def getPos(self):
        for i, row in enumerate(self.pieces):
            for j, piece in enumerate(row):
                if piece == self:
                    return (j, i)


class Chariot(Piece):
    def __init__(self, board, clr):
        super().__init__(board, clr)
        self.valid_move = []
    
    def drawText(self, posX, posY):
        self.board.draw_text(fontSize, '车', self.clr, posX - textMove, posY - textMove)

    def makeMoves(self):
        pos = self.getPos()
        del self.valid_move[:]
        # up
        for i in range(pos[1] - 1, -1, -1):
            if self.pieces[i][pos[0]] == 0 :
                self.valid_move.append((pos[0], i))
            elif self.pieces[i][pos[0]].clr != self.clr:
                self.valid_move.append((pos[0], i))
                break
            elif self.pieces[i][pos[0]].clr == self.clr:
                break
        # down
        for i in range(pos[1] + 1, 10, 1):
            if self.pieces[i][pos[0]] == 0 :
                self.valid_move.append((pos[0], i))
            elif self.pieces[i][pos[0]].clr != self.clr:
                self.valid_move.append((pos[0], i))
                break
            elif self.pieces[i][pos[0]].clr == self.clr:
                break    
        # left
        for i in range(pos[0] - 1, -1, -1):
            if self.pieces[pos[1]][i] == 0 :
                self.valid_move.append((i, pos[1]))
            elif self.pieces[pos[1]][i].clr != self.clr:
                self.valid_move.append((i, pos[1]))
                break
            elif self.pieces[pos[1]][i].clr == self.clr:
                break    
        # right
        for i in range(pos[0] + 1, 9, 1):
            if self.pieces[pos[1]][i] == 0 :
                self.valid_move.append((i, pos[1]))
            elif self.pieces[pos[1]][i].clr != self.clr:
                self.valid_move.append((i, pos[1]))
                break
            elif self.pieces[pos[1]][i].clr == self.clr:
                break  


class Horse(Piece):
    def __init__(self, board, clr):
        super().__init__(board, clr)
        self.valid_move = []

    def drawText(self, posX, posY):
        self.board.draw_text(fontSize, '马', self.clr, posX - textMove, posY- textMove)

    def makeMoves(self):
        pos = self.getPos()
        del self.valid_move[:]
        ''' a    b
        c     |     d         
        ------+------
        e     |     f
            g    h
        '''


class Elephant(Piece):
    def __init__(self, board, clr):
        super().__init__(board, clr)
        self.valid_move = []

    def drawText(self, posX, posY):
        self.board.draw_text(fontSize, '相', self.clr, posX - textMove, posY- textMove)

    def makeMoves(self):
        pass

class Advisor(Piece):
    def __init__(self, board, clr):
        super().__init__(board, clr)
        self.valid_move = []

    def drawText(self, posX, posY):
        self.board.draw_text(fontSize, '士', self.clr, posX - textMove, posY- textMove)

    def makeMoves(self):
        pass

class General(Piece):
    def __init__(self, board, clr):
        super().__init__(board, clr)
        self.valid_move = []

    def drawText(self, posX, posY):
        self.board.draw_text(fontSize, '将', self.clr, posX - textMove, posY- textMove)

    def makeMoves(self):
        pass

class Cannon(Piece):
    def __init__(self, board, clr):
        super().__init__(board, clr)
        self.valid_move = []

    def drawText(self, posX, posY):
        self.board.draw_text(fontSize, '炮', self.clr, posX - textMove, posY- textMove)

    def makeMoves(self):
        pass

class Soldier(Piece):
    def __init__(self, board, clr):
        super().__init__(board, clr)
        self.valid_move = []

    def drawText(self, posX, posY):
        self.board.draw_text(fontSize, '卒', self.clr, posX - textMove, posY- textMove)
    
    def makeMoves(self):
        pass