#GameBoard



class GameBoard:

    pieces = {
        'b_checker': u'\u25FB',
        'b_pawn': u'\u265F',
        'b_rook': u'\u265C',
        'b_knight': u'\u265E',
        'b_bishop': u'\u265D',
        'b_king': u'\u265A',
        'b_queen': u'\u265B',
        'w_checker': u'\u25FC',
        'w_pawn': u'\u2659',
        'w_rook': u'\u2656',
        'w_knight': u'\u2658',
        'w_bishop': u'\u2657',
        'w_king': u'\u2654',
        'w_queen': u'\u2655'
    }
    plainGameBoard = []
    playBoard = []

    def __init__(self, pieces, plainGameBoard, playBoard):

        self.pieces = pieces
        self.plainGameBoard = plainGameBoard
        self.playBoard = playBoard

        pass

    #Initalizeing the game baord here
    def initGB(self):

        self.buildGameBoard(self)
        self.placeGamePieces(self)

        for row in self.playBoard:
            print(row)

        print(self.playBoard)

        return self.playBoard

    #This creates the board itself
    def buildGameBoard(self):

        row = [self.pieces['b_checker'], self.pieces['w_checker']]*4

        for i in range(8):
            self.plainGameBoard.append(row if i % 2 == 0 else row[::-1])

    #This palces the pieces in the starting orientation
    def placeGamePieces(self):

        blackRows = [[self.pieces['b_rook'], self.pieces['b_knight'], self.pieces['b_bishop'], self.pieces['b_queen'], self.pieces['b_king'], self.pieces['b_bishop'], self.pieces['b_knight'], self.pieces['b_rook']],
                      [self.pieces['b_pawn'], self.pieces['b_pawn'], self.pieces['b_pawn'], self.pieces['b_pawn'], self.pieces['b_pawn'], self.pieces['b_pawn'], self.pieces['b_pawn'], self.pieces['b_pawn']]]

        whiteRows = [[self.pieces['w_rook'], self.pieces['w_knight'], self.pieces['w_bishop'], self.pieces['w_queen'], self.pieces['w_king'], self.pieces['w_bishop'], self.pieces['w_knight'], self.pieces['w_rook']],
                      [self.pieces['w_pawn'], self.pieces['w_pawn'], self.pieces['w_pawn'], self.pieces['w_pawn'], self.pieces['w_pawn'], self.pieces['w_pawn'], self.pieces['w_pawn'], self.pieces['w_pawn']]]

        self.playBoard = self.plainGameBoard
        self.playBoard[0] = blackRows[0]
        self.playBoard[1] = blackRows[1]
        self.playBoard[-1] = whiteRows[0]
        self.playBoard[-2] = whiteRows[1]

    def reportPositions(self, playerOneTurn):

        report = []
        pieces = list(self.pieces.values())
        blackPieces = pieces[1:7]
        whitePieces = pieces[8:14]

        if playerOneTurn == True:
            for row in self.playBoard:
                for piece in row:
                    if piece in whitePieces:
                        report.append(piece)
        else:
            for row in self.playBoard:
                for piece in row:
                    if piece in blackPieces:
                        report.append(piece)

        return report