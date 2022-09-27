n = int(input())



for _ in range(n):
  stk = []
  for a in input():
    if a == '(':
      stk.append(a)
    else: 
      if stk:
        stk.pop(0)
      else:
        stk.append(a)
        break
  if stk:
    print('NO')
  else:
    print('YES')

