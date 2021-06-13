/**
 *    author:  youssef_boumhaout
 *    Platform : arena.moi
**/

n = input()
k = n.count("0")
r = n.count("1")
if k > r:
    print(k - r)
else:
    print(r-k)
