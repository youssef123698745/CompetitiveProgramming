/**
 *    author:  tourist
 *    platform : arena.moi
**/


t = int(input())
for loop in range(t):
    def solution(n):
        if (n == 0): return 1
        elif (n <= 2): return n
        elif (n == 3): return 6
        elif (n == 4): return 4
        else: return 0
    print(solution(int(input())))
