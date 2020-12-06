#!/usr/bin/env python3


def climbing_leaderboard(r, p):    
    dist_r = []
    for ele in r:
        if ele in dist_r:
            dist_r.append(ele)

def main():
    r_size = int(input())
    r = list(map(int,input().split()))
    p_size = int(input())
    p = list(map(int,input().split()))
    climbing_leaderboard(r, p)


if __name__ == '__main__':
    main()