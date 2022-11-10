#이것이 코딩테스트다 223p
#https://www.acmicpc.net/problem/11727
#DP
#20221110
Number = 10007

N = int(input())

cache = [0] * 1001
cache[1] = 1
cache[2] = 3

for i in range(3,N+1):
  cache[i] = (cache[i-1] + 2 * cache[i-2]) % Number
print(cache[N])