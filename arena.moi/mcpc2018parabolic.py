/**
 *    author:  youssef_boumhaout
 *    Platform : arena.moi
**/

from math import sqrt,ceil
for _ in range(int(input())):
    n,x,y=map(int,input().split())
    print(ceil(sqrt(x**2+4*n**2 * y**2)))
