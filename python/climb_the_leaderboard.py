#!/usr/bin/env python3


def climbing_leaderboard(r, p):
    ranks = []
    for val in r:
        if val not in ranks:
            ranks.append(val)
    
    idx = len(ranks) - 1
    scr = []
    for x in p:
        while idx != -1 and ranks[idx] <= x:
            idx -= 1
        
        if idx == -1:
            scr.append(1)
        else:
            scr.append(idx + 2)

    for ele in scr:
        print(ele)


def main():
    r_size = int(input())
    r = list(map(int,input().split()))
    p_size = int(input())
    p = list(map(int,input().split()))
    climbing_leaderboard(r, p)


if __name__ == '__main__':
    main()