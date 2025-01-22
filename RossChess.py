### RossChess! is back
import time
import pygame
import Pieces
import copy

class Chess():
    def __init__(self): ### game manager init
        #self.OpeningSequence()
        self.Board = [["" for x in range(8)] for y in range(8)] ### create 8*8 2D list to act as the board
        self.Pieces = [] ### this list contains all pieces
        self.Turn = "White" ### White will play first
        self.Winner = None
        #self.WhiteCheckActive = False ### this is a boolean to check if a king is put in check by a move, this will not catch self checks, fix later
        #self.BlackCheckActive = False ### this is a boolean to check if a king is put in check by a move, this will not catch self checks, fix later
        self.CreatePieces() ### create all pieces and add to Pieces
        #self.PMCP() ### this is for custom testing of possible moves
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

    def HighlightCyan(self,moveList):
        Cyan = (0,255,255)
        for move in moveList:
            self.Window.fill(Cyan,((move[0] * 80),( move[1] * 80), 80, 80))
        pygame.display.update()
        #print("done")
    
    def Evaluate(self):
        ### for now have both scores be positive
        # if turns out need black to be negative, simple change

        whiteScore = 0
        blackScore = 0
        for piece in self.Pieces:
            if piece.GetColour() == "White":
                whiteScore += piece.GetScore()
            else:
                blackScore += piece.GetScore()
        
        #print ("white score : ",whiteScore,"\nblack score : ",blackScore)

        # if whiteScore > blackScore:
        #     print("white +",whiteScore - blackScore)
        # elif blackScore != whiteScore:
        #     print("black +",blackScore - whiteScore)
        # else:
        #     print("even game")

        return whiteScore - blackScore

    def Promote(self,chosenPiece,colour):
        promote = input(print("Enter the piece you would like to promote to : "))
                            
        if promote == "Pawn":
            pass
        elif promote == "Rook":
            self.Pieces.append(Pieces.Rook(chosenPiece.x,chosenPiece.y,"Rook",colour,chosenPiece.GetMoveCount()))
            self.Pieces.remove(chosenPiece)
        elif promote == "Horse":
            self.Pieces.append(Pieces.Horse(chosenPiece.x,chosenPiece.y,"Horse",colour,chosenPiece.GetMoveCount()))
            self.Pieces.remove(chosenPiece)
        elif promote == "Bishop":
            self.Pieces.append(Pieces.Bishop(chosenPiece.x,chosenPiece.y,"Bishop",colour,chosenPiece.GetMoveCount()))
            self.Pieces.remove(chosenPiece)
        elif promote == "Queen":
            self.Pieces.append(Pieces.Queen(chosenPiece.x,chosenPiece.y,"Queen",colour,chosenPiece.GetMoveCount()))
            self.Pieces.remove(chosenPiece)
        ### no need for an else, this will be replace with a GUI panel


    def IsValidMove(self,checkPiece,destination):
        ### get piece and destination, return true if destination in possible moves
        possibleMoves = checkPiece.PossibleMoves(self.Pieces)
        # for piece in self.Pieces:
        #     if piece.GetPieceType() == "King" and piece.GetColour() == self.Turn:
        #         king = piece
        #         break
        
        ### get deep copy of fake pieces,
        ### for each possible move, make the move, enquire if still in check, remove from possible moves


        #call remove invalid with checkPiece.GetLocation()

        #d = self.RemoveInvalid(possibleMoves,checkPiece.GetLocation(),king)



        #### here we can check if a move will exit a check

        return destination in possibleMoves

    def GUIGamplayLoop(self):
        self.isPieceChosen = False
        run = True
        while run:
            


            Event = pygame.event.poll()
            if Event.type == pygame.QUIT:
                pygame.quit()
                break
            elif Event.type == pygame.MOUSEBUTTONDOWN:
                #print(pygame.mouse.get_pos())
                (mouseX,mouseY) = pygame.mouse.get_pos() ### get the position of the mouse
                mouseLoc = (int(mouseX / 80),int( mouseY / 80)) ### convert to the board location
                #print(mouseLoc)
                if not self.isPieceChosen: ### there is no current piece chosen
                    chosenPiece = None ### assume space is empty
                    for piece in self.Pieces: ### check all pieces for the click location
                        if piece.GetLocation() == mouseLoc and piece.GetColour() == self.Turn: ### a piece of the correct team is selected
                            chosenPiece = piece ### space is not empty, assign piece
                            self.isPieceChosen = True
                    self.GUIUpdateBoard(chosenPiece)

                else: ### a piece has been chosen, dont reference chosenPiece outside of this, except in GUIUpdateBoard()
                    ### bases to cover:
                    # selecting different piece
                    # capture move
                    # non capture move
                    peacefulMove = True ## the same piece is being selectied
                    for piece in self.Pieces: ### check all pieces for the 2nd click location
                        if piece.GetLocation() == mouseLoc and piece.GetColour() == self.Turn: ### a different piece was chosen to move
                            chosenPiece = piece ### reassing selected piece
                            self.isPieceChosen = True ### a piece is chosen
                            peacefulMove = False ### there is no move being made, so peacefulMove = False
                            break ### break the loop
                        elif piece.GetLocation() == mouseLoc: ### chosen piece is an enemy
                            ### the location of 2nd mouse click is the enemy
                            capturePiece = piece
                            if self.IsValidMove(chosenPiece,mouseLoc): ### validate input move
                                self.MovePiece(chosenPiece.GetLocation() , mouseLoc,self.Pieces,True) ### move the first piece to the capture piece
                                if capturePiece.GetPieceType() == "King":
                                    self.Winner = chosenPiece.GetColour()
                                    run = False
                            self.isPieceChosen = False ### a piece has been moved, deselect all
                            peacefulMove = False ### this was not a peaceful move
                            break
                    if peacefulMove and self.IsValidMove(chosenPiece,mouseLoc): ### non capture move is chosen and valid move
                        self.MovePiece(chosenPiece.GetLocation(), mouseLoc,self.Pieces,True)

                    if chosenPiece.GetPieceType() == "Pawn": ### if pawn moves, check if promotion possible
                        if chosenPiece.GetColour() == "White" and chosenPiece.y == 0: ### white pawn is valid for promotion
                            self.Promote(chosenPiece,"White")
                        elif chosenPiece.GetColour() == "Black" and chosenPiece.y == 7: ### black pawn is valid for promotion
                            self.Promote(chosenPiece,"Black")



                    ### at this point any move that would be made, has been made

                    ### check if a king in check
    

                    #whiteScore = self.Evaluate()
                    chosenPiece = None ### deselect all
                    self.isPieceChosen = False
                    #self.UpdateCheck()
                    self.GUIUpdateBoard(None) 
                    
                    #print("White in check :",self.WhiteCheckActive,"\nBlack in check : ",self.BlackCheckActive)


                    #print("second click")



                # self.PopulateBoard()
                # self.DisplayBoard()

                # self.MakeMove()
        print("Game Over, winner : ",self.Winner)



    def InCheck(self,King,Pieces):
        ### may cause issues !!!!

        ### search all opp peices, return true if king in check
        ### have the current king passed as a paramater, compare coords to every opp possible move
        for piece in Pieces:
            if piece.GetColour() != King.GetColour(): ### opp peice
                for move in piece.PossibleMoves(Pieces):
                    if move == King:
                        print(King.GetColour(),"King is in check")
                        return True
        return False
    
    def UpdateCheck(self):
        for piece in self.Pieces:
            if piece.GetPieceType() == "King":
                if piece.GetColour() == "White":
                    whiteKing = piece
                else:
                    blackKing = piece
        self.WhiteCheckActive = self.InCheck(whiteKing,self.Pieces)
        self.BlackCheckActive = self.InCheck(blackKing,self.Pieces)


    def ChangeTurn(self):
        if self.Turn == "White":
            self.Turn = "Black"
        else:
            self.Turn = "White"


    def StartGUIWindow(self):
        ### everythign for the GUI gameplay has to originate in here
        pygame.init() ### initialise pygame
        #print("Loading.")
        WindowSize = 640 ### set the window size
        self.Window = pygame.display.set_mode((WindowSize, WindowSize)) ### create window
        self.Window.fill((255,255,255))
        self.GUIUpdateBoard(None)
        self.GUIGamplayLoop()
                
    
    def GUIUpdateBoard(self,chosenPiece):
        #print("Loading..")
        DarkGrey = (80, 80, 80)
        DarkWhite = (200, 200, 200)
        self.Window.fill(DarkWhite)
        #print("Loading...")
        for i in range(0,640,160):
            for j in range(0,640,160):  
                self.Window.fill(DarkWhite,(i, j, 80, 80))
                self.Window.fill(DarkGrey,(i, j + 80, 80, 80))
        for i in range(80,720,160):
            for j in range(-80,720,160):  
                self.Window.fill(DarkWhite,(i, j, 80, 80))
                self.Window.fill(DarkGrey,(i, j + 80, 80, 80))

        chosenPieceMoves = []

        if chosenPiece != None: ### do not reference chosnnPiece outside of this
                    for piece in self.Pieces:
                        if piece.GetPieceType() == "King" and piece.GetColour() == self.Turn:
                            king = piece
                    chosenPieceMoves = chosenPiece.PossibleMoves(self.Pieces)
                    # print("pre cull ",chosenPieceMoves)
                    # print("black check : ",self.BlackCheckActive)
                    # d = self.RemoveInvalid(chosenPieceMoves,chosenPiece.GetLocation(),king)
                    # ########
                    # print("post cull ",d)

                    self.HighlightCyan(chosenPieceMoves)
                    #print(chosenPieceMoves)

        for piece in self.Pieces: ### for every piece remaining, concat the colour and type, get image 
            #print(piece.GetColour() + piece.GetPieceType() + "at : " , piece.x , "," , piece.y)
            spriteString = piece.GetColour() + piece.GetPieceType()
            if piece.GetLocation() in chosenPieceMoves:
                Image = pygame.image.load("sprites\\"+spriteString+"Cyan.png")
            else:
                Image = pygame.image.load("sprites\\"+spriteString+".png")
            self.Window.blit(Image,piece.GetPosition())
        pygame.display.update()
        #print("Done!")

    # define a method that will take a peice, move it to the desired location, and remove any opponent in that
    # location from self.pieces

    def RemoveInvalid(self,possibleMoves,startLoc,king):
        fakeWhiteCheck = False
        fakeBlackCheck = False
        if self.WhiteCheckActive:
            fakeWhiteCheck = True
        if self.BlackCheckActive:
            fakeBlackCheck = True
        for move in possibleMoves:
            fakePieces = copy.deepcopy(self.Pieces)
            #print("pre move",fakePieces)
            self.MovePiece(startLoc,move,fakePieces,False)
            if self.Turn == "White":
                fakeWhiteCheck = self.InCheck(king,fakePieces)
                if fakeWhiteCheck:
                    possibleMoves.remove(move)
            else:
                #print("post move",fakePieces)
                fakeBlackCheck = self.InCheck(king,fakePieces)
                if fakeBlackCheck:
                    possibleMoves.remove(move)

        return possibleMoves

    def MovePiece(self,startLoc,endLoc,gameState,real): ### this removes a piece from the board
        #print(self.Pieces)
        chosenPiece = None ### assume the chosen square is empty
        deadPiece = None ### assume the destination square is empty
        
        for piece in gameState: ### search all pieces
            if piece.GetLocation() == startLoc: ### if there is a piece at the start point, it will be moved
                chosenPiece = piece
            if piece.GetLocation() == endLoc: ### if there is a piece at the end point, it will be removed
                deadPiece = piece

        if deadPiece != None: ### remove the deadpiece if there is one
            gameState.remove(deadPiece)
        
        #print(chosenPiece.GetPieceType())
        chosenPiece.SetLocation(endLoc)
        chosenPiece.IncrementMoveCount()
        
        if real:
            self.ChangeTurn()
            self.GUIUpdateBoard(None)
        #chosenPiece.PossibleMoves(gameState)
            
        #print(chosenPiece.GetLocation())
        
        #print(gameState)

    def SelectGameMode(self):
        ### to be removed in favour of GUI selection
        GameMode = input("Please enter the number of players : > ") ### Main menu to ask for the gamemode
        while GameMode != "2" and GameMode != "1" and GameMode != "0":
            print("Please input a valid number, being 0, 1 or 2")
            GameMode = input("Please enter the number of players : > ")
        #print(GameMode)

    def DisplayPieces(self):
        for piece in self.Pieces:
            print(piece.x,piece.y)

    def DisplayBoard(self): ### display string representation of board
        print(self.__str__())

    def PMCP(self):
        self.Pieces.append(Pieces.Horse(6,6,"Horse","White",0))
        self.Pieces.append(Pieces.Rook(5,4,"Rook","Black",0))
        self.Pieces.append(Pieces.Rook(5,5,"Rook","White",0))
        self.Pieces.append(Pieces.Rook(7,4,"Rook","White",0))
        # self.Pieces.append(Pieces.Rook(2,3,"Rook","White",0))

        piece = self.Pieces[0]
        #print("s",piece.PossibleMoves(self.Pieces))

    def CreatePieces(self):
        for i in range(0,8):### populate Pawns
            self.Pieces.append(Pieces.Pawn(i,1,"Pawn","Black",0))
            self.Pieces.append(Pieces.Pawn(i,6,"Pawn","White",0))

        self.Pieces.append(Pieces.Rook(0,0,"Rook","Black",0)) ### populate all 4 Rooks
        self.Pieces.append(Pieces.Rook(7,0,"Rook","Black",0))
        self.Pieces.append(Pieces.Rook(0,7,"Rook","White",0))
        self.Pieces.append(Pieces.Rook(7,7,"Rook","White",0))

        self.Pieces.append(Pieces.Horse(1,0,"Horse","Black",0)) ### populate all 4 Horses
        self.Pieces.append(Pieces.Horse(6,0,"Horse","Black",0))
        self.Pieces.append(Pieces.Horse(1,7,"Horse","White",0))
        self.Pieces.append(Pieces.Horse(6,7,"Horse","White",0))

        self.Pieces.append(Pieces.Bishop(2,0,"Bishop","Black",0)) ### populate all 4 Bishops
        self.Pieces.append(Pieces.Bishop(5,0,"Bishop","Black",0))
        self.Pieces.append(Pieces.Bishop(2,7,"Bishop","White",0))
        self.Pieces.append(Pieces.Bishop(5,7,"Bishop","White",0))

        self.Pieces.append(Pieces.King(4,0,"King","Black",0)) ### populate all 4 Royals
        self.Pieces.append(Pieces.Queen(3,0,"Queen","Black",0))
        self.Pieces.append(Pieces.King(4,7,"King","White",0))
        self.Pieces.append(Pieces.Queen(3,7,"Queen","White",0))

    def PopulateBoard(self): ### fill the board with the pieces
        self.Board = [["" for x in range(8)] for y in range(8)] ### empty board
        for piece in self.Pieces: ### populate piece
            self.Board[piece.y][piece.x] = piece

    def GetPieceFromTuple(self,inputLocation): ### get the chosen piece from the input location
        for piece in self.Pieces:
            startLoc = (piece.x,piece.y)
            if startLoc == inputLocation: ### if the piece is present, return that piece
                return piece


    


if __name__ == "__main__":
    GameState = Chess()
    
