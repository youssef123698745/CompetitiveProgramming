/**
 *    author:  youssef_boumhaout
 *    platform : arena.moi
**/

maxi = 0
n=int(input())
a = [*map(int,input().split())]
lis = [1]*n
for i in range(1,n):
    for j in range(i):
        if(a[i]>a[j] and lis[i]<lis[j]+1):
            lis[i] = lis[j]+1
for i in range(n):
    maxi = max(maxi,lis[i])
print(maxi)
