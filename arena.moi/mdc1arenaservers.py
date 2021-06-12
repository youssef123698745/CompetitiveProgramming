/**
 *    author:  tourist
 *    platform : arena.moi
**/



import math

t = int(input())
while(t):
  a,b = map(int,input().split())
  arr = list(map(int,input().split()))
  l = []
  for i in arr:
    k = math.ceil(i/b)
    l.append(k)
  print(sum(l))
  t = t - 1
