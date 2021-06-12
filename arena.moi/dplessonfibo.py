/**
 *    author:  youssef_boumhaout
 *    platform : arena.moi       
**/

MOD = 10**9 +7
fn=[0,1]
for i in range(2,10**6+1):
    fn.append((fn[i-1]+fn[i-2])%MOD)
q= int(input())
for i in range(q):
    n = int(input())
    print(fn[n])
