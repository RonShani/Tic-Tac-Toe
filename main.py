from LinesChecker import IsMiddlePossible, CanIWin, IsOpponentAboutToWin, ElongateMe, IsThereAWinner, CanOpponentWinInTwo
import os

BOARD_DIMENSIONS = 5
def BoardCreate(_width:int, _height:int):
    board = list()
    width_list = list()
    for w in range(_width):
        width_list.append(None)
    for h in range(_height):
        board.append(width_list.copy())
    return board
def PlayerPutPeone(_board:list, _me:str, _computer:str, _plays:int):
    pos_input = ["A","A"]
    while not pos_input[0].isdigit() or len(pos_input) < 2 or not pos_input[1].isdigit():
        pos_input = input("Enter X Y seperated by space:")
        pos_input = pos_input.split(" ")
    x = int(pos_input[0])
    y = int(pos_input[1])
    if x < 0 or x >= len(_board) or y < 0 or y >= len(_board) or _board[y][x] != None:
        return PlayerPutPeone(_board,_me, _computer,_plays)
    _board[y][x] = _me
    _plays = IsGameContinues(_board,_me,_computer,_plays)
    return _plays,_board

def BoardPrint(_board:list):
    os.system('cls')
    print()
    for y,row in enumerate(_board):
        for x,col in enumerate(row):
            if col == None:
                if x == 0:
                    print("|"," ", "|", end="")
                else:
                    print(" ","|",end="")
            else:
                if x == 0:
                    print("|", col, "|", end="")
                else:
                    print(col, "|", end="")
        print()
def ComputerOptions(_board:list, _me:str, _opo:str):
    result = CanIWin(_board, _me, _opo)
    if result != False:
        return result
    result = IsMiddlePossible(_board, _me)
    if result != False:
        return result
    result = IsOpponentAboutToWin(_board, _me, _opo)
    if result != False:
        return result
    result = CanOpponentWinInTwo(_board, _me, _opo)
    if result != False:
        _board[result[0]][result[1]] = _me
        return _board
    result = ElongateMe(_board, _me, _opo)
    if result != False:
        return result
    else:
        return _board


def ComputerPlay(_board:list, _me:str, _computer:str, _plays:int):
    board = ComputerOptions(_board, _computer, _me)
    _plays = IsGameContinues(_board,_me,_computer,_plays)
    return _plays,board

def IsGameContinues(_board:list, _me:str, _computer:str, _plays:int):
    BoardPrint(_board)
    winner = IsThereAWinner(_board, _me, _computer)
    if winner != False:
        print("The winner is ", winner)
        exit(0)
    if _plays == 0:
        print("Its a tie")
        exit(0)
    return _plays - 1

def StartPlay():
    board_dimensions = BOARD_DIMENSIONS
    me = "X"
    computer = "O"
    plays = board_dimensions*board_dimensions
    board = BoardCreate(board_dimensions,board_dimensions)
    BoardPrint(board)
    while plays > 0:
        plays,board = PlayerPutPeone(board, me,computer,plays)
        plays,board = ComputerPlay(board,me,computer,plays)

if __name__ == '__main__':
    StartPlay()


"""
1. if possible - put in the middle
2. if opponent about to win (size-1 strike) --> block him
3. if i can elongate my strike --> do that
"""