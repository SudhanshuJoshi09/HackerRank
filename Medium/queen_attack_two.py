#!/usr/bin/env python3

def check(n, k, row, col, blocks):
    row -= 1
    col -= 1

    ur = min(row, abs(col - (n - 1)))
    ul = min(row, col)
    lr = min(abs(row - (n - 1)), abs(col - (n - 1)))
    ll = min(abs(row - (n - 1)), col)
    uv = row
    lv = abs(n - row) - 1
    lh = col
    rh = abs(n - col) - 1
    
    if k == 0:
        return ur + ul + lr + ll + uv + lv + lh + rh

    for x, y in blocks:
        x -= 1
        y -= 1
        if (x-y) == (row-col):
            if row > x:
                ul = min(ul, abs(row - x) - 1)
            else:
                lr = min(lr, (x - row) - 1)
        elif (x+y) == (row+col):
            if row > x:
                ur = min(ur, (row - x) - 1)
            else:
                ll = min(ll, abs(x - row) - 1)
        if x == row and y != col:
            if y < col:
                lh = min(lh, abs(y - col) - 1)
            else:
                rh = min(lv, abs(col - y) - 1)
        elif y == col and row != x:
            if x < row:
                uv = min(uv, abs(x - row) - 1)
            else:
                lv = min(lv, abs(row - x) - 1)
    return ur + ul + lr + ll + uv + lv + lh + rh


n, k = map(int, input().split())
if n != 0:
    q_r, q_c = map(int, input().split())
    obst = []
    for i in range(k):
        r, c = map(int, input().split())
        obst.append([r, c])
    val = check(n, k, q_r, q_c, obst)
    print(val)
else:
    print(0)