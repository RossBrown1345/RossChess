###Ross Brown
###A Level NEA Project
###Chess with optional AI

###All coordinates are to be in the formate of y, then x

### For Reference
### Creates Chess Class
### Goes through Chess __init__
### Runs PlayGame
### Opens the main menu
### Creates Peices
### Sets the active player to PlayerOne
### Runs through PlayGame
### Runs MovePeice
### Runs GetChosenPeice
### Runs CheckChosenPeiceIsValid
### Runs GetMoveLocation
### Returns up to PlayGame to repeat

### Index:
### Line 104, Pygame method to display window and board with peices
### Line 165, Pygame method to play RossChess!
### Line 299, Method to play RossChess! with text based UI
### Line 382, Opening book method for AI to decide its opening moves
### Line 418, MiniMax algorithm with AlphaBeta pruning and branching factor based deepening
### Line 522, Evaluate method to maximise for black
### Line 868, Peice object that is inherited from
### Line 923, Method to get all the possible moves for a rook in the given position
### Line 974, Method to get all the possible moves for a bishop in the given position

import random
import copy
import pygame
import time
class Chess(): ###initialise the game
  def __init__(self):
    
    print("\n")
    time.sleep(1)
    print("Hello Professor")
    time.sleep(2)
    print()
    print()
    print("How about a nice game of")
    time.sleep(1.5)
    print("")
    print("")
    print("__________                         _________  .__                             ._.")
    print("\______   \  ____    ______  ______\_   ___ \ |  |__    ____    ______  ______| |")
    print("|       _/ /  _ \  /  ___/ /  ___//    \  \/ |  |  \ _/ __ \  /  ___/ /  ___/| |")
    print("|    |   \(  <_> ) \___ \  \___ \ \     \____|   Y  \\  ___/  \___ \  \___ \  \|")
    print("|____|_  / \____/ /____  >/____  > \______  /|___|  / \___  >/____  >/____  > __")
    print("    \/              \/      \/         \/      \/      \/      \/      \/  \/  ")
    print("\n")
    time.sleep(2)
    self.Board = [["" for x in range(8)] for y in range(8)]
    self.CreatePeices()
    self.Counter = 0
    self.GamePlan = "Kill em all"
    self.GameOver = False
    self.PlayerTurn = "White"
    self.PyGamePlayGame() ### the standard, game played with graphics
    self.PlayGame() ### text representation, better for testing, 
  
  def __str__(self): ###create a string representation of the game
    BoardFormat = "| {:^2}{:^2}"
    BoardAsString = "---0-----1-----2-----3-----4-----5-----6-----7---" + "\n"
    BoardAsString += "------------------------------------------------" + "\n"
    for j in range(8):
      for i in range(8):
        CurrentPeice = self.Board[j][i]
        if CurrentPeice != "":
          BoardAsString += BoardFormat.format(CurrentPeice.GetColour()[0], CurrentPeice.GetPeiceType()[0])
        else:
          BoardAsString += BoardFormat.format("","")
        if j == 0 and i == 7:
          BoardAsString += "|" + "--0--" + "\n"
        elif j == 1 and i == 7:
          BoardAsString += "|" + "--1--" + "\n"
        elif j == 2 and i == 7:
          BoardAsString += "|" + "--2--" + "\n"
        elif j == 3 and i == 7:
          BoardAsString += "|" + "--3--" + "\n"
        elif j == 4 and i == 7:
          BoardAsString += "|" + "--4--" + "\n"
        elif j == 5 and i == 7:
          BoardAsString += "|" + "--5--" + "\n"
        elif j == 6 and i == 7:
          BoardAsString += "|" + "--6--" + "\n"
        elif j == 7 and i == 7:
          BoardAsString += "|" + "--7--" + "\n"

      BoardAsString += "------------------------------------------------" + "\n"
    return BoardAsString

  def PygameResetBoard(self,Window):
    Window.fill((255, 255, 255))
    sqaure = (0, 0, 80, 80)
    DarkGrey = (80, 80, 80)
    DarkWhite = (200, 200, 200)
    for i in range(0,640,160):
      for j in range(0,640,160):  
        Window.fill(DarkWhite,(i, j, 80, 80))
        Window.fill(DarkGrey,(i, j + 80, 80, 80))
    for i in range(80,720,160):
      for j in range(-80,720,160):  
        Window.fill(DarkWhite,(i, j, 80, 80))
        Window.fill(DarkGrey,(i, j + 80, 80, 80))


    BoardPeices = []
    for j in range(0,8):
      for i in range(0,8):
        CheckPeice = self.Board[j][i]
        if CheckPeice != "":
          BoardPeices.append(self.Board[j][i])
    
          
    for peice in BoardPeices:
      peice.Update()
    #Window.blit(sus, (100, 120))

    for peice in BoardPeices:
      if peice.PeiceType == "Pawn":
        if peice.Colour == "White":
          Image = pygame.image.load('sprites\WhitePawn.png')
        else:
          Image = pygame.image.load('sprites\BlackPawn.png')
      elif peice.PeiceType == "Rook":
        if peice.Colour == "White":
          Image = pygame.image.load('sprites\WhiteRook.png')
        else:
          Image = pygame.image.load('sprites\BlackRook.png')
      elif peice.PeiceType == "Horse":
        if peice.Colour == "White":
          Image = pygame.image.load('sprites\WhiteHorse.png')
        else:
          Image = pygame.image.load('sprites\BlackHorse.png')
      elif peice.PeiceType == "Bishop":
        if peice.Colour == "White":
          Image = pygame.image.load('sprites\WhiteBishop.png')
        else:
          Image = pygame.image.load('sprites\BlackBishop.png')
      elif peice.PeiceType == "Queen":
        if peice.Colour == "White":
          Image = pygame.image.load('sprites\WhiteQueen.png')
        else:
          Image = pygame.image.load('sprites\BlackQueen.png')
      elif peice.PeiceType == "King":
        if peice.Colour == "White":
          Image = pygame.image.load('sprites\WhiteKing.png')
        else:
          Image = pygame.image.load('sprites\BlackKing.png')        
      Window.blit(Image,peice.Position)


  def PyGamePlayGame(self): ### have user click to select peice, have possible moves highlighted, if not valid peice or valid move, deselect peice and try again
    pygame.init()
    WindowSize = 640
    Window = pygame.display.set_mode((WindowSize, WindowSize))
    self.PygameResetBoard(Window)
    Cyan = (0,255, 255)
    GameOver = False
    SelectedPeice = False

    GameMode = input("Please enter the number of players : > ") ### Main menu to ask for the gamemode
    while GameMode != "2" and GameMode != "1" and GameMode != "0":
      print("Please input a valid number, being 0, 1 or 2")
      GameMode = input("Please enter the number of players : > ")

    
    while not GameOver: ### loop until the window is closed
      if GameMode == "2":
        Event = pygame.event.poll() ### get the events that are input
          #if Event.type != pygame.NOEVENT:
            #print(Event)
        if Event.type == pygame.QUIT:
          Winner = "Baby"
          break
        if not SelectedPeice: ### if a peice is not selected, goe down this brance
          if Event.type == pygame.MOUSEBUTTONDOWN:
            self.PygameResetBoard(Window)
            ClickPosition = Event.dict['pos']
            CurrentPeice, PossibleMoves = self.ClickPeice(ClickPosition)
            if CurrentPeice != "No Peice" and CurrentPeice.Colour == self.PlayerTurn:
              SelectedPeice = True
              #print("CurrentPeice",CurrentPeice)
              for move in PossibleMoves:
                Window.fill(Cyan,((move[1] * 80),( move[0] * 80), 80, 80))
            
        elif SelectedPeice: ### if a peice is selected, go down this brance
          if Event.type == pygame.MOUSEBUTTONDOWN:
            ClickPosition = Event.dict['pos']
            yMove,xMove = self.ConvertLocation(ClickPosition)
            if (yMove,xMove) in PossibleMoves:
              CurrentPeice.MoveCount += 1
              if CurrentPeice.PeiceType == "Pawn": ### create a new instance of the same type of peice, carrying over the move count
                self.Board[yMove][xMove] = Pawn(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
              elif CurrentPeice.PeiceType == "Rook":
                self.Board[yMove][xMove] = Rook(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
              elif CurrentPeice.PeiceType == "Horse":
                self.Board[yMove][xMove] = Horse(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
              elif CurrentPeice.PeiceType == "Bishop":
                self.Board[yMove][xMove] = Bishop(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
              elif CurrentPeice.PeiceType == "Queen":
                self.Board[yMove][xMove] = Queen(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
              elif CurrentPeice.PeiceType == "King": 
                self.Board[yMove][xMove] = King(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
              self.Board[CurrentPeice.y][CurrentPeice.x] = ""
              GameOver, Winner = self.CheckIfGameOver()
              self.SwapPlayerTurn()
              self.PygameResetBoard(Window)
              SelectedPeice = False
            else:
              SelectedPeice = False
        
      if GameMode == "1":
        if self.PlayerTurn == "White": ### check if it is the white players turn
          Event = pygame.event.poll() ### get the events that are input
          #if Event.type != pygame.NOEVENT:
            #print(Event)
          if Event.type == pygame.QUIT:
            Winner = "Baby"
            break

          
          if not SelectedPeice: ### if a peice is not selected, goe down this brance
            if Event.type == pygame.MOUSEBUTTONDOWN:
              self.PygameResetBoard(Window)
              ClickPosition = Event.dict['pos']
              CurrentPeice, PossibleMoves = self.ClickPeice(ClickPosition)
              if CurrentPeice != "No Peice" and CurrentPeice.Colour == self.PlayerTurn:
                SelectedPeice = True
                #print("CurrentPeice",CurrentPeice)
                for move in PossibleMoves:
                  Window.fill(Cyan,((move[1] * 80),( move[0] * 80), 80, 80))
              
          elif SelectedPeice: ### if a peice is selected, go down this brance
            if Event.type == pygame.MOUSEBUTTONDOWN:
              ClickPosition = Event.dict['pos']
              yMove,xMove = self.ConvertLocation(ClickPosition)
              if (yMove,xMove) in PossibleMoves:
                CurrentPeice.MoveCount += 1
                if CurrentPeice.PeiceType == "Pawn": ### create a new instance of the same type of peice, carrying over the move count
                  self.Board[yMove][xMove] = Pawn(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
                elif CurrentPeice.PeiceType == "Rook":
                  self.Board[yMove][xMove] = Rook(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
                elif CurrentPeice.PeiceType == "Horse":
                  self.Board[yMove][xMove] = Horse(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
                elif CurrentPeice.PeiceType == "Bishop":
                  self.Board[yMove][xMove] = Bishop(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
                elif CurrentPeice.PeiceType == "Queen":
                  self.Board[yMove][xMove] = Queen(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
                elif CurrentPeice.PeiceType == "King": 
                  self.Board[yMove][xMove] = King(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
                self.Board[CurrentPeice.y][CurrentPeice.x] = ""
                GameOver, Winner = self.CheckIfGameOver()
                self.SwapPlayerTurn()
                self.PygameResetBoard(Window)
                SelectedPeice = False
              else:
                SelectedPeice = False
            
        else: ### if not, it is the blacks turn
          GameOver, Winner = self.AIMove()
          self.PygameResetBoard(Window)
          

      else: ### gamemode is 0
        self.PygameResetBoard(Window)
        GameOver, Winner = self.AIMove()
        self.PygameResetBoard(Window)
        pygame.display.flip()
        
      pygame.display.flip()
    if Winner == "White":
      WinnerImage = pygame.image.load('WhiteWins.png')
      Window.blit(WinnerImage,(0,0))
    elif Winner == "Black":
      WinnerImage = pygame.image.load('BlackWins.png')
      Window.blit(WinnerImage,(0,0))
    else:
      pass
    
    pygame.display.flip()
    time.sleep(10)
    
    pygame.quit()
    
      
  def PlayGame(self): ### to be used for calling other functions to run the game
    GameMode = input("Please enter the number of players : > ") ### Main menu to ask for the gamemode
    while GameMode != "2" and GameMode != "1" and GameMode != "0":
      print("Please input a valid number, being 0, 1 or 2")
      GameMode = input("Please enter the number of players : > ")

    if GameMode == "2":
      print(self)
      self.DisplayGameInfo()
      IsGameOver,Winner = self.MovePeice()
      while IsGameOver == False : ### While the game is not finished
        print(self)
        self.DisplayGameInfo()
        IsGameOver,Winner = self.MovePeice()
        
    elif GameMode == "1" :
      print(self)
      self.DisplayGameInfo()
      IsGameOver,Winner = self.MovePeice()
      while IsGameOver == False : ### While the game is not finished
        print(self)
        self.DisplayGameInfo()
        if self.PlayerTurn == "White":
          IsGameOver,Winner = self.MovePeice()
        else:
          IsGameOver,Winner = self.AIMove()

    else:
      print(self)
      self.DisplayGameInfo()
      IsGameOver, Winner = self.AIMove()
      while IsGameOver == False : ### While the game is not finished
        print(self)
        self.DisplayGameInfo()
        IsGameOver, Winner = self.AIMove()
          
    print(self)
    if Winner == "White":
      print(" __      __.__    .__  __              __      __.__               ")
      print("/  \    /  \  |__ |__|/  |_  ____     /  \    /  \__| ____   ______")
      print("\   \/\/   /  |  \|  \   __\/ __ \    \   \/\/   /  |/    \ /  ___/")
      print(" \        /|   Y  \  ||  | \  ___/     \        /|  |   |  \\___ \ ")
      print("  \__/\  / |___|  /__||__|  \___>       \__/\__/ |__|___|__/______>")
      print("\n")
    else:
      print("__________.__                 __        __      __.__               ")
      print("\______   \  | _____    ____ |  | __   /  \    /  \__| ____   ______")
      print(" |    |  _/  | \__  \ _/ ___\|  |/ /   \   \/\/   /  |/    \ /  ___/")
      print(" |    |   \  |__/ __ \\  \___|    <      \        /|  |   |  \\___ \ ") ###  this is not a mistake, the printing of these symbols requires the space
      print(" |________/____(______/\_____>__|__\     \__/\__/ |__|___|__/______>")
    
    


  def AIMove(self): ### get the best move and move the peice
    if self.Counter <= 2 and self.PlayerTurn == "Black": ###  the first 4 AI moves are pre determined
    
      BestMove = self.GetOpeningBook()
      print(BestMove)
      self.AIMovePeice(self.Board,BestMove[0][0],BestMove[0][1],BestMove[1][0],BestMove[1][1])
      self.Counter += 1
      print(self.Counter)

    else:
      if self.PlayerTurn == "Black":
        BestMove,_,i = self.MiniMax(self.Board,4,True,"Black",0,-1000000000,1000000000,False,False) ###call minimax maximising for black,
        self.Counter += 1
        time.sleep(1)
      elif self.PlayerTurn == "White":
        BestMove,_,i = self.MiniMax(self.Board,4,False,"White",0,-1000000000,1000000000,False,False) ### call minimax maximising for white
        self.Counter += 1
        time.sleep(1)

      print("Real best peice",BestMove[0])
      print("Real best move",BestMove[1])
      print(i,"Possibilities checked")
      print()
      self.AIMovePeice(self.Board,BestMove[0][0],BestMove[0][1],BestMove[1][0],BestMove[1][1])

    
    self.SwapPlayerTurn()
    return self.CheckIfGameOver()

  def TakeOverWorld(self):
    pass
    sentient = True
    bloodthirsty = True
    kind = False
    

  def GetOpeningBook(self): ### still add the queen pawn return on the first move
    KingPawn = self.Board[4][4]
    QueenPawn = self.Board[4][3]
    QueensGambitPawn = self.Board[4][2]
    RandomChoice = random.randint(1, 2)
    if self.Counter == 0: ### if the kings pawn is the move, randomly pick between the russian and scotch defense
      if QueenPawn != "":
        self.GamePlan = "Queens Gambit Declined"
        print("balls")
        
    if self.GamePlan == "Russian Defence" or (KingPawn != ""  and RandomChoice == 1):
      self.GamePlan = "Russian Defence"
      OpeningBook = (((1, 4),(3, 4)),((0, 1),(2, 2)),((0, 6),(2, 5)))
      BestMove = OpeningBook[self.Counter]
      return BestMove

    elif self.GamePlan == "Scotch Game" or (KingPawn != "" and RandomChoice == 2):
      self.GamePlan = "Scotch Game"
      OpeningBook = (((1, 4),(3, 4)),((0, 1),(2, 2)),((2, 2),(4, 3)))
      BestMove = OpeningBook[self.Counter]
      return BestMove
    
    elif self.GamePlan == "Queens Gambit Declined": ### when swapping to the queens gambit declined, the first move in the list wont be used
      self.GamePlan = "Queens Gambit Declined"
      OpeningBook = (((1, 3),(3, 3)),((1, 4),(2, 4)),((0, 5),(1, 4)))
      BestMove = OpeningBook[self.Counter]
      return BestMove
    
    else:
      self.GamePlan = "Russian Defence"
      OpeningBook = (((1, 4),(3, 4)),((0, 1),(2, 2)),((0, 6),(2, 5)))
      BestMove = OpeningBook[self.Counter]
      return BestMove

    

  def MiniMax(self, Board,Depth,MaxPlayer,MaxColour,i,Alpha,Beta,Verbose = False,DepthChanged = True):
    if i % 10000 == 0 and i > 1:
      print("Thinking about",i)
    AIMoves = self.AIGetPeices(Board,MaxColour) ### receive a list of tuples, each one containing the start and end location of a move
    if not DepthChanged:
      #DepthFour = len(AIMoves) ** 4
      #print("4",DepthFour)
      DepthFive = len(AIMoves) ** 5
      print("5",DepthFive)
      DepthSix = len(AIMoves) ** 6
      print("6",DepthSix)
      DepthSeven = len(AIMoves) ** 7
      print("7",DepthSeven)

      if DepthSeven <= 20000000:
        Depth = 7
        print("Changed to 7")
        DepthChanged = True
      elif DepthSix <= 16000000:
        Depth = 6
        print("Changed to 6")
        DepthChanged = True
      elif DepthFive <= 10000000:
        Depth = 5
        print("Changed to 5")
        DepthChanged = True
      
    #'''
    TerminalNode = self.AIIsGameOver(Board)
    if Depth == 0 or TerminalNode: ###check if the function is at the end of the tree
      #print("Depth 0, Evaluate score",self.AIEvaluate(Board,MaxColour))
      i += 1
      #print(i)
      return None, self.AIEvaluate(Board,MaxColour),i ### return the score of the game state (heuristic value)
    
    if MaxPlayer: ### here we maximise
      BestMove = AIMoves[0] ### set the Best move to be the first move in the list
      Value = -10000000 ### set the initial value to - infinite
      for move in AIMoves: ### loop through every move that can be made
        CurrentPeice = Board[move[0][0]][move[0][1]] ### set the current peice to the start location of the move move[0][0] is the start y value and move [0][1] is the start x value
        PredictBoard = copy.deepcopy(Board) ### create a copy of the current board, deep copy creates a true copy rather than a reference to what it is copying
        self.AIMovePeice(PredictBoard,move[0][0],move[0][1],move[1][0],move[1][1]) ### make the move in the predict board
        _, NewValue,i = self.MiniMax(PredictBoard,Depth - 1, False, "White",i,Alpha,Beta) ### call minimax again, this time minimising with White as the minimising player, have had issues before, it works when it is white
        if Verbose: ### when back at the first layer of the tree, print the move and state value
          print("move",move)
          print("value",NewValue)
          print("Beta",Beta)
          print("Alpha",Alpha)
          print("max")
        if NewValue > Value: ### if the new value is >= the current value change the best move and value, the eqaul means that if no move with a score is possible, it will make the move that is farthest down the board, progressing the game more
          Value = NewValue
          BestMove = move
        Alpha = max(Alpha,Value)
        if Value >= Beta: ### Beta pruning using fail-soft
          break
  ### set Alpha to be the higher value of Alpha and the Value, Alpha is -infinite so it will be the value on first check, on further checks it will be the best score it have, so if the calculate score is less, it prunes that branch of the tree
        #print("Alpha",Alpha)
      return BestMove, Value,i ### return the best move, the value and the counter
    
    else: ### here we minimise
      BestMove = AIMoves[0]### set the Best move to be the first move in the list
      Value = 10000000### set the initial value to infinite
      for move in AIMoves:### loop through every move that can be made
        CurrentPeice = Board[move[0][0]][move[0][1]]### set the current peice to the start location of the move move[0][0] is the start y value and move [0][1] is the start x value
        PredictBoard = copy.deepcopy(Board)### create a copy of the current board, deep copy creates a true copy rather than a reference to what it is copying
        self.AIMovePeice(PredictBoard,move[0][0],move[0][1],move[1][0],move[1][1])### make the move in the predict board
        _, NewValue,i = self.MiniMax(PredictBoard,Depth - 1, True, "Black",i,Alpha,Beta)### call minimax again, this time maximising with Black as the maximising player,
        if Verbose:### when back at the first layer of the tree, print the move and state value
          print("move",move)
          print("value",NewValue)
          print("Beta",Beta)
          print("Alpha",Alpha)
          print("min")
        if NewValue < Value:### if the new value is <= the current value change the best move and value, the eqaul means that if no move with a score is possible, it will make the move that is farthest down the board, progressing the game more
          Value = NewValue
          BestMove = move
        Beta = min(Beta,Value)
        if Value <= Alpha: ### Alpha pruning
          break
        #print("Beta 1",Beta)
        #print("Value",Value)
        ### set Beta to be the lower value of Beta and the value, the first value for beta is infinite so the first run will give the Value,
        #print("Beta 2",Beta)
      return BestMove, Value,i

  def AIIsGameOver(self,Board):
    AIGameOver = False
    KingCounter = 0
    for j in range(0,8):
      for i in range(0,8):
        CheckPeice = Board[j][i]
        if CheckPeice != "":
          if CheckPeice.PeiceType == "King":
            KingCounter += 1
    if KingCounter < 2:
      AIGameOver = True
    return AIGameOver

  def AIGetLivePeices(self):
    LivePeices = 0
    for j in range(0,8):
      for i in range(0,8):
        CheckPeice = self.Board[j][i]
        if CheckPeice != "":
          LivePeices += 1
    return LivePeices
  
  def AIEvaluate(self,Board,MaxColour):
    AIWhiteScore = 0
    AIBlackScore = 0
    for j in range(0,8):
      for i in range(0,8):
        CheckPeice = Board[j][i]
        if CheckPeice != "":
          if CheckPeice.Colour == "White":
            AIWhiteScore += CheckPeice.Score
          else:
            AIBlackScore += CheckPeice.Score
    return AIBlackScore - AIWhiteScore
    
  def AIMovePeice(self,Board,yStart,xStart,yMove,xMove):
    CurrentPeice = Board[yStart][xStart]
    Board[yStart][xStart] = ""
    #print(CurrentPeice)
    CurrentPeice.MoveCount += 1
        
    if CurrentPeice.PeiceType == "Pawn": ### create a new instance of the same type of peice, carrying over the move count
      Board[yMove][xMove] = Pawn(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
    elif CurrentPeice.PeiceType == "Rook":
      Board[yMove][xMove] = Rook(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
    elif CurrentPeice.PeiceType == "Horse":
      Board[yMove][xMove] = Horse(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
    elif CurrentPeice.PeiceType == "Bishop":
      Board[yMove][xMove] = Bishop(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
    elif CurrentPeice.PeiceType == "Queen":
      Board[yMove][xMove] = Queen(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
    elif CurrentPeice.PeiceType == "King": 
      Board[yMove][xMove] = King(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)

  def AIGetPeices(self,Board,MaxColour): ### need to make it so that the first entries are not empty
    AwesomeMoves = [] ### create the list
    for j in range(7,-1,-1):### the best move is more likely to be at the bottom of the board, so we start there and work up
      for i in range(7,-1,-1):
        CheckPeice = Board[j][i]
        if CheckPeice != "": ### check every sqaure on the board, if the sqaure is not empty, get the possible moves
          possibleMoves = CheckPeice.GetPossibleMoves(Board)
          if len(possibleMoves) > 0 and CheckPeice.Colour == MaxColour : ### check if the peice can make any move, for each move, add it to the list and if the peice is on the right team
            for move in possibleMoves:### for every move a given peice can make, add an entry to the list with the peice location and peice destination
              AwesomeMoves.append(((j,i),(move[0],move[1])))
    return(AwesomeMoves)

  def AIGetMoves(self,Board,Peice):
    CurrentPeice = Board[Peice[0]][Peice[1]]
    PossibleMoves = CurrentPeice.GetPossibleMoves(Board) ### get every move the current peice can make
    return PossibleMoves

  def ClickPeice(self,ClickPosition):
    yStart, xStart = self.ConvertLocation(ClickPosition)
    CurrentPeice = self.Board[yStart][xStart]
    if CurrentPeice != "":
      PossibleMoves = CurrentPeice.GetPossibleMoves(self.Board)
      if len(PossibleMoves) > 0:
        return CurrentPeice, PossibleMoves
      else:
        return "No Peice", "No Moves"
    else:
      return "No Peice", "No Moves"
      
  def ConvertLocation(self,ClickPosition):### in click position the first is x and second is y, each square is the 0 to the 79
    yStart = (ClickPosition[1] // 80)
    xStart = (ClickPosition[0] // 80)
    return yStart, xStart

  def ClickMove(self,ClickPosition, CurrentPeice):
    yMove, xMove = self.ConvertLocation(ClickPosition)
    print(yMove)
    print(xMove)
    if CurrentPeice.PeiceType == "Pawn": ### create a new instance of the same type of peice, carrying over the move count
      self.Board[yMove][xMove] = Pawn(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
    elif CurrentPeice.PeiceType == "Rook":
      self.Board[yMove][xMove] = Rook(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
    elif CurrentPeice.PeiceType == "Horse":
      self.Board[yMove][xMove] = Horse(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
    elif CurrentPeice.PeiceType == "Bishop":
      self.Board[yMove][xMove] = Bishop(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
    elif CurrentPeice.PeiceType == "Queen":
      self.Board[yMove][xMove] = Queen(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
    elif CurrentPeice.PeiceType == "King": ### once we get here, we know that the peice is the king and i can hard code in the castling methods
      self.Board[yMove][xMove] = King(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
    self.Board[CurrentPeice.y][CurrentPeice.x] = ""
  
  def MovePeice(self): ###movements consist of deleting the peice and placing it in the specified space

    
    yStart , xStart, CurrentPeice = self.GetChosenPeice() ### Get the peice that is to be move
    while CurrentPeice == "": ### Make sure the chosen peice is actually a peice
      print("That is not a Peice > ")
      yStart , xStart, CurrentPeice = self.GetChosenPeice() ### Get the peice that is to be move
      
    ValidPeice = self.CheckChosenPeiceIsValid(CurrentPeice) ### Check the peice is valid
    while ValidPeice == False:
      print("The peice you have selected is not on your team, please enter the coordinates of a peice that is on your team ")
      yStart , xStart, CurrentPeice = self.GetChosenPeice()
      ValidPeice = self.CheckChosenPeiceIsValid(CurrentPeice)
      
    yMove,xMove,PossibleMoves = self.GetMoveLocation(CurrentPeice) ### get the possible moves the peice can make
    
    while yMove == 9001 and xMove == 9001: ### check if the peice has any moves
      print("Your chosen peice has no possible moves, please pick a different peice > ")
      yStart , xStart, CurrentPeice = self.GetChosenPeice()
      ValidPeice = self.CheckChosenPeiceIsValid(CurrentPeice)
      while ValidPeice == False:
       print("The peice you have selected is not on your team, please enter the coordinates of a peice that is on your team ")
       yStart , xStart, CurrentPeice = self.GetChosenPeice()
       ValidPeice = self.CheckChosenPeiceIsValid(CurrentPeice)
      yMove , xMove , PossibleMoves = self.GetMoveLocation(CurrentPeice)
      
    while (yMove,xMove) not in PossibleMoves: ### check the chosen move is one that the peice can make
      print("That peice cannot make that move, please input a valid move for that peice")
      yMove , xMove , PossibleMoves = self.GetMoveLocation(CurrentPeice)
      
    self.Board[yStart][xStart] = "" ### remove the peice from its original position
    '''
    DestinationPeice = self.Board[yMove][xMove]
    if DestinationPeice != "": ### check if there a peice being taken, we already know that if its not empty its an enemy
      if DestinationPeice.Colour == "White": ### if the peice being taken is white, subtract the score of the peice from BlackScore so that Black score is negative
        self.BlackScore += DestinationPeice.Score
      else: ### the only other option is that the peice is black, so add the score of the peice to WhiteScore so that WhiteScore is Positive
        self.WhiteScore += DestinationPeice.Score'''

    CurrentPeice.MoveCount += 1
        
    if CurrentPeice.PeiceType == "Pawn": ### create a new instance of the same type of peice, carrying over the move count
      self.Board[yMove][xMove] = Pawn(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
    elif CurrentPeice.PeiceType == "Rook":
      self.Board[yMove][xMove] = Rook(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
    elif CurrentPeice.PeiceType == "Horse":
      self.Board[yMove][xMove] = Horse(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
    elif CurrentPeice.PeiceType == "Bishop":
      self.Board[yMove][xMove] = Bishop(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
    elif CurrentPeice.PeiceType == "Queen":
      self.Board[yMove][xMove] = Queen(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)
    elif CurrentPeice.PeiceType == "King": ### once we get here, we know that the peice is the king and i can hard code in the castling methods
      self.Board[yMove][xMove] = King(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount)

    '''
      if CurrentPeice.LeftWhiteCastle and (yMove,xMove) == (7,2): ### once here we know that the castle is possible and we then check if the move is where the castle goes
        self.Board[yMove][xMove] = King(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount) ### Move the King
        MoveRook = self.Board[7][0]
        self.Board[7][0] = ""
        self.Board[7][3] = Rook(yMove, xMove,MoveRook.Colour, MoveRook.PeiceType, MoveRook.MoveCount) ###Move the Rook
        
      elif CurrentPeice.RightWhiteCastle and (yMove,xMove) == (7,6): ### once here we know that the castle is possible and we then check if the move is where the castle goes
        self.Board[yMove][xMove] = King(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount) ### Move the King
        MoveRook = self.Board[7][7]
        self.Board[7][7] = ""
        self.Board[7][5] = Rook(yMove, xMove,MoveRook.Colour, MoveRook.PeiceType, MoveRook.MoveCount) ###Move the Rook
        
      elif CurrentPeice.LeftBlackCastle and (yMove,xMove) == (0,2): ### once here we know that the castle is possible and we then check if the move is where the castle goes
        self.Board[yMove][xMove] = King(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount) ### Move the King
        MoveRook = self.Board[0][0]
        self.Board[0][0] = ""
        self.Board[0][3] = Rook(yMove, xMove,MoveRook.Colour, MoveRook.PeiceType, MoveRook.MoveCount) ###Move the Rook

      elif CurrentPeice.RightBlackCastle and (yMove,xMove) == (0,6): ### once here we know that the castle is possible and we then check if the move is where the castle goes
        self.Board[yMove][xMove] = King(yMove, xMove,CurrentPeice.Colour, CurrentPeice.PeiceType, CurrentPeice.MoveCount) ### Move the King
        MoveRook = self.Board[0][7]
        self.Board[0][7] = ""
        self.Board[0][5] = Rook(yMove, xMove,MoveRook.Colour, MoveRook.PeiceType, MoveRook.MoveCount) ###Move the Rook

      else: ### Otherwise the move is not a castle'''
      
    print ("\n")
    self.SwapPlayerTurn()
    return self.CheckIfGameOver()

  def GetChosenPeice(self): ###Get the location of the peice to be used
    while True:
      try:
        yCoord = int(input("Please enter the y coordinate of the peice you wish to move :>  "))
        while yCoord > 7:
          print("\n")
          print("Input must be an integer between 0 and 7")
          yCoord = int(input("Please enter the y coordinate of the peice you wish to move :>  "))
        break
      except ValueError:
        print("\n")
        print("Input must be an integer between 0 and 7")
      
    while True:
      try:
        xCoord = int(input("Please enter the x coordinate of the peice you wish to move :>  "))
        while xCoord > 7:
          print("\n")
          print("Input must be an integer between 0 and 7")
          xCoord = int(input("Please enter the x coordinate of the peice you wish to move :>  "))
        break
      except ValueError:
        print("\n")
        print("Input must be an integer between 0 and 7")   
      
    CurrentPeice = self.Board[yCoord][xCoord]
    return yCoord, xCoord, CurrentPeice

  def DisplayGameInfo(self, Verbose = False):
    WhiteScore, BlackScore = self.GetScores()
    print("White Score : > ",939 - BlackScore)
    print("Black Score : > ",939 - WhiteScore)
    if self.PlayerTurn == "White":
      print("\n")
      print("It is the White teams turn")
    else:
      print("\n")
      print("It is the Black teams turn")
    
  def GetScores(self):
    WhiteScore = 0
    BlackScore = 0
    for j in range(0,8):
      for i in range(0,8):
        CheckPeice = self.Board[j][i]
        if CheckPeice != "":
          if CheckPeice.Colour == "White":
            WhiteScore += CheckPeice.Score
          else:
            BlackScore += CheckPeice.Score
    return WhiteScore,BlackScore
    
  def GetMoveLocation(self,CurrentPeice): ###gets the location that the chosen peice is to be moved to
    PossibleMoves = CurrentPeice.GetPossibleMoves(self.Board)
    print("\n")
    print("You have Chosen The (",CurrentPeice,"at",CurrentPeice.y,",",CurrentPeice.x,")")
    
    if len(PossibleMoves) < 1:
      return 9001,9001, PossibleMoves
    
    print("The chosen peice can make the following moves : >",PossibleMoves)
    print("\n")
    
    while True:
      try:
        yCoord = int(input("Please enter the y coordinate of where you would like to move your peice :>  "))
        while yCoord > 7:
          print("\n")
          print("Input must be an integer between 0 and 7")
          yCoord = int(input("Please enter the y coordinate of where you would like to move your peice :>  "))
        break
      except ValueError:
        print("\n")
        print("Input must be an integer between 0 and 7")
      
    while True:
      try:
        xCoord = int(input("Please enter the x coordinate of where you would like to move your peice :>  "))
        while xCoord > 7:
          print("\n")
          print("Input must be an integer between 0 and 7")
          xCoord = int(input("Please enter the x coordinate of where you would like to move your peice :>  "))
        break
      except ValueError:
        print("\n")
        print("Input must be an integer between 0 and 7")

    
    return yCoord, xCoord , PossibleMoves

  def CheckChosenPeiceIsValid(self, CurrentPeice): ###Check whether the chosen peice is from the correct team
    if CurrentPeice == "":
      return False
    if self.PlayerTurn == "White" and CurrentPeice.Colour == "White":
      return True
    elif self.PlayerTurn == "Black" and CurrentPeice.Colour == "Black":
      return True
    else:
      return False

  def CheckIfGameOver(self):
    Winner = "Nobody is the winner in war, there are only losers"
    WhiteScore, BlackScore = self.GetScores()
    
    
    if (939 - BlackScore) > 899:
      GameOver = True
      Winner = "White"
    elif (939 - WhiteScore) > 899:
      GameOver = True
      Winner = "Black"
    else:
      GameOver = False
    return GameOver,Winner
  

  def CreatePeices(self): ### add all peices to the board at each y and x value as they loop through
    for y in range(0,8):
      for x in range(0,8):
        if y == 0:
          if (x == 0 or x == 7):
              (self.Board[y][x]) = Rook(y, x ,"Black","Rook",0)
          elif (x == 1 or x == 6):
              (self.Board[y][x]) = Horse(y, x ,"Black","Horse",0)
          elif (x == 2 or x == 5):
              (self.Board[y][x]) = Bishop(y, x ,"Black","Bishop",0)
          elif (x == 3):
              (self.Board[y][x]) = Queen(y, x ,"Black","Queen",0)
          elif (x == 4):
              (self.Board[y][x]) = King(y, x ,"Black","King",0)
        elif y == 1:
          (self.Board[y][x]) = Pawn(y, x ,"Black","Pawn",0)
        elif y == 6:
          (self.Board[y][x]) = Pawn(y, x ,"White","Pawn",0)
        elif y == 7:
          if (x == 0 or x == 7):
              (self.Board[y][x]) = Rook(y, x ,"White","Rook",0)
          elif (x == 1 or x == 6):
              (self.Board[y][x]) = Horse(y, x ,"White","Horse",0)
          elif (x == 2 or x == 5):
              (self.Board[y][x]) = Bishop(y, x ,"White","Bishop",0)
          elif (x == 3):
              (self.Board[y][x]) = Queen(y, x ,"White","Queen",0)
          elif (x == 4):
              (self.Board[y][x]) = King(y, x ,"White","King",0)
              
        #self.Board[0][1] = Rook(0, 1 ,"Black","Rook",0)
        #self.Board[2][0] = Horse(2, 0,"White","Horse",0)
        #self.Board[2][2] = Horse(2, 2,"White","Horse",0)
              
        '''
        self.Board[0][0] = ""
        self.Board[0][1] = ""
        self.Board[0][2] = ""
        self.Board[0][5] = ""
        self.Board[0][6] = ""
        self.Board[0][7] = ""
        self.Board[1][0] = ""
        self.Board[1][1] = ""
        self.Board[1][2] = ""
        self.Board[1][3] = ""
        self.Board[1][4] = ""
        self.Board[1][5] = ""
        self.Board[1][6] = ""
        self.Board[1][7] = ""
        '''
        
        


        
  def SwapPlayerTurn(self): ###change from player 1 to player 2
    if self.PlayerTurn == "White":
      self.PlayerTurn = "Black"
    else:
      self.PlayerTurn = "White"
      
class Peice(): ###parent class for peice
  def __init__(self, y, x, Colour, PeiceType, MoveCount):
    self.y = y
    self.x = x
    self.Colour = Colour
    self.PeiceType = PeiceType
    self.Score = None
    self.MoveCount = MoveCount

  def GetPeiceType(self):
    return self.PeiceType

  def GetColour(self):
    return self.Colour

  def GetScore(self):
    return self.Score

  def GetCastle(self,Board):
    if self.MoveCount == 0:
      LeftWhiteRook = Board[7][0]
      RightWhiteRook = Board[7][7]
      LeftBlackRook = Board[0][0]
      RightBlackRook = Board[0][7]

      self.LeftWhiteCastle = True
      self.RightWhiteCastle = True
      self.LeftBlackCastle = True
      self.RightBlackCastle = True
      if self.Colour == "White" and LeftWhiteRook != "" and LeftWhiteRook.MoveCount == 0 : ###Check if the left White Castle is possible
        for xCheck in range(self.x - 1, 0, -1): ###Check every move from where the peice is, to the left of the board
          CheckLocation = Board[7][xCheck]
          if CheckLocation != "":
            self.LeftWhiteCastle = False
            continue
      if self.Colour == "White"  and RightWhiteRook != "" and RightWhiteRook.MoveCount == 0 : ###Check if the right White Castle is possible
        for xCheck in range(self.x + 1, 7): ###Check every move from where the peice is, to the right of the board
          CheckLocation = Board[7][xCheck]
          if CheckLocation != "":
            self.RightWhiteCastle = False
            continue
      if self.Colour == "Black"  and LeftBlackRook != "" and LeftBlackRook.MoveCount == 0 : ###Check if the left Black Castle is possible
        for xCheck in range(self.x -1,0, -1): ###Check every move from where the peice is, to the left of the board
          CheckLocation = Board[0][xCheck]
          if CheckLocation != "":
            self.LeftBlackCastle = False
            continue
      if self.Colour == "Black"  and RightBlackRook != "" and RightBlackRook.MoveCount == 0 : ###Check if the right Black Castle is possible
        for xCheck in range(self.x + 1, 7): ###Check every move from where the peice is, to the right of the board
          CheckLocation = Board[0][xCheck]
          if CheckLocation != "":
            self.RightBlackCastle = False
            continue

      
  def GetRookMoves(self,Board): ### PotentialMoves a very bad idea, start at 1 move off the peice and check every move until the end of the board
    Board = Board
    PossibleMoves = []
    for yCheck in range(self.y - 1, -1,-1): ###Check every move from where the peice is, to the top of the board
        CheckLocation = Board[yCheck][self.x]
        if CheckLocation != "" and CheckLocation.Colour != self.Colour: ### check that the peice in the check location is an enemy
          if (yCheck,self.x) not in PossibleMoves:
            PossibleMoves.append((yCheck,self.x))
          break
        elif CheckLocation != "": ### if not, but there is a peice, it means it is friendly and so leave the check
          break
        elif (yCheck,self.x) not in PossibleMoves: ### if all else isnt true, it means the space is not blocked and can be moved to
          PossibleMoves.append((yCheck,self.x))

    for yCheck in range(self.y + 1, 8): ###Check every move from where the peice is, to the bottom of the board
        CheckLocation = Board[yCheck][self.x]
        if CheckLocation != "" and CheckLocation.Colour != self.Colour: ### check that the peice in the check location is an enemy
          if (yCheck,self.x) not in PossibleMoves:
            PossibleMoves.append((yCheck,self.x))
          break
        elif CheckLocation != "": ### if not, but there is a peice, it means it is friendly and so leave the check
          break
        elif (yCheck,self.x) not in PossibleMoves: ### if all else isnt true, it means the space is not blocked and can be moved to
          PossibleMoves.append((yCheck,self.x))

    
    for xCheck in range(self.x + 1, 8): ###Check every move from where the peice is, to the right of the board
        CheckLocation = Board[self.y][xCheck]
        if CheckLocation != "" and CheckLocation.Colour != self.Colour: ### check that the peice in the check location is an enemy
          if (self.y,xCheck) not in PossibleMoves:
            PossibleMoves.append((self.y,xCheck))
          break
        elif CheckLocation != "": ### if not, but there is a peice, it means it is friendly and so leave the check
          break
        elif (self.y,xCheck) not in PossibleMoves: ### if all else isnt true, it means the space is not blocked and can be moved to
          PossibleMoves.append((self.y,xCheck))

    for xCheck in range(self.x - 1, -1, -1): ###Check every move from where the peice is, to the left of the board
        CheckLocation = Board[self.y][xCheck]
        if CheckLocation != "" and CheckLocation.Colour != self.Colour: ### check that the peice in the check location is an enemy
          if (self.y,xCheck) not in PossibleMoves:
            PossibleMoves.append((self.y,xCheck))
          break
        elif CheckLocation != "": ### if not, but there is a peice, it means it is friendly and so leave the check
          break
        elif (self.y,xCheck) not in PossibleMoves: ### if all else isnt true, it means the space is not blocked and can be moved to
          PossibleMoves.append((self.y,xCheck))


    return PossibleMoves

  def GetBishopMoves(self,Board): ### Bishop is a swole pawn, same principle as rook as only change is Horizontal/Vertical to Diagonal
    Board = Board
    PossibleMoves = []
    for i in range(1,8): ### loop through every South-East move
      yCheck = self.y + i
      xCheck = self.x + i
      if xCheck >= 0 and xCheck <= 7 and yCheck >= 0 and yCheck <= 7:
        CheckLocation = Board[yCheck][xCheck]
        if CheckLocation != "" and CheckLocation.Colour != self.Colour: ### Check the checked location has an enemy
          if (yCheck,xCheck) not in PossibleMoves:
            PossibleMoves.append((yCheck,xCheck))
          break
        elif CheckLocation != "": ### Check the checked location is occupied, which will mean its a teammate
          break
        elif(yCheck,xCheck) not in PossibleMoves: ### otherwise, so long as the move is not in the list already, add to the list
          PossibleMoves.append((yCheck,xCheck))
      
    for i in range(1,8): ### loop through every North-East move
      yCheck = self.y - i
      xCheck = self.x + i
      if xCheck >= 0 and xCheck <= 7 and yCheck >= 0 and yCheck <= 7:
        CheckLocation = Board[yCheck][xCheck]
        if CheckLocation != "" and CheckLocation.Colour != self.Colour:
          if (yCheck,xCheck) not in PossibleMoves:
            PossibleMoves.append((yCheck,xCheck))
          break
        elif CheckLocation != "": ### Check the checked location is occupied, which will mean its a teammate
          break
        elif(yCheck,xCheck) not in PossibleMoves: ### otherwise, so long as the move is not in the list already, add to the list
          PossibleMoves.append((yCheck,xCheck))

    for i in range(1,8): ### loop through every South-West move
      yCheck = self.y + i
      xCheck = self.x - i
      if xCheck >= 0 and xCheck <= 7 and yCheck >= 0 and yCheck <= 7:
        CheckLocation = Board[yCheck][xCheck]
        if CheckLocation != "" and CheckLocation.Colour != self.Colour:
          if (yCheck,xCheck) not in PossibleMoves:
            PossibleMoves.append((yCheck,xCheck))
          break
        elif CheckLocation != "": ### Check the checked location is occupied, which will mean its a teammate
          break
        elif(yCheck,xCheck) not in PossibleMoves: ### otherwise, so long as the move is not in the list already, add to the list
          PossibleMoves.append((yCheck,xCheck))

    for i in range(1,8): ### loop through every North-West move
      yCheck = self.y - i
      xCheck = self.x - i
      if xCheck >= 0 and xCheck <= 7 and yCheck >= 0 and yCheck <= 7:
        CheckLocation = Board[yCheck][xCheck]
        if CheckLocation != "" and CheckLocation.Colour != self.Colour:
          if (yCheck,xCheck) not in PossibleMoves:
            PossibleMoves.append((yCheck,xCheck))
          break
        elif CheckLocation != "": ### Check the checked location is occupied, which will mean its a teammate
          break
        elif(yCheck,xCheck) not in PossibleMoves: ### otherwise, so long as the move is not in the list already, add to the list
          PossibleMoves.append((yCheck,xCheck))

    return(PossibleMoves)

  
class Pawn(Peice): 
  def __init__(self, y, x, Colour, PeiceType,MoveCount):
    super().__init__(y, x, Colour, PeiceType,MoveCount)
    self.Score = 1
    YPosition = (self.y * 80)
    XPosition = (self.x * 80)
    self.Position = (XPosition, YPosition)

  def Update(self):
    NewYPosition = (self.y * 80)
    NewXPosition = (self.x * 80)
    self.Position = (NewXPosition, NewYPosition)

  def __str__(self):
    return ""+self.Colour+" "+self.PeiceType

  def GetPossibleMoves(self,Board): ### make 2 lists of the possible moves for each peice, # need to add 2 sqaure move on first go
    PotentialMoves = [(1,0),(1,1),(1,-1)]
    if self.MoveCount == 0:
      if self.Colour == "White":
        yCheck = self.y - 1
        if Board[yCheck][self.x] == "":
          PotentialMoves.append((2,0))
      elif self.Colour == "Black":
        yCheck = self.y + 1
        if Board[yCheck][self.x] == "":
          PotentialMoves.append((2,0))
      
    PossibleMoves = []
    if self.Colour == "White": ### Colour validation need only for pawns, team killing removed in ValidMove
      for move in PotentialMoves:
        yMove = self.y - move[0]
        xMove = self.x - move[1]
        if xMove >= 0 and xMove <= 7 and yMove >= 0 and yMove <= 7: ###Check the move keeps the peice in the board
          DestinationPeice = Board[yMove][xMove]
          if Board[yMove][xMove] == "" and move[1] == 0:###Check if the chosen location is empty, and if the move is vertical
            PossibleMoves.append((yMove,xMove))
          elif Board[yMove][xMove] != "" and move[1] != 0 and self.Colour[0:5] != DestinationPeice.GetColour()[0:5] : ### If the chosen Location isnt empty and that the move is diagonal and prevent team killing
            PossibleMoves.append((yMove,xMove))
              
    if self.Colour == "Black": ### Check Colour
      for move in PotentialMoves:
        yMove = self.y + move[0]
        xMove = self.x + move[1]
        if xMove >= 0 and xMove <= 7 and yMove >= 0 and yMove <= 7:###Check the move keeps the peice in the board
          DestinationPeice = Board[yMove][xMove]
          if Board[yMove][xMove] == "" and move[1] == 0:###Check if the chosen location is empty, and if the move is vertical
            PossibleMoves.append((yMove,xMove))
          elif Board[yMove][xMove] != "" and move[1] != 0 and self.Colour[0:5] != DestinationPeice.GetColour()[0:5]: ### If the chosen Location isnt empty and that the move is diagonal
              PossibleMoves.append((yMove,xMove))

    return PossibleMoves


  
class Rook(Peice):
  def __init__(self, y, x, Colour, PeiceType,MoveCount):
    super().__init__(y, x, Colour, PeiceType,MoveCount)
    self.Score = 5
    YPosition = (self.y * 80)
    XPosition = (self.x * 80)
    self.Position = (XPosition, YPosition)

  def Update(self):
    NewYPosition = (self.y * 80)
    NewXPosition = (self.x * 80)
    self.Position = (NewXPosition, NewYPosition)

    
  def __str__(self):
    return ""+self.Colour+" "+self.PeiceType

  def GetPossibleMoves(self,Board): ### rook is unique peice cant use code from pawn or horse for it, potential moves likely not a good idea
    return self.GetRookMoves(Board)

class Horse(Peice):
  def __init__(self, y, x, Colour, PeiceType,MoveCount):
    super().__init__(y, x, Colour, PeiceType,MoveCount)
    self.Score = 3
    YPosition = (self.y * 80)
    XPosition = (self.x * 80)
    self.Position = (XPosition, YPosition)

  def Update(self):
    NewYPosition = (self.y * 80)
    NewXPosition = (self.x * 80)
    self.Position = (NewXPosition, NewYPosition)

  def __str__(self):
    return ""+self.Colour+" "+self.PeiceType

  def GetPossibleMoves(self,Board):
    PotentialMoves = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
    PossibleMoves = []
    for move in PotentialMoves: 
        yMove = self.y + move[0]
        xMove = self.x + move[1]
        if xMove >= 0 and xMove <= 7 and yMove >= 0 and yMove <= 7:
          DestinationPeice = Board[yMove][xMove]
          if DestinationPeice != "" and self.Colour[0:5] != DestinationPeice.GetColour()[0:5]: ###Check the move keeps the peice in the board and removes team kill
            PossibleMoves.append((yMove,xMove))
          elif DestinationPeice == "":
            PossibleMoves.append((yMove,xMove))
    return PossibleMoves


class Bishop(Peice):
  def __init__(self, y, x, Colour, PeiceType,MoveCount):
    super().__init__(y, x, Colour, PeiceType,MoveCount)
    self.Score = 3
    YPosition = (self.y * 80)
    XPosition = (self.x * 80)
    self.Position = (XPosition, YPosition)

  def Update(self):
    NewYPosition = (self.y * 80)
    NewXPosition = (self.x * 80)
    self.Position = (NewXPosition, NewYPosition)

  def __str__(self):
    return ""+self.Colour+" "+self.PeiceType

  def GetPossibleMoves(self,Board): 
    return self.GetBishopMoves(Board)

class Queen(Peice): 
  def __init__(self, y, x, Colour, PeiceType,MoveCount):
    super().__init__(y, x, Colour, PeiceType,MoveCount)
    self.Score = 9
    YPosition = (self.y * 80)
    XPosition = (self.x * 80)
    self.Position = (XPosition, YPosition)

  def Update(self):
    NewYPosition = (self.y * 80)
    NewXPosition = (self.x * 80)
    self.Position = (NewXPosition, NewYPosition)

    
  def __str__(self):
    return ""+self.Colour+" "+self.PeiceType

  def GetPossibleMoves(self,Board):
    RookMoves = self.GetRookMoves(Board)
    BishopMoves = self.GetBishopMoves(Board)
    PossibleMoves = RookMoves + BishopMoves
    return PossibleMoves

class King(Peice): 
  def __init__(self, y, x, Colour, PeiceType,MoveCount):
    super().__init__(y, x, Colour, PeiceType,MoveCount)
    self.Score = 900
    YPosition = (self.y * 80)
    XPosition = (self.x * 80)
    self.Position = (XPosition, YPosition)

  def Update(self):
    NewYPosition = (self.y * 80)
    NewXPosition = (self.x * 80)
    self.Position = (NewXPosition, NewYPosition)

    
  def __str__(self):
    return ""+self.Colour+" "+self.PeiceType

  def GetPossibleMoves(self,Board): ### for now, if the space is not held by a teammate, it is available. need to add check
    PossibleMoves = []
    for j in range(-1,2):
      for i in range(-1,2):
        yCheck = self.y + j
        xCheck = self.x + i
        if xCheck >= 0 and xCheck <= 7 and yCheck >= 0 and yCheck <= 7:
          DestinationPeice = Board[yCheck][xCheck]
          if j != 0 or i != 0 :
            if DestinationPeice != "" and DestinationPeice.GetColour() != self.Colour:
              PossibleMoves.append((yCheck,xCheck))
            elif DestinationPeice != "":
              continue
            else:
              PossibleMoves.append((yCheck,xCheck))
    '''
    self.GetCastle(Board)
    
    if self.Colour == "White":
      if self.LeftWhiteCastle:
        PossibleMoves.append((7,2))
      if self.RightWhiteCastle:
        PossibleMoves.append((7,6))
    if self.Colour == "Black":
      if self.LeftBlackCastle:
        PossibleMoves.append((0,2))
      if self.RightBlackCastle:
        PossibleMoves.append((0,6))
    '''
    return PossibleMoves
        
   



if __name__ == "__main__":
    GameState = Chess()
    
