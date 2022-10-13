import sys

input = sys.stdin.readline

N = int(input())

s1 = set()

for _ in range(N):
  a, b = input().split()
  if b == 'enter':
    s1.add(a)
  else:
    s1.remove(a)

s1 = list(s1)
s1.sort(reverse=True)

for i in s1:
  print(i)