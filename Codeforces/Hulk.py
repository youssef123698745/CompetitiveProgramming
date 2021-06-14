/**
 *    author:  youssef_boumhaout
 *    Platform : codeforces.com
**/

n = int(input())
if n == 1:
  print('I hate it')
else:
  print('I hate',end='')
  for i in range(2,n+1):
    if i % 2 == 0:
      print(' that I love',end='')
    else:
        print(' that I hate',end='')
  print(' it')
