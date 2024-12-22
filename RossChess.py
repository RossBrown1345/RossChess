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

Horse
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

have a list containing all pieces, to allow the same pieces to be moved without creating new instances

backend will use 0 - 7, for x and y, front end will include A to H and 1 to 8
'''


import time
import pygame

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
        self.Pieces = [] ### this list contains all pieces
        self.CreatePieces() ### create all pieces and add to Pieces
        self.PopulateBoard() ### populate board
        self.DisplayBoard() ### display board
        self.GUIWindow()

        
        '''testPiece = self.getPieceFromTuple((4,6))
        testPiece.move((4,4)) # test move
        self.populateBoard()
        self.displayBoard()'''

    def GUIWindow(self):
        pygame.init() ### initialise pygame
        print("Loading.")
        WindowSize = 640 ### set the window size
        run = True
        Window = pygame.display.set_mode((WindowSize, WindowSize)) ### create window
        self.GUIPopulateBoard(Window)
        

        while run:
            Event = pygame.event.poll()
            if Event.type == pygame.QUIT:
                break




        Cyan = (0,255, 255) ### colour for available moves
        Selectedpiece = False ### no piece is selected

    def GUIPopulateBoard(self, Window):
        print("Loading..")
        DarkGrey = (80, 80, 80)
        DarkWhite = (200, 200, 200)
        Window.fill(DarkWhite)
        print("Loading...")
        for i in range(0,640,160):
            for j in range(0,640,160):  
                Window.fill(DarkWhite,(i, j, 80, 80))
                Window.fill(DarkGrey,(i, j + 80, 80, 80))
        for i in range(80,720,160):
            for j in range(-80,720,160):  
                Window.fill(DarkWhite,(i, j, 80, 80))
                Window.fill(DarkGrey,(i, j + 80, 80, 80))
        print("Done!")


        for piece in self.Pieces:
            if piece.type == "Pawn":
                if piece.colour == "White":
                    Image = pygame.image.load('sprites\WhitePawn.png')
                else:
                    Image = pygame.image.load('sprites\BlackPawn.png')
            elif piece.type == "Rook":
                if piece.colour == "White":
                    Image = pygame.image.load('sprites\WhiteRook.png')
                else:
                    Image = pygame.image.load('sprites\BlackRook.png')
            elif piece.type == "Horse":
                if piece.colour == "White":
                    Image = pygame.image.load('sprites\WhiteHorse.png')
                else:
                    Image = pygame.image.load('sprites\BlackHorse.png')
            elif piece.type == "Bishop":
                if piece.colour == "White":
                    Image = pygame.image.load('sprites\WhiteBishop.png')
                else:
                    Image = pygame.image.load('sprites\BlackBishop.png')
            elif piece.type == "Queen":
                if piece.colour == "White":
                    Image = pygame.image.load('sprites\WhiteQueen.png')
                else:
                    Image = pygame.image.load('sprites\BlackQueen.png')
            elif piece.type == "King":
                if piece.colour == "White":
                    Image = pygame.image.load('sprites\WhiteKing.png')
                else:
                    Image = pygame.image.load('sprites\BlackKing.png')        
            Window.blit(Image,piece.Position)








    def DisplayPieces(self):
        for piece in self.Pieces:
            print(piece.x,piece.y)

    def DisplayBoard(self): ### display string representation of board
        print(self.__str__())

    def CreatePieces(self):
        for i in range(0,8):### populate Pawns
            self.Pieces.append(Pawn(i,1,"Pawn","Black",0))
            self.Pieces.append(Pawn(i,6,"Pawn","White",0))

        self.Pieces.append(Rook(0,0,"Rook","Black",0)) ### populate all 4 Rooks
        self.Pieces.append(Rook(0,7,"Rook","Black",0))
        self.Pieces.append(Rook(7,0,"Rook","White",0))
        self.Pieces.append(Rook(7,7,"Rook","White",0))

        self.Pieces.append(Rook(1,0,"Horse","Black",0)) ### populate all 4 Horses
        self.Pieces.append(Rook(6,0,"Horse","Black",0))
        self.Pieces.append(Rook(1,7,"Horse","White",0))
        self.Pieces.append(Rook(6,7,"Horse","White",0))

        self.Pieces.append(Rook(2,0,"Bishop","Black",0)) ### populate all 4 Bishops
        self.Pieces.append(Rook(5,0,"Bishop","Black",0))
        self.Pieces.append(Rook(2,7,"Bishop","White",0))
        self.Pieces.append(Rook(5,7,"Bishop","White",0))

        self.Pieces.append(Rook(4,0,"King","Black",0)) ### populate all 4 Royals
        self.Pieces.append(Rook(3,0,"Queen","Black",0))
        self.Pieces.append(Rook(4,7,"King","White",0))
        self.Pieces.append(Rook(3,7,"Queen","White",0))

    def PopulateBoard(self): ### fill the board with the pieces
        self.Board = [["" for x in range(8)] for y in range(8)] ### empty board
        for piece in self.Pieces: ### populate piece
            self.Board[piece.y][piece.x] = piece

    def GetPieceFromTuple(self,inputLocation): ### get the chosen piece from the input location
        for piece in self.Pieces:
            startLoc = (piece.x,piece.y)
            if startLoc == inputLocation: ### if the piece is present, return that piece
                return piece


    def __str__(self): ###create a string representation of the game
        BoardFormat = "| {:^2}{:^2}"
        BoardAsString = "------------------------------------------------" + "\n"
        for j in range(8):
            for i in range(8):
                CurrentPiece = self.Board[j][i]
                if CurrentPiece != "":
                    BoardAsString += BoardFormat.format(CurrentPiece.GetColour()[0], CurrentPiece.GetPieceType()[0])
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
    def __init__(self,x,y,type,colour,moveCount):
        self.x = x
        self.y = y
        self.type = type
        self.colour = colour
        self.moveCount = 0 ### may need to change to moveCount, or remove all

    ### getters
    def GetLocation(self): 
        return (self.x, self.y)
    def GetColour(self):
        return self.colour
    def GetMoveCount(self):
        return self.moveCount
    def GetPieceType(self):
        return self.type

class Pawn(Piece):
    def __init__(self,x,y,type,colour,moveCount):
        super().__init__(x,y,type,colour,moveCount) ### call parent init
        self.Score = 1
        YPosition = (self.y * 80) ### multiply x and y locations by 80 to get the location on the display
        XPosition = (self.x * 80)
        self.Position = (XPosition, YPosition) ### return a tuple of location

    def Move(self,newLocation):
        self.x = newLocation[0]
        self.y = newLocation[1]

    
class Rook(Piece):
    def __init__(self,x,y,type,colour,moveCount):
        super().__init__(x,y,type,colour,moveCount) ### call parent init
        self.Score = 5
        YPosition = (self.y * 80) ### multiply x and y locations by 80 to get the location on the display
        XPosition = (self.x * 80)
        self.Position = (XPosition, YPosition) ### return a tuple of location

class Horse(Piece):
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
    
