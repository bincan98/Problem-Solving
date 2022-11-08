#이것이 코딩테스트다 217p
#DP
#20221108
N = int(input())

cache = [-1] * (N+1)

cache[1] = 0
cache[2] = 1
cache[3] = 1
cache[4] = 2
cache[5] = 1

for i in range(6, N+1):
  cache[i] = cache[i-1] + 1
  
  if i % 5 == 0:
    cache[i] = min(cache[i],cache[i//5] + 1)
  if i % 3 == 0:
    cache[i] = min(cache[i],cache[i//3] + 1)
  if i % 2 == 0:
    cache[i] = min(cache[i],cache[i//2] + 1)

print(cache[N])