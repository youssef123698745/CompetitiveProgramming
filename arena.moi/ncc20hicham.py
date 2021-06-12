/**
 *    author:  tourist
 *    platform : arena.moi       
**/

x,a,b = map(int,input().split())
p=input()
cnt=0
for i in range(a,b+1):
    if(i%x==0):
        if(all(j in p for j in str(i))):
             cnt+=1
print(cnt)
