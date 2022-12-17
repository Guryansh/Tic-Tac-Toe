# By Guryansh

ttt = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def tttdiag():
    print(" {} | {} | {}".format(ttt[0][0], ttt[0][1], ttt[0][2]))
    print("---|---|---")
    print(" {} | {} | {}".format(ttt[1][0], ttt[1][1], ttt[1][2]))
    print("---|---|---")
    print(" {} | {} | {}".format(ttt[2][0], ttt[2][1], ttt[2][2]))


def check(symbol):
    won = False
    if (ttt[0][0] == symbol):
        if (ttt[0][1] == symbol):
            if (ttt[0][2] == symbol):
                won = True

        elif (ttt[1][0] == symbol):
            if (ttt[2][0] == symbol):
                won = True

        elif (ttt[1][1] == symbol):
            if (ttt[2][2] == symbol):
                won = True

    elif (ttt[1][1] == symbol):
        if (ttt[1][0] == symbol):
            if (ttt[1][2] == symbol):
                won = True

        elif (ttt[0][2] == symbol):
            if (ttt[2][0] == symbol):
                won = True

        elif (ttt[2][1] == symbol):
            if (ttt[0][1] == symbol):
                won = True

    elif (ttt[2][2] == symbol):
        if (ttt[2][0] == symbol):
            if (ttt[2][1] == symbol):
                won = True

        elif (ttt[0][2] == symbol):
            if (ttt[1][2] == symbol):
                won = True

    return won


def turn(player):
    if player == 1:
        symbol = p1sym
    else:
        symbol = p2sym

    p = input("Player {} enter position(R,C):".format(player))
    i = int(p.split()[0]) % 3
    j = int(p.split()[1]) % 3
    if i == 0:
        i = 3
    if j == 0:
        j = 3
    if (ttt[i - 1][j - 1] == ' '):
        ttt[i - 1][j - 1] = symbol
    else:
        turn(player)

    return symbol


print("Welcome to Tic Tac Toe")

print("What would player 1 like to choose?")
p1sym = input("Enter o or x:")
p2sym = 'x'
if (p2sym == p1sym):
    p2sym = 'o'

gwon = False

for i in range(9):
    i %= 2
    i += 1

    symbol = turn(i)
    tttdiag()

    if check(symbol):
        print("Player{} won".format(i))
        gwon = True
        break

if gwon == False:
    print("Draw")
