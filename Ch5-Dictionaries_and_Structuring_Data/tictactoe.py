# This is a very basic, just as much as described in the texts. I might or might not make this better in the future :)

board = {
    'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
    'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
    'low-l': ' ', 'low-m': ' ', 'low-r': ' '
}

def printBoard(board):
    print(board['top-l'] + ' | ' + board['top-m'] + ' | ' + board['top-r'])
    print(board['mid-l'] + ' | ' + board['mid-m'] + ' | ' + board['mid-r'])
    print(board['low-l'] + ' | ' + board['low-m'] + ' | ' + board['low-r'])

turn = 'X'

for i in range(9):
    printBoard(board)
    print(f"Turn for {turn}. Move on which space?")
    move = input().lower()
    board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

# printBoard(board)