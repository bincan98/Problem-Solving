#이것이 코딩테스트다  149p
#DFS
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def is_valid_coord(y, x):
  return 0 <= y < N and 0 <= x < M

def dfs(graph, x, y, visited):
  visited[y][x] = True
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if is_valid_coord(ny,nx) and not visited[ny][nx] and ice_map[ny][nx] == '0':
      dfs(graph, nx, ny, visited)

N, M = map(int, input().split())

visited = [[False for _ in range(M) ] for _ in range(N)]
ice_map = [[] for _ in range(N)]
answer = 0

for i in range(N):
  ice_map[i] = input()

for k in range(N):
  for j in range(M):
    if not visited[k][j] and ice_map[k][j] == '0':
      answer += 1
      dfs(ice_map, j, k, visited)
print(answer)