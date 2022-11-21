#이것이 코딩테스트다  149p
#DFS
#20221120
dx = [0,1,0,-1]
dy = [1,0,-1,0]

if __name__ == '__main__':
    N, M = map(int, input().split())
    board = []
    answer = 0
    for i in range(N):
        board.append(list(map(int, input())))

    def is__coord(y, x):
        return 0 <= y < N and 0 <= x < M

    def dfs(y, x):

        if board[y][x] == 1:
            return

        board[y][x] = 1

        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]
            if is__coord(ny, nx) and board[ny][nx] == 0:
                dfs(ny, nx)

    for j in range(N):
        for k in range(M):
            if board[j][k] == 0:
                answer += 1
                dfs(j, k)
    print(answer)