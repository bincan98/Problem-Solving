#이것이 코딩테스트다  341p
#https://www.acmicpc.net/problem/14502
#DFS
#20221018
import sys

input = sys.stdin.readline

dx = [0, -1, 0 ,1]
dy = [-1, 0, 1, 0]

N, M = map(int, input().split())

lab = []

for i in range(N):
  lab.append(list(map(int,input().split())))
#print(lab)
temp = [[0] * M for _ in range(N)]
safety_score = 0

def is_valid_coord(y,x):
  return 0 <= y < N and 0 <= x < M

def score(temp):
  score = 0
  for i in range(N):
    for j in range(M):
      if temp[i][j] == 0:
        score += 1
  return score

def dfs(temp, y, x):
  for r in range(4):
    nx = x + dx[r]
    ny = y + dy[r]
    if is_valid_coord(ny,nx) and temp[ny][nx] == 0:
      temp[ny][nx] = 2
      dfs(temp,ny,nx)
  #print(f'temp : {temp}')

for i in range(N * M):
  y1 = i // M
  x1 = i % M
  
  if lab[y1][x1] == 1 or lab[y1][x1] == 2:
    continue
  for j in range(N * M):
    y2 = j // M
    x2 = j % M
    if lab[y2][x2] == 1 or lab[y2][x2] == 2 or i == j:
      continue
    for k in range(N * M):
      y3 = k // M
      x3 = k % M
      if lab[y3][x3] == 1 or lab[y3][x3] == 2 or j == k or i == k:
        continue
      
      lab[y1][x1] = 1
      lab[y2][x2] = 1
      lab[y3][x3] = 1
      
      for p in range(N):
        for q in range(M):
          temp[p][q] = lab[p][q]
      
      for l in range(N):
        for m in range(M):
          if lab[l][m] == 2:
            dfs(temp, l, m)
      
      safety_score = max(safety_score ,score(temp))
      
      #print(f'lab : {lab}')
      lab[y1][x1] = 0
      lab[y2][x2] = 0
      lab[y3][x3] = 0

print(safety_score)