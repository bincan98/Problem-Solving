import sys
input = sys.stdin.readline

a = set()
b = set()

N, M = map(int, input().split())
for _ in range(N):
  not_hear = input().strip()
  a.add(not_hear)
for _ in range(M):
  not_look = input().strip()
  b.add(not_look)

c = list(a & b)
c.sort()

print(len(c))
for i in c:
  print(i)