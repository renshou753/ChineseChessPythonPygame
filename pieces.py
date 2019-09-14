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
        # a, self.pieces[pos[1]-1][pos[0]] == 0 is to make sure there is no obstacles
        if pos[0] > 0 and pos[1] > 1 and self.pieces[pos[1]-1][pos[0]] == 0:
            TargetPiece = self.pieces[pos[1] - 2][pos[0] - 1]
            if TargetPiece == 0 or TargetPiece.clr != self.clr:
                self.valid_move.append((pos[0] - 1, pos[1] - 2))
        # b
        if pos[0] < 8 and pos[1] > 1 and self.pieces[pos[1]-1][pos[0]] == 0:
            TargetPiece = self.pieces[pos[1] - 2][pos[0] + 1]
            if TargetPiece == 0 or TargetPiece.clr != self.clr:
                self.valid_move.append((pos[0] + 1, pos[1] - 2))
        # c
        if pos[0] > 1 and pos[1] > 0 and self.pieces[pos[1]][pos[0]-1] == 0:
            TargetPiece = self.pieces[pos[1] - 1][pos[0] - 2]
            if TargetPiece == 0 or TargetPiece.clr != self.clr:
                self.valid_move.append((pos[0] - 2, pos[1] - 1))
        # d
        if pos[0] < 7 and pos[1] > 0 and self.pieces[pos[1]][pos[0]+1] == 0:
            TargetPiece = self.pieces[pos[1] - 1][pos[0] + 2]
            if TargetPiece == 0 or TargetPiece.clr != self.clr:
                self.valid_move.append((pos[0] + 2, pos[1] - 1))
        # e
        if pos[0] > 1 and pos[1] < 9 and self.pieces[pos[1]][pos[0]-1] == 0:
            TargetPiece = self.pieces[pos[1] + 1][pos[0] - 2]
            if TargetPiece == 0 or TargetPiece.clr != self.clr:
                self.valid_move.append((pos[0] - 2, pos[1] + 1))
        # f
        if pos[0] < 7 and pos[1] < 9 and self.pieces[pos[1]][pos[0]+1] == 0:
            TargetPiece = self.pieces[pos[1] + 1][pos[0] + 2]
            if TargetPiece == 0 or TargetPiece.clr != self.clr:
                self.valid_move.append((pos[0] + 2, pos[1] + 1))
        # g
        if pos[0] > 0 and pos[1] < 8 and self.pieces[pos[1]+1][pos[0]] == 0:
            TargetPiece = self.pieces[pos[1] + 2][pos[0] - 1]
            if TargetPiece == 0 or TargetPiece.clr != self.clr:
                self.valid_move.append((pos[0] - 1, pos[1] + 2))
        # h
        if pos[0] < 8 and pos[1] < 8 and self.pieces[pos[1]+1][pos[0]] == 0:
            TargetPiece = self.pieces[pos[1] + 2][pos[0] + 1]
            if TargetPiece == 0 or TargetPiece.clr != self.clr:
                self.valid_move.append((pos[0] + 1, pos[1] + 2))



class Elephant(Piece):
    def __init__(self, board, clr):
        super().__init__(board, clr)
        self.valid_move = []

    def drawText(self, posX, posY):
        self.board.draw_text(fontSize, '相', self.clr, posX - textMove, posY- textMove)

    def makeMoves(self):
        ''' 
          a       b
              |              
        ------+------
              |     
          c        d
        '''
        del self.valid_move[:]
        pos = self.getPos()

        # generic to all piece color, moves would be the same if the piece is on 1st or last column
        if pos[0] == 0:  # if piece is on the left most column
            self.genMoves(2, -2, 1, -1)   # b
            self.genMoves(2, 2, 1, 1)  # d
        elif pos[0] == 8: # if piece is on the right most column
            self.genMoves(-2, -2, -1, -1) # a
            self.genMoves(-2, 2, -1, 1) # c
        
        if pos[0] != 0 and pos[0] != 8 and pos[1] in [0, 2, 5, 7]:  # if piece is on these rows
            self.genMoves(-2, 2, -1, 1) # c
            self.genMoves(2, 2, 1, 1)  # d
        if pos[0] != 0 and pos[0] != 8 and pos[1] in [2, 4, 7, 9]:
            self.genMoves(-2, -2, -1, -1) # a
            self.genMoves(2, -2, 1, -1)  # b
    
    def genMoves(self, inX, inY, blockX, blockY):
        pos = self.getPos()
        if self.pieces[pos[1] + blockY][pos[0] + blockX] == 0:
            targetPiece = self.pieces[pos[1] + inY][pos[0] + inX]
            if targetPiece == 0 or targetPiece.clr != self.clr:
                self.valid_move.append((pos[0] + inX, pos[1] + inY))


class Advisor(Piece):
    def __init__(self, board, clr):
        super().__init__(board, clr)
        self.valid_move = []

    def drawText(self, posX, posY):
        self.board.draw_text(fontSize, '士', self.clr, posX - textMove, posY- textMove)

    def makeMoves(self):
        ''' 
          a       b
                            
              e
                   
          c        d
        '''
        del self.valid_move[:]
        pos = self.getPos()
        # if piece is on a position
        if (pos[0] == 3 and pos[1] == 0) or (pos[0] == 3 and pos[1] == 7):
            self.genMoves(1, 1)
        # c
        elif (pos[0] == 3 and pos[1] == 2) or (pos[0] == 3 and pos[1] == 9):
            self.genMoves(1, -1)
        # b
        elif (pos[0] == 5 and pos[1] == 0) or (pos[0] == 5 and pos[1] == 7):
            self.genMoves(-1, 1)
        # d
        elif (pos[0] == 5 and pos[1] == 2) or (pos[0] == 5 and pos[1] == 9):
            self.genMoves(-1, -1)
        
        # e
        if (pos[0] == 4):
            self.genMoves(-1, -1)
            self.genMoves(-1, 1)
            self.genMoves(1, -1)
            self.genMoves(1, 1)

    def genMoves(self, inX, inY):
        pos = self.getPos()
        targetPiece = self.pieces[pos[1] + inY][pos[0] + inX]
        if targetPiece == 0 or targetPiece.clr != self.clr:
            self.valid_move.append((pos[0] + inX, pos[1] + inY))

class General(Piece):
    def __init__(self, board, clr):
        super().__init__(board, clr)
        self.valid_move = []
        self.block = ((3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2),
        (3, 7), (3, 8), (3, 9), (4, 7), (4, 8), (4, 9), (5, 7), (5, 8), (5, 9))

    def drawText(self, posX, posY):
        self.board.draw_text(fontSize, '将', self.clr, posX - textMove, posY- textMove)

    def makeMoves(self):
        del self.valid_move[:]
        self.genMoves(-1, 0)
        self.genMoves(1, 0)
        self.genMoves(0, 1)
        self.genMoves(0, -1)
        
    def genMoves(self, inX, inY):
        pos = self.getPos()
        # if the target pos is in the block
        if (pos[0] + inX, pos[1] + inY) in self.block:
            targetPiece = self.pieces[pos[1] + inY][pos[0] + inX]
            if targetPiece == 0 or targetPiece.clr != self.clr:
                self.valid_move.append((pos[0] + inX, pos[1] + inY))

class Cannon(Piece):
    def __init__(self, board, clr):
        super().__init__(board, clr)
        self.valid_move = []

    def drawText(self, posX, posY):
        self.board.draw_text(fontSize, '炮', self.clr, posX - textMove, posY- textMove)

    def makeMoves(self):
        pos = self.getPos()
        del self.valid_move[:]
        counter = 0
        # up
        for i in range(pos[1] - 1, -1, -1):
            if self.pieces[i][pos[0]] == 0 :
                # if the pos is blank before the 1st encountered piece add to valid move
                if counter == 0:
                    self.valid_move.append((pos[0], i))
                # if counter != 0 but is on the top row, reset counter to 0
                elif i == 0:
                    counter = 0
            # if not blank, i.e. there is a piece
            else:
                # if first piece only increments counter
                if counter == 0 and i != 0:
                    counter += 1
                elif counter == 0 and i == 0:
                    counter = 0
                elif counter == 1:
                    counter = 0
                    if self.pieces[i][pos[0]].clr != self.clr:
                        self.valid_move.append((pos[0], i))
                        break
                    elif self.pieces[i][pos[0]].clr == self.clr:
                        break
        # down
        for i in range(pos[1] + 1, 10, 1):
            if self.pieces[i][pos[0]] == 0 :
                if counter == 0:
                    self.valid_move.append((pos[0], i))
                elif i == 9:
                    counter = 0
            else:
                if counter == 0 and i != 9:
                    counter += 1
                elif counter == 0 and i == 9:
                    counter = 0
                elif counter == 1:
                    counter = 0
                    if self.pieces[i][pos[0]].clr != self.clr:
                        self.valid_move.append((pos[0], i))
                        break
                    elif self.pieces[i][pos[0]].clr == self.clr:
                        break    
        # left
        for i in range(pos[0] - 1, -1, -1):
            if self.pieces[pos[1]][i] == 0 :
                if counter == 0:
                    self.valid_move.append((i, pos[1]))
                elif i == 0:
                    counter = 0
            else:
                if counter == 0 and i != 0:
                    counter += 1
                elif counter == 0 and i == 0:
                    counter = 0
                elif counter == 1:
                    counter = 0               
                    if self.pieces[pos[1]][i].clr != self.clr:
                        self.valid_move.append((i, pos[1]))
                        break
                    elif self.pieces[pos[1]][i].clr == self.clr:
                        break    
        # right
        for i in range(pos[0] + 1, 9, 1):
            if self.pieces[pos[1]][i] == 0 :
                if counter == 0:
                    self.valid_move.append((i, pos[1]))
                elif i == 8:
                    counter = 0
            else:
                if counter == 0 and i != 8:
                    counter += 1
                elif counter == 0 and i == 8:
                    counter = 0
                elif counter == 1:
                    counter = 0 
                    if self.pieces[pos[1]][i].clr != self.clr:
                        self.valid_move.append((i, pos[1]))
                        break
                    elif self.pieces[pos[1]][i].clr == self.clr:
                        break 

class Soldier(Piece):
    def __init__(self, board, clr):
        super().__init__(board, clr)
        self.valid_move = []

    def drawText(self, posX, posY):
        self.board.draw_text(fontSize, '卒', self.clr, posX - textMove, posY- textMove)
    
    def makeMoves(self):
        del self.valid_move[:]
        pos = self.getPos()
        # black
        if self.clr == black:
            if pos[1] != 9:
                self.genMoves(0, 1)
            if pos[1] > 4:
                if pos[0] == 0:
                    self.genMoves(1, 0)
                elif pos[0] == 8:
                    self.genMoves(-1, 0)
                else:
                    self.genMoves(-1, 0)
                    self.genMoves(1, 0)
        # red
        if self.clr == red:
            if pos[1] != 0:
                self.genMoves(0, -1)
            if pos[1] < 5:
                if pos[0] == 0:
                    self.genMoves(1, 0)
                elif pos[0] == 8:
                    self.genMoves(-1, 0)
                else:
                    self.genMoves(-1, 0)
                    self.genMoves(1, 0)     

    def genMoves(self, inX, inY):
        pos = self.getPos()
        targetPiece = self.pieces[pos[1] + inY][pos[0] + inX]
        if targetPiece == 0 or targetPiece.clr != self.clr:
            self.valid_move.append((pos[0] + inX, pos[1] + inY))       
 