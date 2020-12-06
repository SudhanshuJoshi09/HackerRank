#!/usr/bin/env python3

from itertools import *

X = []
X.extend(list(map(int,input().split())))
X.extend(list(map(int,input().split())))
X.extend(list(map(int,input().split())))


# This is the maximum sum possible
ans = 81
for p in permutations(1, 10):
    # if first row sum is 15 and second row sum is 15 then definately sum of the third row would be 15
    # if first col sum is 15 and second col sum is 15 then definately sum of the third col would be 15
    if (sum(p[0:3]) == 15) and (sum(p[3:6]) == 15) and (sum(p[0::3]) == 15) and (sum(p[1::3]) == 15) and ((p[0] + p[4] + p[8]) == 15) and ((p[2] + p[4] + p[6]) == 15):
        ans = min(ans, sum(abs(p[i] - X[i] for i in range(0, 9))))

print(ans)