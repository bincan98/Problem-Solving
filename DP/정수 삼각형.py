##이것이 코딩테스트다  376p
#https://www.acmicpc.net/problem/1932
#DP
#20221121
answer = 0
n = int(input())
board = []
for i in range(n):
  board.append(list(map(int, input().split())))
#print(*board)
for j in range(1,n):
  for k in range(j+1):
    #print(j,k)
    maximum = 0
    if k - 1 >= 0:
      maximum = max(maximum, board[j-1][k-1])
    if j != k:
      maximum = max(maximum, board[j-1][k])
    board[j][k] += maximum 
for l in range(n):
  answer = max(answer, board[n-1][l])
print(answer)