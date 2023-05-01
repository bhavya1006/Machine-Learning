import random
# print(random.randint(1,10))


def p1(l):
    x = int(input("Enter position Player 1: "))
    if x not in l:
        print("Position occupied!!")
        x = p1(l)
    return x
def p2(l):
    o = int(input("Enter position Player 2: "))
    if o not in l:
        print("Position occupied!!")
        o = p2(l)
    return o
def bot(l):
    o = random.randint(1,10)
    if o not in l:
        o = bot(l)
    return o

def chkFills(board):
    l = []
    for i in board:
        if board[i]=='_':
            l.append(i)
    return l

def chkBoard(Board):
    if chkFills(Board) == []:
        print('!-------Draw-------!')

# created board storage
bd = {1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_',}

# created display for tic tac toe
def displayBD(board):
    for i in board:
        print(board[i],end=' ')
        if i%3==0:
            print()

def logic(board,game):
    for i in range(0,3):
        j = i*3
        game = 1
        if board[1+i]=='x' and board[4+i]=='x' and board[7+i]=='x':
            print("Player 1 Wins!!!")
            return game
        elif board[1+i]=='o' and board[4+i]=='o' and board[7+i]=='o':
            print("Player 2 Wins!!")
            return game
        elif board[1+j]=='x' and board[2+j]=='x' and board[3+j]=='x':
            print("Player 1 Wins!!!")
            return game
        elif board[1+j]=='o' and board[2+j]=='o' and board[3+j]=='o':
            print("Player 2 Wins!!")
            return game
        elif (board[1]=='x' and board[5]=='x' and board[9]=='x') or (board[3]=='x' and board[5]=='x' and board[7]=='x'):
            print("Player 1 Wins!!!")
            return game
        elif (board[1]=='o' and board[5]=='o' and board[9]=='o') or (board[3]=='o' and board[5]=='o' and board[7]=='o'):
            print("Player 2 Wins!!")
            return game
        break
    game = 0
    return game

def logicbot(board,game):
    for i in range(0,3):
        j = i*3
        game = 1
        if board[1+i]=='x' and board[4+i]=='x' and board[7+i]=='x':
            print("Player 1 Wins!!!")
            return game 
        elif board[1+i]=='o' and board[4+i]=='o' and board[7+i]=='o':
            print("BOT Wins!!")
            return game 
        elif board[1+j]=='x' and board[2+j]=='x' and board[3+j]=='x':
            print("Player 1 Wins!!!")
            return game 
        elif board[1+j]=='o' and board[2+j]=='o' and board[3+j]=='o':
            print("BOT Wins!!")
            return game 
        elif (board[1]=='x' and board[5]=='x' and board[9]=='x') or (board[3]=='x' and board[5]=='x' and board[7]=='x'):
            print("Player 1 Wins!!!")
            return game 
        elif (board[1]=='o' and board[5]=='o' and board[9]=='o') or (board[3]=='o' and board[5]=='o' and board[7]=='o'):
            print("BOT Wins!!")
            return game
        break
    game = 0
    return game
            


def playervs():
    game = 0
    while game == 0:

        l = chkFills(bd)

        # to take value at positions
        bd[p1(l)] = 'x'

        displayBD(bd)
        game = logic(bd,game)
        if game==1:
            break
        chkBoard(bd)
        l = chkFills(bd)

        # to take value at positions
        
        bd[p2(l)] = 'o'

        displayBD(bd)
        logic(bd,game)
        chkBoard(bd)

def playerbot():
    game = 0
    while game == 0:

        l = chkFills(bd)

        # to take value at positions
        bd[p1(l)] = 'x'

        displayBD(bd)
        game = logicbot(bd,game)
        # print(game)
        if game==1:
            break
        l = chkFills(bd)

        # to take value at positions
        
        bd[bot(l)] = 'o'
        print("Bot Played---------")
        displayBD(bd)
        logicbot(bd,game)

print("Which mode you wanna play : ")
print("1) With Player")
print("2) With Bot")

ch = int(input("Enter your choice: "))
if ch == 1:
    playervs()
    print("Game Over!!")
elif ch == 2:
    playerbot()
    print("Game Over!!")
else:
    print("No choice given")

