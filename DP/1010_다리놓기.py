#https://www.acmicpc.net/problem/1010
#DP
#20221109
N = int(input())

cache = [[0] * 30 for _ in range(30)]
cache[1][0] = 1
cache[1][1] = 1

for i in range(2,30):
  for j in range(30):
    cache[i][j] = cache[i-1][j-1] + cache[i-1][j]

for _ in range(N):
  a, b = map(int, input().split())
  print(cache[b][a])