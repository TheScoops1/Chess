#Game.py


from GameBoard import GameBoard

class Game:

    playerOneTurn = True
    playerTwoTurn = False
    turnCount = 0

    def __init__(self):

        self.playerOneTurn = True
        self.playerTwoTurn = False
        self.turnCount = 0
        self.startGame()

        pass

    def GameOp(self):
        pass

    def startGame(self):
        board = GameBoard.initGB(GameBoard)

        print('Welcome to Scoops Chess Game')
        self.takePlayerTurn()


    def takePlayerTurn(self):
        if self.turnCount % 2 == 0:
            self.whitesTurn()
            self.turnCount += 1
        else:
            self.blacksturn()
            self.turnCount += 1

    def whitesTurn(self):
        print('White, What piece do you want to move?')
        print(GameBoard.reportPositions(GameBoard, self.playerOneTurn))

    def blacksTurn(self):
        print('Black, What piece do you want to move?')
