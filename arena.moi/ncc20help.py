/**
 *    author:  youssef_boumhaout
 *    platform : arena.moi
**/

list1=[]
t=int(input())
for _ in range(t):
    n=input().split()
    m=int(n[0])
    s=n[1]
    s=[i for i in s]
    s.pop(m-1)
    list1.append(s)
for i in range(t):
    print(i+1,"".join(list1[i]))
