def CountSpecificRow(_board:list, _row_num:int, _player:str, _search_for_empty:bool):
    counts = 0
    for x in range(len(_board)):
        if _board[_row_num][x] == _player:
            counts += 1
        elif _search_for_empty and _board[_row_num][x] != None:
            return 0
    return counts

def CountSpecificCol(_board:list, _col_num:int, _player:str, _search_for_empty:bool):
    counts = 0
    for y in range(len(_board)):
        if _board[y][_col_num] == _player:
            counts += 1
        elif _search_for_empty and _board[y][_col_num] != None:
            return 0
    return counts

def CountDiagonalStraight(_board:list, _player:str, _search_for_empty:bool):
    counts = 0
    for xy in range(len(_board)):
        if _board[xy][xy] == _player:
            counts += 1
        elif _search_for_empty and _board[xy][xy] != None:
            return 0
    return counts

def GetEmptySpecificRow(_board:list, _row_num:int, _check_what):
    empty = None
    for x in range(len(_board)):
        if _board[_row_num][x] == None:
            empty = (_row_num,x)
    return empty

def GetEmptySpecificCol(_board:list, _col_num:int, _check_what):
    empty = None
    for y in range(len(_board)):
        if _board[y][_col_num] == _check_what:
            empty = (y,_col_num)
    return empty

def GetEmptyDiagonalStraight(_board:list, _check_what):
    for xy in range(len(_board)):
        if _board[xy][xy] == _check_what:
            return xy,xy
    return None
def GetEmptyDiagonalInvert(_board:list, _check_what):
    for xy in range(len(_board)):
        if _board[xy][len(_board)-xy-1] == _check_what:
            return xy,len(_board)-xy-1
    return None
def CountPlayerInRowsMax(_board:list, _player:str):
    needed = len(_board)
    max_counts = 0
    pos_empty = None
    pos_tmp = None
    for y in range(needed):
        cnt = 0
        for x in range(needed):
            if _board[y][x] == _player:
                cnt += 1
            elif _board[y][x] == None:
                pos_tmp = [x,y]
        if cnt > max_counts:
            max_counts = cnt
            pos_empty = pos_tmp
        else:
            pos_tmp = None
    if pos_empty == None and max_counts == 0:
        return pos_tmp,max_counts
    return pos_empty,max_counts

def CountPlayerInColsMax(_board:list, _player:str):
    needed = len(_board)
    max_counts = 0
    pos_empty = None
    pos_tmp = None
    for x in range(needed):
        cnt = 0
        for y in range(needed):
            if _board[y][x] == _player:
                cnt += 1
            elif _board[y][x] == None:
                pos_tmp = [x, y]
        if cnt > max_counts:
            max_counts = cnt
            pos_empty = pos_tmp
        else:
            pos_tmp = None
    if pos_empty == None and max_counts == 0:
        return pos_tmp,max_counts
    return pos_empty,max_counts

def CountDiagonalsMax(_board:list, _player:str):
    needed = len(_board)
    max_counts = 0
    pos_empty = None
    pos_tmp = None
    cnt = 0
    for xy in range(needed):
        if _board[xy][xy] == _player:
            cnt += 1
        elif _board[xy][xy] == None:
            pos_tmp = [xy,xy]
    if cnt > max_counts:
        max_counts = cnt
        pos_empty = pos_tmp
    else:
        pos_tmp = None
    cnt = 0
    for xy in range(needed):
        if _board[xy][needed-xy-1] == _player:
            cnt += 1
        elif _board[xy][needed-xy-1] == None:
            pos_tmp = [xy,needed-xy-1]
    if cnt >= max_counts:
        max_counts = cnt
        pos_empty = pos_tmp
    else:
        pos_tmp = None
    if pos_empty == None and max_counts == 0:
        return pos_tmp,max_counts
    return pos_empty,max_counts

def GetMax(_a:list,_b:list,_c:list):
    if _a[1] > _b[1] and _a[1] > _c[1]:
        return _a
    elif _c[1] > _b[1] and _c[1] > _a[1]:
        return _c
    elif _b[1] > _c[1] and _b[1] > _a[1]:
        return _b
    else:
        return False
def GetMaxOrEqual(_a:list,_b:list,_c:list):
    if _a[1] >= _b[1] and _a[1] >= _c[1]:
        return _a
    elif _c[1] >= _b[1] and _c[1] >= _a[1]:
        return _c
    elif _b[1] >= _c[1] and _b[1] >= _a[1]:
        return _b
def CountContinuemOponnent(_board:list, _player:str):
    rowsMax = CountPlayerInRowsMax(_board,_player)
    if rowsMax[0] == None:
        rowsMax = ([],0)
    colsMax = CountPlayerInColsMax(_board,_player)
    if colsMax[0] == None:
        colsMax = ([],0)
    diagMax = CountDiagonalsMax(_board,_player)
    if diagMax[0] == None:
        diagMax = ([],0)
    ans = GetMax(rowsMax,colsMax,diagMax)
    if ans == False:
        return GetMaxOrEqual(rowsMax,colsMax,diagMax)
    return ans


def IsThereAWinner(_board:list, _opo:str, _me:str):
    needed = len(_board)
    players = [_opo,_me]
    for player in players:
        max_counts = 0
        for y in range(needed):
            cnt = 0
            for x in range(needed):
                if _board[y][x] == player:
                    cnt += 1
        if cnt > max_counts:
            max_counts = cnt
        for x in range(needed):
            cnt = 0
            for y in range(needed):
                if _board[y][x] == player:
                    cnt += 1
            if cnt > max_counts:
                max_counts = cnt
        cnt = 0
        for xy in range(needed):
            if _board[xy][xy] == player:
                cnt += 1
        if cnt > max_counts:
            max_counts = cnt
        cnt = 0
        for xy in range(needed):
            if _board[xy][needed-xy-1] == player:
                cnt += 1
        if cnt > max_counts:
            max_counts = cnt
        if max_counts == needed:
            return player
    return False

def IsMiddlePossible(_board:list, _me:str):
    pos = int(len(_board)/2)
    if  _board[pos][pos] == None:
        _board[pos][pos] = _me
        return _board
    return False

def IsOpponentAboutToWin(_board:list, _me:str, _opo:str):
    result = CountContinuemOponnent(_board,_opo)
    if len(result[0]) == 0:
        return False
    if result[1] == len(_board)-1:
        _board[result[0][1]][result[0][0]]= _me
        return _board
    return False

def CanOpponentWinInTwo(_board:list, _me:str, _opo:str):
    for y in range(len(_board)):
        for x in range(len(_board)):
            if _board[y][x] == None:
                possible_wins = 0
                board_copy = _board.copy()
                board_copy[y][x] = _opo
                res = CountSpecificRow(board_copy,y,_opo, True)
                if res == len(board_copy)-1:
                    possible_wins += 1
                res = CountSpecificCol(board_copy,x,_opo, True)
                if res == len(board_copy)-1:
                    possible_wins += 1
                if x == y:
                    res = CountDiagonalStraight(board_copy,_opo, True)
                    if res == len(board_copy)-1:
                        possible_wins += 1
                if x == len(board_copy) - y -1:
                    if res == len(board_copy)-1:
                        possible_wins += 1
                if possible_wins > 1:
                    _board[y][x] = None
                    return y,x
                else:
                    _board[y][x] = None

    return False

def CanIWin(_board:list, _me:str, _opo:str):
    result = CountContinuemOponnent(_board,_me)
    if result[1] == len(_board)-1:
        _board[result[0][1]][result[0][0]]= _me
        return _board
    return False

def CountContinuemForMe(_board:list, _player:str):
    needed = len(_board)
    max_counts = 0
    pos_empty = None
    for y in range(needed):
        counts_in_row = CountSpecificRow(_board,y,_player, False)
        empty_pos = GetEmptySpecificRow(_board,y,None)
        if counts_in_row >= max_counts and empty_pos != None:
            max_counts = counts_in_row
            pos_empty = empty_pos

    for x in range(needed):
        counts_in_col = CountSpecificCol(_board,x,_player, False)
        empty_pos = GetEmptySpecificCol(_board,x,None)
        if counts_in_col >= max_counts and empty_pos != None:
            max_counts = counts_in_row
            pos_empty = empty_pos
    counts_diag = CountDiagonalStraight(_board, _player, False)
    empty_pos = GetEmptyDiagonalStraight(_board,None)

    if counts_diag >= max_counts and empty_pos != None:
        max_counts = counts_in_row
        pos_empty = empty_pos
    empty_pos = GetEmptyDiagonalInvert(_board,None)

    if counts_diag >= max_counts and empty_pos != None:
        max_counts = counts_in_row
        pos_empty = empty_pos
    return pos_empty,max_counts
def ElongateMe(_board:list, _me:str, _opo:str):
    result = CountContinuemForMe(_board,_me)
    if result[0] == None:
        return _board
    _board[result[0][1]][result[0][0]] = _me
    return _board


"""
def CountPlayerInRowsMax(_board:list, _player:str):
    needed = len(_board)
    max_counts = 0
    pos_empty = None
    pos_tmp = None
    for y in range(needed):
        cnt = 0
        for x in range(needed):
            if _board[y][x] == _player:
                cnt += 1
            elif _board[y][x] == None:
                pos_tmp = [x,y]
        if cnt > max_counts:
            max_counts = cnt
            pos_empty = pos_tmp
        else:
            pos_tmp = None
    if pos_empty == None and max_counts == 0:
        return pos_tmp,max_counts
    return pos_empty,max_counts
    
    
def CountContinuemForMe(_board:list, _player:str):
    needed = len(_board)
    max_counts = 0
    pos_empty = None
    pos_tmp = None
    for y in range(needed):
        cnt = 0
        for x in range(needed):
            if _board[y][x] == _player:
                cnt += 1
            elif _board[y][x] == None:
                pos_tmp = [x,y]
        if cnt >= max_counts:
            max_counts = cnt
            pos_empty = pos_tmp
    for x in range(needed):
        cnt = 0
        for y in range(needed):
            if _board[y][x] == _player:
                cnt += 1
            elif _board[y][x] == None:
                pos_tmp = [x,y]
        if cnt >= max_counts:
            max_counts = cnt
            pos_empty = pos_tmp
    cnt = 0
    for xy in range(needed):
        if _board[xy][xy] == _player:
            cnt += 1
        elif _board[xy][xy] == None:
            pos_tmp = [xy,xy]
    if cnt >= max_counts:
        max_counts = cnt
        pos_empty = pos_tmp
    cnt = 0
    for xy in range(needed):
        if _board[xy][needed-xy-1] == _player:
            cnt += 1
        elif _board[xy][needed-xy-1] == None:
            pos_tmp = [xy,needed-xy-1]
    if cnt >= max_counts:
        pos_empty = pos_tmp
        max_counts = cnt
    return pos_empty,max_counts
"""