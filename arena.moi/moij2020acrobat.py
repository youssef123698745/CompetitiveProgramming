/**
 *    author:  youssef_boumhaout
 *    platform : arena.moi       
**/

t = int(input())
l = 0
g = int(1e9) + 7
for i in range(t):
    l = int(input())
    print((l*(l - 1)//2 + 1) % g)
