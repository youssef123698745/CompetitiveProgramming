/**
 *    author:  youssef_boumhaout
 *    platform : arena.moi       
**/

MOD = 10**9 + 7
for _ in range(int(input())):
    n, m = map(int, input().split())
    res = 1
    for i in range(n,n + m - 1):
        res *= i
        res //= (i-n+1)
    print(res%MOD)
