#이것이 코딩테스트다 226p
#DP
#20221110
N, M = map(int, input().split())
bills = []
for _ in range(N):
  bills.append(int(input()))

bills.sort()
cache = [10001] * (M+1)

cache[0] = 0

for bill in bills:
  for i in range(bill,M+1):
    cache[i] = min(cache[i],cache[i-bill]+1)
if cache[M] == 10001:
  print(-1)
else:
  print(cache[M])