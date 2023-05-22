import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
for i in range(h):
    row = input()

r1 = ' #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ### '
r2 = '# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   # '
r3 = '### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ## '
r4 = '# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #       '
r5 = '# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #  '
united = [r1, r2, r3, r4, r5]

# for i in range(len(united)):
#     united[i] = united[i].replace('#','-')


for i in united:
    for chart in t:
        if chart.upper() in [chr(x).upper() for x in range(65,92)]:
            cord = ord(chart.upper())-65
        else:
            cord = 26
        print(i[cord*4:(cord*4)+4],end='')
    print()
