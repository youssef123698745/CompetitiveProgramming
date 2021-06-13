/**
 *    author:  youssef_boumhaout
 *    Platform : arena.moi
**/

from sys import stdin
n, *arr = map(int,stdin.read().split())
res = arr[0] 
for i in range(1,n): res ^= arr[i] 
print(res)
