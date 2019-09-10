from config import fontSize, black, red, textMove

class Piece:
    # super class
    def __init__(self, board, clr):
        self.board = board
        if clr == 'b':
            self.clr = black
        else:
            self.clr = red


class Chariot(Piece):
    def __init__(self, board, clr):
        super().__init__(board, clr)
        self.valid_move = []
    
    def drawText(self, posX, posY):
        self.board.draw_text(fontSize, '车', self.clr, posX - textMove, posY- textMove)

    def makeMoves(self):
        pass


class Horse(Piece):
    def __init__(self, board, clr):
        super().__init__(board, clr)
        self.valid_move = []

    def drawText(self, posX, posY):
        self.board.draw_text(fontSize, '马', self.clr, posX - textMove, posY- textMove)

class Elephant(Piece):
    def __init__(self, board, clr):
        super().__init__(board, clr)
        self.valid_move = []

    def drawText(self, posX, posY):
        self.board.draw_text(fontSize, '相', self.clr, posX - textMove, posY- textMove)

class Advisor(Piece):
    def __init__(self, board, clr):
        super().__init__(board, clr)
        self.valid_move = []

    def drawText(self, posX, posY):
        self.board.draw_text(fontSize, '士', self.clr, posX - textMove, posY- textMove)

class General(Piece):
    def __init__(self, board, clr):
        super().__init__(board, clr)
        self.valid_move = []

    def drawText(self, posX, posY):
        self.board.draw_text(fontSize, '将', self.clr, posX - textMove, posY- textMove)

class Cannon(Piece):
    def __init__(self, board, clr):
        super().__init__(board, clr)
        self.valid_move = []

    def drawText(self, posX, posY):
        self.board.draw_text(fontSize, '炮', self.clr, posX - textMove, posY- textMove)

class Soldier(Piece):
    def __init__(self, board, clr):
        super().__init__(board, clr)
        self.valid_move = []

    def drawText(self, posX, posY):
        self.board.draw_text(fontSize, '卒', self.clr, posX - textMove, posY- textMove)