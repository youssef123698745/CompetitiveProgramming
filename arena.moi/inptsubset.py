/**
 *    author:  youssef_boumhaout
 *    Platform : arena.moi
**/

from sys import stdin
from itertools import combinations
n, k = map(int,stdin.readline().split())
arr = list(map(int,stdin.readline().split()))
r = 0
for i in range(1,n+1):
    for j in combinations(arr,i):
        if sum(j) == k:
            r += 1
print(r)
