/**
 *    author:  youssef_boumhaout
 *    platform : arena.moi       
**/
import math

def solution(n, K):
  return K + math.floor((K - 1) / (N - 1))
t = int(input())
for loop in range(t):
  N,K = map(int,input().split())
  print(solution(N, K))
