#이것이 코딩테스트다  344p
#https://www.acmicpc.net/problem/18405
#BFS
#20221018
from collections import deque
import sys

input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

N, K = map(int, input().split())
lab = []
virus_data = []

for _ in range(N):
  lab.append(list(map(int, input().split())))

#data에 바이러스의 번호, 시간, y, x 저장
for j in range(N):
  for k in range(N):
    if lab[j][k] != 0:
      virus_data.append([lab[j][k], 0, j, k])

S, X, Y = map(int, input().split())

virus_data.sort()
q = deque(virus_data)

def is_valid_coord(y, x):
  return 0 <= y < N and 0 <= x < N

def bfs(virus_num, y, x):
  #queue = deque(virus_num)
  
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if is_valid_coord(ny, nx) and lab[ny][nx] == 0:
      lab[ny][nx] = virus_num

while q:
  virus_num, s, y, x = q.popleft()
  
  if s == S:
    break
  
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if is_valid_coord(ny, nx) and lab[ny][nx] == 0:
      lab[ny][nx] = virus_num
      q.append([virus_num, s+1, ny, nx])

#print(lab)
print(lab[X-1][Y-1]) 