#이것이 코딩테스트다 220p
#DP
#20221109
N = int(input())
store = list(map(int, input().split()))

cache = [-1] * (N+1)

cache[0] = 0
cache[1] = store[-1]

for i in range(2,N+1):
  cache[i] = max(cache[i-1],cache[i-2] + store[N-i])
print(cache[N])