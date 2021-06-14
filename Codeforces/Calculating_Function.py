/**
 *    author:  youssef_boumhaout
 *    Platform : codeforces.com
**/

def solution():
        n = int(input())
        if n % 2 == 0:
                return n // 2
        else:
                return -(n + 1) // 2

print(solution())
