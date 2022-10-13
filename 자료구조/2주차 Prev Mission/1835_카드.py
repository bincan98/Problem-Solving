from collections import deque

n = int(input())

d = deque()

for i in range(n, 0, -1):
  d.appendleft(i)
  for _ in range(i):
    d.appendleft(d.pop())

print(*list(d))

#테스트