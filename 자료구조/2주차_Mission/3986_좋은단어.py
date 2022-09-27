N = int(input())

stk = []
count = 0

for _ in range(N):
  for a in input():
    if stk:
      if a == stk[-1]:
        stk.pop()
      else:
        stk.append(a)
    else:
      stk.append(a)
  if len(stk) == 0:
    count += 1
  stk = []
print(count)