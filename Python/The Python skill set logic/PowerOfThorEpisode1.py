# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

flagX,flagY ='',''
# game loop
while True:
    
    # Do not remove this line.
    # remaining_turns = int(input())  # The remaining amount of turns Thor can move. 

    if light_x - initial_tx != 0:
        if light_x > initial_tx:
            initial_tx += 1
            flagY = 'E'
        elif light_x < initial_tx:
            initial_tx -= 1
            flagY = 'W'
    else:
        flagY = ''
    if light_y - initial_ty != 0:
        if light_y > initial_ty:
            initial_ty += 1
            flagX = 'S'
        elif light_y < initial_ty:
            initial_ty -= 1
            flagX = 'N'
    else:
        flagX = ''


    print(flagX+flagY)
    if light_x == initial_tx and light_y == initial_ty:
        break
print("Thor reached the goal")