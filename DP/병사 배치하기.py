#이것이 코딩테스트다 380p
#https://www.acmicpc.net/problem/18353
#DP
#20221130
N = int(input())
lst = list(map(int, input().split()))

cache = [1] * N

for i in range(1, N):
  for j in range(i):
    if lst[j] > lst[i]:
      cache[i] = max(cache[i], cache[j] + 1)

print(N - max(cache))