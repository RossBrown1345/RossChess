### RossChess! is back
'''
make board 2d list

have parent class for pieces with attributes:
score
colour
name
location
moveCount ### this is needed to pawns to en passant and rooks to castle

and methods:
move

Pawn
score : 1

Rook
score : 5

Knight
score: 3

Bishop
score : 3

Queen
score : 9

King
score : 100
isCastleValid
isInCheck


make board methods
capturing and score keeping
'''


import time

class Chess():
    def __init__(self): ### game manager init
        print("\n")
        time.sleep(1)
        print("Hello Professor")
        time.sleep(2)
        print("How about a nice game of")
        time.sleep(1.5)
        print("__________                         _________  .__                             ._.")
        time.sleep(0.3)
        print("\______   \  ____    ______  ______\_   ___ \ |  |__    ____    ______  ______| |")
        time.sleep(0.3)
        print("|       _/ /  _ \  /  ___/ /  ___//    \  \/ |  |  \ _/ __ \  /  ___/ /  ___/ | |")
        time.sleep(0.3)
        print("|    |   \(  <_> ) \___ \  \___ \ \     \____|   Y  \\  ___/  \___ \  \___ \   | |")
        time.sleep(0.3)
        print("|____|_  / \____/ /____  >/____  > \______  /|___|  / \___  >/____  >/____  >  \|")
        time.sleep(0.3) 
        print("    \/              \/      \/         \/      \/      \/      \/      \/      O")
        print("\n")
        time.sleep(1)
        self.Board = [["" for x in range(8)] for y in range(8)] ### create 8*8 2D list to act as the board
        self.displayBoard()

    def displayBoard(self):
        print(self.__str__())


    def __str__(self): ###create a string representation of the game
        BoardFormat = "| {:^2}{:^2}"
        BoardAsString = "------------------------------------------------" + "\n"
        for j in range(8):
            for i in range(8):
                CurrentPiece = self.Board[j][i]
                if CurrentPiece != "":
                    BoardAsString += BoardFormat.format(CurrentPiece.getColour()[0], CurrentPiece.getPieceType()[0])
                else:
                    BoardAsString += BoardFormat.format("","")
                if j == 0 and i == 7:
                    BoardAsString += "|" + "--8--" + "\n"
                elif j == 1 and i == 7:
                    BoardAsString += "|" + "--7--" + "\n"
                elif j == 2 and i == 7:
                    BoardAsString += "|" + "--6--" + "\n"
                elif j == 3 and i == 7:
                    BoardAsString += "|" + "--5--" + "\n"
                elif j == 4 and i == 7:
                    BoardAsString += "|" + "--4--" + "\n"
                elif j == 5 and i == 7:
                    BoardAsString += "|" + "--3--" + "\n"
                elif j == 6 and i == 7:
                    BoardAsString += "|" + "--2--" + "\n"
                elif j == 7 and i == 7:
                    BoardAsString += "|" + "--1--" + "\n"
            BoardAsString += "------------------------------------------------" + "\n"
        BoardAsString += "---A-----B-----C-----D-----E-----F-----G-----H---" + "\n"
        return BoardAsString
            

class Piece(): ### parent class for all pieces
    def __init__(self,x,y,colour,moveCount):
        self.x = x
        self.y = y
        self.colour = colour
        self.moveCount = 0

    def getLocation(self):
        return (self.x, self.y)
    def getColour(self):
        return self.colour
    def getMoveCount(self):
        return self.moveCount

class Pawn(Piece):
    def __init__(self,x,y,type,colour,moveCount):
        super().__init__(x,y,type,colour,moveCount) ### call parent init
        self.Score = 1
        YPosition = (self.y * 80) ### multiply x and y locations by 80 to get the location on the display
        XPosition = (self.x * 80)
        self.Position = (XPosition, YPosition) ### return a tuple of location

    def move(self,newLocation):
        pass

    def getPieceType(self):
        return self.colour
    
class Rook(Piece):
    def __init__(self,x,y,type,colour,moveCount):
        super().__init__(x,y,type,colour,moveCount) ### call parent init
        self.Score = 5
        YPosition = (self.y * 80) ### multiply x and y locations by 80 to get the location on the display
        XPosition = (self.x * 80)
        self.Position = (XPosition, YPosition) ### return a tuple of location

class Knight(Piece):
    def __init__(self,x,y,type,colour,moveCount):
        super().__init__(x,y,type,colour,moveCount) ### call parent init
        self.Score = 3
        YPosition = (self.y * 80) ### multiply x and y locations by 80 to get the location on the display
        XPosition = (self.x * 80)
        self.Position = (XPosition, YPosition) ### return a tuple of location
    
class Bishop(Piece):
    def __init__(self,x,y,type,colour,moveCount):
        super().__init__(x,y,type,colour,moveCount) ### call parent init
        self.Score = 3
        YPosition = (self.y * 80) ### multiply x and y locations by 80 to get the location on the display
        XPosition = (self.x * 80)
        self.Position = (XPosition, YPosition) ### return a tuple of location
    
class Queen(Piece):
    def __init__(self,x,y,type,colour,moveCount):
        super().__init__(x,y,type,colour,moveCount) ### call parent init
        self.Score = 9
        YPosition = (self.y * 80) ### multiply x and y locations by 80 to get the location on the display
        XPosition = (self.x * 80)
        self.Position = (XPosition, YPosition) ### return a tuple of location
    
class King(Piece):
    def __init__(self,x,y,type,colour,moveCount):
        super().__init__(x,y,type,colour,moveCount) ### call parent init
        self.Score = 100
        YPosition = (self.y * 80) ### multiply x and y locations by 80 to get the location on the display
        XPosition = (self.x * 80)
        self.Position = (XPosition, YPosition) ### return a tuple of location
    
    def isCastleValid():
        pass

    def isInCheck():
        pass


if __name__ == "__main__":
    GameState = Chess()
    
