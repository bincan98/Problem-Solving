#이것이 코딩테스트다 375p
#DP
#20221121
T = int(input())
for i in range(T):
  answer = 0
  n, m = map(int, input().split())
  lst = list(map(int, input().split()))
  board = [[] for _ in range(n)]
  for j in range(n):
    board[j] = lst[j*m:(j+1)*m]
  #print(*lst)
  #print(*board)
  for k in range(m-2, -1, -1):
    for l in range(n):
      maximum = 0
      maximum = max(maximum,board[l][k+1])
      if l-1 >= 0:
        maximum = max(maximum,board[l-1][k+1])
      if l+1 <= n-1:
        maximum = max(maximum,board[l+1][k+1])
      board[l][k] += maximum
  for o in range(n):
    answer = max(answer,board[o][0])
  print(answer)