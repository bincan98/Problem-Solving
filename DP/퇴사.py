#이것이 코딩테스트다  377p
#https://www.acmicpc.net/problem/14501
#DP
#20221121
N = int(input())
table = [[0,0]]
for _ in range(N):
  table.append(list(map(int, input().split())))
cache = [0] * (N + 2)
if table[N][0] == 1:
  cache[N] = table[N][1]
else:
  cache[N] = 0
#print(*table)
for i in range(N - 1, 0, -1):
  if i + table[i][0] <= N + 1:
    cache[i] = max(table[i][1] + cache[i + table[i][0]],cache[i+1])
  else:
    cache[i] = cache[i+1]
print(cache[1])