/**
 *    author:  youssef_boumhaout
 *    platform : arena.moi       
**/

n=int(input())
s=[*map(int,input().split())]
res=[]
cnt=0
for i in s:
        if(i):
            res.append(i)
        else:
            cnt+=1
res+=[0]*cnt
print(*res)
