from collections import deque

N, K = map(int, input().split())

result = []
dq = deque(range(1, N+1))

while dq:
  for i in range(K-1):
    dq.append(dq.popleft())
  result.append(dq.popleft())

print('<', end='')
print(result[0], end= '')
for j in range(1,len(result)):
  print(', ', end='')
  print(result[j],end='')
print('>')