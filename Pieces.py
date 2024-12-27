
### Piece classes and subclasses


class Piece(): ### parent class for all pieces
    def __init__(self,x,y,type,colour,moveCount):
        self.x = x
        self.y = y
        self.type = type
        self.colour = colour
        self.score = 0 ### this will be overloaded in child constructors, required for getscore
        self.moveCount = 0 ### may need to change to moveCount, or remove all
        ### multiply x and y locations by 80 to get the location on the display
        self.position = (self.x * 80, self.y * 80) ### return a tuple of location

    def PossibleMoves(self,board):
        ### method to be overided, board is the list Chess.Pieces,
        pass
    
    def IncrementMoveCount(self):
        self.moveCount+=1

    def IsInBounds(self,CheckLoc):
        (checkX,checkY) = CheckLoc
        return checkX >= 0 and checkX <= 7 and checkY >= 0 and checkY <= 7
        

    ### getters
    def GetScore(self):
        return self.score
    def GetPosition(self):
        return self.position
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
        self.position = (self.x * 80, self.y * 80) ### return a tuple of location


    def CheckDirection(self,checkLoc,board):
        emptySpace = True ### assume the checked space is empty
        for piece in board: ### iterate through pieces
                if checkLoc == piece.GetLocation(): ### contact with peice
                    emptySpace = False ### the space is not empty, stop checking this direction after this piece
                    if piece.GetColour() != self.GetColour(): ###pieces are not on same team
                        return checkLoc,emptySpace
                        #print("enemy yay")
                    else:
                        return (-1,-1), emptySpace

             ### empty space 
        if emptySpace:
            return checkLoc,emptySpace

    def RookMoves(self,board):
        ### rook moves are used by both the rook, and queen
        # up to 8 spaces horizontal or vertical
        # if not moved, and empty spaces between it and King
        # who has also not moved, castle is allowed
        # so long as in bounds

        # get location
        # have a loop for both up, down, left and right, starting from location
        # if square is empty, add to list, if enemy, add to list and break
        # if teammate, break
        (startX,startY) = self.GetLocation()
        possibleMoves = []
        
        ### vertical first
        for y in range(startY -1,-1, -1): ### this loop is for up
           checkLoc = (startX,y)
           move , emptySpace = self.CheckDirection(checkLoc, board)
           if move != (-1,-1): ### if the move isnt a teammate
            possibleMoves.append(move)
           if not emptySpace:
              break

        emptySpace = True ### reset the empty space value to true
        for y in range(startY +1,8): ### this loop is for up
           checkLoc = (startX,y)
           move , emptySpace = self.CheckDirection(checkLoc, board)
           if move != (-1,-1): ### if the move isnt a teammate
            possibleMoves.append(move)
           if not emptySpace:
              break

        emptySpace = True
        for x in range(startX -1,-1, -1): ### this loop is for left
            checkLoc = (x,startY)
            move , emptySpace = self.CheckDirection(checkLoc, board)
            if move != (-1,-1): ### if the move isnt a teammate
                possibleMoves.append(move)
            if not emptySpace:
                break

        emptySpace = True
        for x in range(startX + 1,8): ### this loop is for right
            checkLoc = (x,startY)
            move , emptySpace = self.CheckDirection(checkLoc, board)
            if move != (-1,-1): ### if the move isnt a teammate
                possibleMoves.append(move)
            if not emptySpace:
                break

        return possibleMoves
    
    def BishopMoves(self,board):
        # up to 8 spaces diagonally
    # so long as in bounds


        (startX,startY) = self.GetLocation()
        possibleMoves = []


        ### this is north west
        emptySpace = True
        (checkX,checkY) = (startX -1,startY-1) ### move one space NW
        checkLoc = (checkX,checkY)
        while self.IsInBounds(checkLoc): ### while remaining in bounds
            move, emptySpace = self.CheckDirection(checkLoc, board) ### check the move, if it is empty/ has an opp or teammate
            if move != (-1,-1): ### if piece in checkLoc isnt teammate
                possibleMoves.append(move)
            if not emptySpace: ### a piece has been hit, break this direction
                break
            (checkX,checkY) = (checkX - 1,checkY - 1) ### increment direction
            checkLoc = (checkX,checkY)


        ### this is north east
        emptySpace = True
        (checkX,checkY) = (startX +1,startY-1) ### move one space NE
        checkLoc = (checkX,checkY)
        while self.IsInBounds(checkLoc): ### while remaining in bounds
            move, emptySpace = self.CheckDirection(checkLoc, board) ### check the move, if it is empty/ has an opp or teammate
            if move != (-1,-1): ### if piece in checkLoc isnt teammate
                possibleMoves.append(move)
            if not emptySpace: ### a piece has been hit, break this direction
                break
            (checkX,checkY) = (checkX + 1,checkY - 1) ### increment direction
            checkLoc = (checkX,checkY)


        ### this is south east
        emptySpace = True
        (checkX,checkY) = (startX +1,startY+1) ### move one space SE
        checkLoc = (checkX,checkY)
        while self.IsInBounds(checkLoc): ### while remaining in bounds
            move, emptySpace = self.CheckDirection(checkLoc, board) ### check the move, if it is empty/ has an opp or teammate
            if move != (-1,-1): ### if piece in checkLoc isnt teammate
                possibleMoves.append(move)
            if not emptySpace: ### a piece has been hit, break this direction
                break
            (checkX,checkY) = (checkX + 1,checkY + 1)### increment direction
            checkLoc = (checkX,checkY)
        

        ### this is south west
        emptySpace = True
        (checkX,checkY) = (startX -1,startY+1) ### move one space SW
        checkLoc = (checkX,checkY)
        while self.IsInBounds(checkLoc): ### while remaining in bounds
            move, emptySpace = self.CheckDirection(checkLoc, board) ### check the move, if it is empty/ has an opp or teammate
            if move != (-1,-1): ### if piece in checkLoc isnt teammate
                possibleMoves.append(move)
            if not emptySpace: ### a piece has been hit, break this direction
                break
            (checkX,checkY) = (checkX - 1,checkY + 1)### increment direction
            checkLoc = (checkX,checkY)
        

        return possibleMoves

    

class Pawn(Piece):
    def __init__(self,x,y,type,colour,moveCount):
        super().__init__(x,y,type,colour,moveCount) ### call parent init
        self.score = 1

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
                if checkLoc == twoSpace or not self.IsInBounds(twoSpace):
                    twoSpacePossible = False
                if checkLoc == oneSpace or not self.IsInBounds(oneSpace):
                    oneSpacePossible = False
                if piece.GetColour() == "Black": ### check the black pieces and append possible captures
                    if checkLoc == leftCap :
                        possibleMoves.append(leftCap)
                    elif checkLoc == rightCap:
                        possibleMoves.append(rightCap)
            if oneSpacePossible: ### append possible moves
                possibleMoves.append(oneSpace)
            if twoSpacePossible:
                possibleMoves.append(twoSpace)
            return possibleMoves
        
        else:
            oneSpace = (startX, startY + 1) ## the four potential moves of a pawn, enpassant to be added later
            twoSpace = (startX, startY + 2)
            leftCap = (startX - 1 , startY + 1)
            rightCap = (startX + 1, startY + 1)
            for piece in board: ### search all the opp pieces
                checkLoc = piece.GetLocation()
                if checkLoc == twoSpace or not self.IsInBounds(twoSpace):
                    twoSpacePossible = False
                if checkLoc == oneSpace or not self.IsInBounds(oneSpace):
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
        self.score = 5

    def PossibleMoves(self,board):
        ### return the rook moves
        return self.RookMoves(board)

class Horse(Piece):
    def __init__(self,x,y,type,colour,moveCount):
        super().__init__(x,y,type,colour,moveCount) ### call parent init
        self.score = 3

    def PossibleMoves(self,board):
        # either 2 vertical and 1 horizontal or 2 horizontal 1 vertical
        # so long as in bounds

        (startX,startY) = self.GetLocation()
        possibleMoves = []
        potentialMoves = [(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1),(-2,-1)]  ### the eight possible moves the Horse can make, relative to its own location
        
        for dir in potentialMoves:
            checkLoc= (startX + dir[0], startY + dir[1]) ### check the location of each move
            if self.IsInBounds(checkLoc): ### if move is in bounds
                move,_ = self.CheckDirection(checkLoc,board) ### emptySpace is irrelevant here
                if move != (-1,-1): ### if piece in checkLoc isnt teammate
                    possibleMoves.append(move)
        return possibleMoves
        
        
        
        pass
        
    
class Bishop(Piece):
    def __init__(self,x,y,type,colour,moveCount):
        super().__init__(x,y,type,colour,moveCount) ### call parent init
        self.score = 3  
    
    def PossibleMoves(self,board):
        return self.BishopMoves(board)
    
class Queen(Piece):
    def __init__(self,x,y,type,colour,moveCount):
        super().__init__(x,y,type,colour,moveCount) ### call parent init
        self.score = 9
    def PossibleMoves(self,board):
    # combination of rook and bishop moves
    # so long as in bounds
        return self.RookMoves(board) + self.BishopMoves(board)

class King(Piece):
    def __init__(self,x,y,type,colour,moveCount):
        super().__init__(x,y,type,colour,moveCount) ### call parent init
        self.score = 100
    
    def PossibleMoves(self,board):
        #1 move in any direction
        # if movecount = 0 and rook with LOS has movecount = 0, allow castle
        # so long as in bounds
        (startX,startY) = self.GetLocation()
        possibleMoves = []
        potentialMoves = [(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1)] ### the eight possible moves the king can make, relative to its own location

        for dir in potentialMoves:
            checkLoc= (startX + dir[0], startY + dir[1]) ### check the location of each move
            if self.IsInBounds(checkLoc): ### if move is in bounds
                move,_ = self.CheckDirection(checkLoc,board) ### emptySpace is irrelevant here
                if move != (-1,-1): ### if piece in checkLoc isnt teammate
                    possibleMoves.append(move)
        return possibleMoves
    
    def isCastleValid():
        pass

    def isInCheck():
        pass