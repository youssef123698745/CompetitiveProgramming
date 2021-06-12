/**
 *    author:  youssef_boumhaout
 *    platform : arena.moi       
**/

n=int(input())
a = [*map(int,input().split())]
maxi = a[0]
curr = a[0]
for i in range(1,n):
            curr = max (a[i] , curr + a[i])
            maxi = max(maxi , curr)
print(maxi)
