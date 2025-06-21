# Connect_Four_Game

Connect Four is a two-player game on a 6x7 grid where players take turns dropping discs, aiming to connect four in a row 
horizontally, vertically, or diagonally to win.

## Game Rules:
1.Players: 2 (Player 🟣 and Player 🟢)

2.Turn-based: Players take turns to drop one disc per turn.

3.Board size: 6 rows × 7 columns (standard Connect Four dimensions).

4.Objective: Be the first to connect four of your pieces in a:
    Horizontal line
    Vertical line
    Diagonal line (↘ or ↙)
    
5.Column Selection: Players choose a column (A-G) to place their piece.

6.Manual Row Selection (non-standard): Players must also enter the row index (0–5), which differs from classic Connect Four (where pieces fall to the lowest empty row automatically).

7.Winning Condition: If a player connects 4 discs in a row in any direction, they win.

8.Draw Condition: If the board is full and no player wins, the game ends in a draw.

9.Occupied Check: If the chosen cell is already filled, the player is prompted to choose again.

## Game Logic Summary:
  Game Board: Implemented as a 2D list (gameBoard), 6 rows × 7 columns.
  
  Column Mapping: A–G mapped to indices 0–6 via possibleLetters list.
  
  Turn Tracking: turnCounter determines the current player.

 # Functions:
  printGameBoard(): Renders the board with emojis.
  
  modifyTurn(row, column, player): Updates the board with the player’s piece.
  
  checkWin(): Scans the board for four connected pieces.
