import pandas as pd
import numpy as np
df = pd.read_csv("input.txt", header=None)
hx = 0
hy = 0
tx = 0
ty = 0

hx_list = []
hy_list = []

def movement_hd(move):
    x = 0
    y = 0
    if move == 'R':
        x += 1
        return x
    elif move == 'L':
        x += -1
        return x
    elif move == 'U':
        y += 1
        return y
    elif move == 'D':
        y -= 1
        return y
df[['movement', 'times']] = df[0].str.split(" ",expand=True)
Hd_mvmnt  =[(0, 0)]
Tl_mvmnt = [(0,0)]
index = 0
for item in df['movement']:
    print(f"{item} : {df['times'][index]}")
    for count in range(int(df['times'][index])):
        if item == "R" or item == 'L':
            hx += movement_hd(item)
            # Compare x distance b/w head and tail
            if hx-tx == 2 and hy-ty == 0:
                tx += 1
            elif hx-tx == -2 and hy-ty == 0:
                tx -= 1
            #elif hx - tx != 0 and hy - ty != 0:
            elif hx - tx == 2 and hy > ty:
                tx += 1
                ty += 1
            elif hx - tx == 2 and hy < ty:
                tx += 1
                ty -= 1
            elif hx - tx == -2 and hy > ty:
                tx -= 1
                ty += 1
            elif hx - tx == -2 and hy < ty:
                tx -= 1
                ty -= 1
        elif item == "U" or item == 'D':
            hy += movement_hd(item)
            # Compare y distance b/w head and tail
            if hy - ty == 2 and hx - tx == 0:
                ty += 1
            elif hy - ty == -2 and hx - tx == 0:
                ty -= 1
            # elif hx - tx != 0 and hy - ty != 0:
            elif hy - ty == 2 and hx > tx:
                tx += 1
                ty += 1
            elif hy - ty == 2 and hx < tx:
                ty += 1
                tx -= 1
            elif hy - ty == -2 and hx > tx:
                ty -= 1
                tx += 1
            elif hy - ty == -2 and hx < tx:
                ty -= 1
                tx -= 1
        Hd_mvmnt.append((hx, hy))
        Tl_mvmnt.append((tx, ty))
    index += 1
print(len(set(Tl_mvmnt)))
count1 = 0
for item in range(len(Tl_mvmnt)-1):
    if Tl_mvmnt[item] != Tl_mvmnt[item+1]:
        count1 += 1
print(count1)