###
[y][x]


[y]
internal ---> external
[7]      --->       [1]
[6]      --->       [2]
[5]      --->       [3]
[4]      --->       [4]
[3]      --->       [5]
[2]      --->       [6]
[1]      --->       [7]
[0]      --->       [8]

[x]
internal ---> external
[7]      --->       [H]
[6]      --->       [G]
[5]      --->       [F]
[4]      --->       [E]
[3]      --->       [D]
[2]      --->       [C]
[1]      --->       [B]
[0]      --->       [A]



i dont like the pieces having move methods, have the methods take the board state and an input move, and return if
possible, then have game manager move the piece. move method in pawn is fine for now

whenever a piece is moved, you need to update its position


for possible moves, return a list of all possible locations a piece can move to

it will then be iterated through in a different method to check if input move is valid,

for castling, check if move distance >1
for en passant, check if valid rank and movecount of adjacent opp = 1 
for promotion, make sure is opposite end of board