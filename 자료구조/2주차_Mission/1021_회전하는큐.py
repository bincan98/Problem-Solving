from collections import deque
from operator import index

dq = deque()
count = 0

N, M = map(int, input().split())
for i in range(1,N+1):
  dq.append(i)

a = list(map(int, input().split()))

for j in range(M):
  while a[0] != dq[0]:
    if dq.index(a[0]) < len(dq)/2:
      dq.append(dq.popleft())
      count += 1
    else:
      dq.appendleft(dq.pop())
      count += 1
  a.pop(0)
  dq.popleft()
print(count)