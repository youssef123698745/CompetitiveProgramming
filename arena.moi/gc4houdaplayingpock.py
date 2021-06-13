/**
 *    author:  youssef_boumhaout
 *    Platform : arena.moi
**/

for _ in range(int(input())):
    n=int(input())
    s=[*map(int,input().split())]
    cursum = s[0]
    maxsum = s[0]
    for i in range(1, len(s)):
        if (cursum < 0):
            cursum = s[i]
        else:
            cursum += s[i]
        if (cursum > maxsum):
            maxsum = cursum
    print(maxsum if maxsum>0 else "better luck next year")
