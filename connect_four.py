import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A","B","C","D","E","F","G"]
gameBoard = [["","","","","","",""], ["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]

rows = 6
cols = 7

def printGameBoard():
    board_display = ""
    for i in range(rows):
        row_display = ""
        for j in range(cols):
            if gameBoard[i][j] == "":
                row_display += "⚪"  
            elif gameBoard[i][j] == "🟣":
                row_display += "🟣"  
            elif gameBoard[i][j] == "🟢":
                row_display += "🟢"  
            row_display += " "
        board_display += row_display + "\n"
    print(board_display)

def modifyTurn(spacePicked, turn):
  gameBoard[spacePicked[0]][spacePicked[1]] = turn

def checkWin():
 for i in range(rows):
  for j in range(cols - 3): 
    if(gameBoard[i][j] == gameBoard[i][j+1] == gameBoard[i][j+2] == gameBoard[i][j+3] != ""): 
      return True

 for j in range(cols): 
   for i in range(rows - 3): 
     if(gameBoard[i][j] == gameBoard[i+1][j] == gameBoard[i+2][j] == gameBoard[i+3][j] != ""): 
       return True

 for i in range(rows - 3): 
   for j in range(cols - 3): 
     if(gameBoard[i][j] == gameBoard[i+1][j+1] == gameBoard[i+2][j+2] == gameBoard[i+3][j+3] != ""): 
       return True

 for i in range(rows - 3): 
  for j in range(3, cols): 
    if(gameBoard[i][j] == gameBoard[i+1][j-1] == gameBoard[i+2][j-2] == gameBoard[i+3][j-3] != ""): 
      return True

  return False

turnCounter = 0

while True:
    printGameBoard()
    if turnCounter % 2 == 0:
        player = "🟣"
    else:
        player = "🟢"
    
    spacePicked = ()

    while True:
        column = input(f"\nPlayer {player}, choose a column (A-G) to place your piece: ").upper()
        row = int(input(f"\nPlayer {player}, choose a row (0-5) to place your piece: "))

        if column in possibleLetters and (row >= 0 and row < 6):
            column = possibleLetters.index(column)
            if gameBoard[row][column] == "":
                spacePicked = (row, column)
                break
            else:
                print("\nColumn is already full. Please try again.")
        else:
            print("\nInvalid input. Please try again.")

    modifyTurn(spacePicked, player)
    turnCounter += 1

    if checkWin():
        printGameBoard()
        print(f"\nPlayer {player} wins!")
        break

    if turnCounter == rows * cols:
        printGameBoard()
        print("\nIt's a draw!")
        break