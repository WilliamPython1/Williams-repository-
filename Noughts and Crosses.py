
board = ['' for b in range(9)]
turnsPassed = 1
Owin = 'OOO'
Xwin = 'XXX'

def positions():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


positions()
noughtOrCross = 1
def choice(turn):
    move = int(input('Which position would you like to go (1-9)?'))
    if (turn % 2) == 0:
        icon = 'O'
    else:
        icon = 'X'
    if board[move - 1] == '':
        board[move - 1] = icon
        positions()

while board[0] + board[1] + board[2] != Xwin or board[0] + board[1] + board[2] != Owin:
    choice(turnsPassed)
    if board[0] + board[1] + board[2] == Xwin or board[3] + board[4] + board[5] == Xwin or board[6] + board[7] + board[8] == Xwin or board[0] + board[4] + board[8] == Xwin or board[2] + board[4] + board[6] == Xwin:
        print('Victory for crosses!')
        break
    elif board[0] + board[1] + board[2] == Owin or board[3] + board[4] + board[5] == Owin or board[6] + board[7] + board[8] == Owin or board[0] + board[4] + board[8] == Owin or board[2] + board[4] + board[6] == Owin:
        print('Victory for noughts!')
        break
    elif board[0] and board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8]:
        print('It was a draw... get good Tom!')
        break
    turnsPassed = turnsPassed + 1
