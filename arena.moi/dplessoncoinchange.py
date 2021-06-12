/**
 *    author:  youssef_boumhaout
 *    platform : arena.moi       
**/

from sys import stdin,stdout
def cont(S, m, n): 
    table = [0 for k in range(n+1)] 
    table[0] = 1
    for i in range(0,m): 
        for j in range(S[i],n+1): 
            table[j] += table[j-S[i]] 
    return table[n]
def main():
    S,k=map(int,stdin.readline().rstrip("\n").split())
    arr=list(map(int,stdin.readline().rstrip("\n").split()))
    ans=cont(arr,k,S)
    stdout.write(str(ans)+"\n")
main()
