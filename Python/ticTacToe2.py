from random import randint as rdi

def board():
    __board = {1:'-',2:'-',3:'-',
             4:'-',5:'-',6:'-',
             7:'-',8:'-',9:'-'}
    return __board
def displayBoard(board):
    for i in board:
        print(board[i],end=' ')
        if i%3==0:
            print()

def player1(s="Player 1"):
    __l1 = int(input(f"Enter your position {s}: "))
    return __l1,s
def player2(s="Player 2"):
    __l2 = int(input(f"Enter your position {s}: "))
    return __l2,s
def Bot():
    return rdi(1,9)
def gameLoop(p1="John",p2="Louis",bot=False):
    __turn1 = []
    __turn2 = []
    __win = [{1,2,3},{4,5,6},{7,8,9},
             {1,4,7},{2,5,8},{3,6,9},
             {1,5,9},{3,5,7}]
    
    B = board()
    if bot == False:

        while True:
            pos,n = player1(p1)
            # __turn1.append(pos)
            if logic(__win,pos,'x',B):
                print(f"{n} wins!!")
                break

            pos,n = player2(p2)
            # __turn2.append(pos)
            if logic(__win,pos,'o',B):
                print(f"{n} wins!!")
                break
    else:

        while True:
            pos,n = player1(p1)
            # __turn1.append(pos)
            if logic(__win,pos,'x',B):
                print(f"{n} wins!!")
                break

            pos,n = Bot(),"Bot"
            # __turn2.append(pos)
            if logic(__win,pos,'o',B,bot=True):
                print(f"{n} wins!!")
                break


def chkB(B,pos,bot=False):
        ch = ['x','o']
        if B[pos] in ch:
            if bot == False:
                pos = int(input("Re Enter Positon"))
            else:
                pos = Bot()
            pos = chkB(B,pos,bot)
        return pos


def logic(win,pos,op,B,bot=False):

    if bot == False:
        pos = chkB(B,pos)
    else:
        pos = chkB(B,pos,bot=True)
        print("Bot Played...!")

        
    B[pos] = op

    displayBoard(B)

    s = {x for x in B if B[x]=='x'}
    for i in win:
        z = s - (s - i)
        if z in win:
            return True
    s1 = {y for y in B if B[y]=='o'}
    for j in win:
        w = s1 - (s1 - j)
        if w in win:
            return True
    return False

def menu():
    print("Hello user Would You like a TicTacToe Game.\nMenu:\
        \n1) With Player\n2) With Bot\n3) Exit.")
    ch = int(input("Enter Your choice: "))
    return ch
while True:
    ch = menu()
    if ch == 1:
        gameLoop(input("Enter player 1 name:"),input("Enter player 2 name:"))
    elif ch == 2:
        gameLoop(input("Enter player name:"),bot=True)
    else:
        print("Thank you!!")
        break