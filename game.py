board = [["." for _ in range(3)] for _ in range(3)]
players = ["X", "O"]
XMoves = 0
YMoves = 0


def startGame():
    global board
    global players

    board = [["." for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print("Игра началась!")


def boardToString():
    global board

    result = ""
    for row in board:
        for cell in row:
            result += cell + " "
        result += "\n"
    return result


def status():
    global board

    moves = f" XMoves = {XMoves}, YMoves = {YMoves}"

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '.':
            return f"Player {board[i][0]} won" + moves
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '.':
            return f"Player {board[0][i]} won" + moves
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.':
        return f"Player {board[0][0]} won" + moves
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '.':
        return f"Player {board[0][2]} won" + moves
    for row in board:
        if '.' in row:
            return "In Progress" + moves

    return "Draw" + moves


def make_move(row, col, cell):
    global XMoves
    global YMoves

    board[row][col] = cell
    if cell == "X":
        XMoves += 1
    if cell == "Y":
        YMoves += 1
