#!/usr/bin/env python3

def main():
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    
    hash_map = [0 for i in range(k)]
    for ele in arr:
        count = ele % k
        if count == 0:
            hash_map[count] = 1
        elif k % 2 == 0 and count == k//2:
            hash_map[count] = 1
        else:
            hash_map[count] += 1
            
    max_count = 0
    for i in range(0, k//2 + 1):
        if i != 0:
            count_one = hash_map[i]
            count_two = hash_map[k - i]
            max_count += max(count_one, count_two)
        else:
            max_count += hash_map[0]
    return max_count

val = main()
print(val)
