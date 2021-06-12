/**
 *    author:  tourist
 *    platform : arena.moi
**/

for _ in range(int(input())):
    a,b=map(str,input().split())
    if(sorted(a)==sorted(b) and a[0]==b[0] and a[-1] == b[-1]):
        print("Awesome anagram")
    else:
        print("Azuz is not my leader")
