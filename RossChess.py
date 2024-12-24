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
        #self.OpeningSequence()
        self.Board = [["" for x in range(8)] for y in range(8)] ### create 8*8 2D list to act as the board
        self.Pieces = [] ### this list contains all pieces
        self.CreatePieces() ### create all pieces and add to Pieces
        self.PopulateBoard() ### populate board
        self.DisplayBoard() ### display board
        self.StartGUIWindow() ### start GUI window
    
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

    def OpeningSequence(self):
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

    def StartGUIWindow(self):
        ### everythign for the GUI gameplay has to originate in here
        pygame.init() ### initialise pygame
        print("Loading.")
        WindowSize = 640 ### set the window size
        self.Window = pygame.display.set_mode((WindowSize, WindowSize)) ### create window
        self.Window.fill((255,255,255))
        self.GUIUpdateBoard()
        run = True
        while run:
            Event = pygame.event.poll()
            if Event.type == pygame.QUIT:
                pygame.quit()
                break
            elif Event.type == pygame.MOUSEBUTTONDOWN:

                self.MovePiece((6,6),(1,1))

                self.GUIUpdateBoard()
                self.PopulateBoard()
                self.DisplayBoard()

                # self.MakeMove()
                
    
    def GUIUpdateBoard(self):
        print("Loading..")
        DarkGrey = (80, 80, 80)
        DarkWhite = (200, 200, 200)
        self.Window.fill(DarkWhite)
        print("Loading...")
        for i in range(0,640,160):
            for j in range(0,640,160):  
                self.Window.fill(DarkWhite,(i, j, 80, 80))
                self.Window.fill(DarkGrey,(i, j + 80, 80, 80))
        for i in range(80,720,160):
            for j in range(-80,720,160):  
                self.Window.fill(DarkWhite,(i, j, 80, 80))
                self.Window.fill(DarkGrey,(i, j + 80, 80, 80))
        for piece in self.Pieces: ### for every piece remaining, concat the colour and type, get image 
            #print(piece.GetColour() + piece.GetPieceType() + "at : " , piece.x , "," , piece.y)
            spriteString = piece.GetColour() + piece.GetPieceType()
            Image = pygame.image.load("sprites\\"+spriteString+".png")
            self.Window.blit(Image,piece.Position)
        pygame.display.update()
        print("Done!")

    # define a method that will take a peice, move it to the desired location, and remove any opponent in that
    # location from self.pieces

    def MovePiece(self,startLoc,endLoc): ### this removes a piece from the board
        #print(self.Pieces)
        chosenPiece = None ### assume the chosen square is empty
        deadPiece = None ### assume the destination square is empty
        for piece in self.Pieces: ### search all pieces
            if (piece.x,piece.y) == startLoc: ### if there is a piece at the start point, it will be moved
                chosenPiece = piece
            if (piece.x,piece.y) == endLoc: ### if there is a piece at the end point, it will be removed
                deadPiece = piece
        if deadPiece != None: ### remove the deadpiece if there is one
            self.Pieces.remove(deadPiece)
        if chosenPiece != None:
            chosenPiece.IncrementMoveCount()
            chosenPiece.SetLocation(endLoc)
            chosenPiece.PossibleMoves(self.Pieces)
            print(chosenPiece.PossibleMoves(self.Pieces))
        #print(chosenPiece.GetLocation())
        
        #print(self.Pieces)







    def SelectGameMode(self):
        ### to be removed in favour of GUI selection
        GameMode = input("Please enter the number of players : > ") ### Main menu to ask for the gamemode
        while GameMode != "2" and GameMode != "1" and GameMode != "0":
            print("Please input a valid number, being 0, 1 or 2")
            GameMode = input("Please enter the number of players : > ")
        print(GameMode)
        Cyan = (0,255, 255) ### colour for available moves
        Selectedpiece = False ### no piece is selected


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
        self.Pieces.append(Rook(7,0,"Rook","Black",0))
        self.Pieces.append(Rook(0,7,"Rook","White",0))
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


    
            

class Piece(): ### parent class for all pieces
    def __init__(self,x,y,type,colour,moveCount):
        self.x = x
        self.y = y
        self.type = type
        self.colour = colour
        self.moveCount = 0 ### may need to change to moveCount, or remove all
        ### multiply x and y locations by 80 to get the location on the display
        self.Position = (self.x * 80, self.y * 80) ### return a tuple of location

    def PossibleMoves(self,board):
        ### method to be overided, board is the list Chess.Pieces,
        pass
    
    def IncrementMoveCount(self):
        self.moveCount+=1

    ### getters
    def GetLocation(self): 
        return (self.x, self.y)
    def GetColour(self):
        return self.colour
    def GetMoveCount(self):
        return self.moveCount
    def GetPieceType(self):
        return self.type

    ### setters
    def SetLocation(self,NewLoc):
        self.x = NewLoc[0] ### update the new x and ys
        self.y = NewLoc[1]
        self.UpdatePosition() ### update the position of the GUI

    def UpdatePosition(self):
        self.Position = (self.x * 80, self.y * 80) ### return a tuple of location

class Pawn(Piece):
    def __init__(self,x,y,type,colour,moveCount):
        super().__init__(x,y,type,colour,moveCount) ### call parent init
        self.Score = 1

    def PossibleMoves(self,board):
        # if nothing in front, move 1 space forward
        # if first move, allow option for 2 space forward
        # if opponent 1 space diagonal
        # so long as in bounds
        ### the code for this can be slightly more exact as it is less mathematical

        (startX,startY) = self.GetLocation()
        possibleMoves = []
        oneSpacePossible = True
        if self.GetMoveCount() > 0:
            twoSpacePossible  = False
        else:
            twoSpacePossible = True

        if self.GetColour() == "White": ##get white moves
            oneSpace = (startX, startY -1) ## the four potential moves of a pawn, enpassant to be added later
            twoSpace = (startX, startY - 2)
            leftCap = (startX - 1 , startY - 1)
            rightCap = (startX + 1, startY - 1)
            for piece in board: ### search all the opp pieces
                checkLoc = piece.GetLocation()
                if checkLoc == twoSpace:
                    twoSpacePossible = False
                elif checkLoc == oneSpace:
                    oneSpacePossible = False
                if piece.GetColour() == "Black": ### check the black pieces and append possible captures
                    if checkLoc == leftCap:
                        possibleMoves.append(leftCap)
                    elif checkLoc == rightCap:
                        possibleMoves.append(rightCap)
            if oneSpacePossible: ### append possible moves
                possibleMoves.append(oneSpace)
            if twoSpacePossible:
                possibleMoves.append(twoSpace)
            return possibleMoves
        
        else:
            oneSpace = (startX, startY +1) ## the four potential moves of a pawn, enpassant to be added later
            twoSpace = (startX, startY + 2)
            leftCap = (startX - 1 , startY + 1)
            rightCap = (startX + 1, startY + 1)
            for piece in board: ### search all the opp pieces
                checkLoc = piece.GetLocation()
                if checkLoc == twoSpace:
                    twoSpacePossible = False
                elif checkLoc == oneSpace:
                    oneSpacePossible = False
                if piece.GetColour() == "White": ### check the white pieces and append possible captures
                    if checkLoc == leftCap:
                        possibleMoves.append(leftCap)
                    elif checkLoc == rightCap:
                        possibleMoves.append(rightCap)
            if oneSpacePossible: ### append possible moves
                possibleMoves.append(oneSpace)
            if twoSpacePossible:
                possibleMoves.append(twoSpace)
            return possibleMoves

    
class Rook(Piece):
    def __init__(self,x,y,type,colour,moveCount):
        super().__init__(x,y,type,colour,moveCount) ### call parent init
        self.Score = 5
    
    def PossibleMoves(self,board):
        # up to 8 spaces horizontal or vertical
        # if not moved, and empty spaces between it and King
        # who has also not moved, castle is allowed
        # so long as in bounds
        pass

class Horse(Piece):
    def __init__(self,x,y,type,colour,moveCount):
        super().__init__(x,y,type,colour,moveCount) ### call parent init
        self.Score = 3

    def PossibleMoves(self,board):
        # either 2 vertical and 1 horizontal or 2 horizontal 1 vertical
        # so long as in bounds
        pass
        
    
class Bishop(Piece):
    def __init__(self,x,y,type,colour,moveCount):
        super().__init__(x,y,type,colour,moveCount) ### call parent init
        self.Score = 3

    def PossibleMoves(self,board):
    # up to 8 spaces diagonally
    # so long as in bounds
        pass

    
class Queen(Piece):
    def __init__(self,x,y,type,colour,moveCount):
        super().__init__(x,y,type,colour,moveCount) ### call parent init
        self.Score = 9
    def PossibleMoves(self,board):
    # combination of rook and bishop moves
    # so long as in bounds
        pass
    
class King(Piece):
    def __init__(self,x,y,type,colour,moveCount):
        super().__init__(x,y,type,colour,moveCount) ### call parent init
        self.Score = 100
    
    def PossibleMoves(self,board):
    #1 move in any direction
    # if movecount = 0 and rook with LOS has movecount = 0, allow castle
    # so long as in bounds
        pass
    
    def isCastleValid():
        pass

    def isInCheck():
        pass


if __name__ == "__main__":
    GameState = Chess()
    
