#이것이 코딩테스트다  152p
#BFS
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def is_valid_coord(y, x):
  return 0 <= y < N and 0 <= x < M

def bfs(y, x):
  queue = deque([[y, x]])
  
  visited[y][x] = True
  
  while queue:
    v = queue.popleft()
    
    if v == [N-1,M-1]:
      return miro[N-1][M-1]
    
    for i in range(4):
      ny = v[0] + dy[i]
      nx = v[1] + dx[i]
      if is_valid_coord(ny, nx) and not visited[ny][nx] and miro[ny][nx] != 0:
        queue.append([ny,nx])
        visited[ny][nx] = True 
        miro[ny][nx] = miro[v[0]][v[1]] + 1

N, M = map(int, input().split())
miro = []
visited = [[False for _ in range(M)] for _ in range(N)]

for i in range(N):
  miro.append(list(map(int, input())))

print(bfs(0,0))