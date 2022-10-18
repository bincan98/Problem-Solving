#이것이 코딩테스트다  339p
#https://www.acmicpc.net/problem/18352
#BFS, 완전탐색
#20221017
from collections import deque
import sys

input = sys.stdin.readline

def bfs(graph, start, N):
  queue = deque()
  visited = [False] * (N+1)
  queue.append((start, 0))
  visited[start] = True
  city_cost = [-1] * (N+1)
  
  while queue:
    v, d = queue.popleft()
    
    d += 1
    for k in graph[v]:
      if not visited[k]:
        queue.append((k, d))
        visited[k] = True
        city_cost[k] = d
  return city_cost

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
city_cost = [-1] * (N+1)

for i in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
#print(graph)


city_cost = bfs(graph, X, N)
#print(city_cost)


for k in range(len(city_cost)):
  if K == city_cost[k]:
    print(k)

if K not in city_cost:
  print(-1)