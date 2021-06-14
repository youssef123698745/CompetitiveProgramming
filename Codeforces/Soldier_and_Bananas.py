/**
 *    author:  youssef_boumhaout
 *    Platform : codeforces.com
**/

a,b,c = map(int,input().split())
sum = 0
for loop in range(0,c+1):
  sum = sum + a*loop
if sum > b:
  print(sum-b)
else:
  print(0)
