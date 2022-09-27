import sys

input = sys.stdin.readline

while True:
  n, m = map(int, input().split())
  if n == 0 and m == 0:
    break

  p = set()
  q = set()

  for _ in range(n):
    p.add(input())

  for _ in range(m):
    q.add(input())
  
  print(len(p & q))



#집합은 add
#집합 선언은 set()
#입력이 한줄 마다 최대 백만씩 있을 수 있으므로 readline을 이용하였다. 
# 결과 print를 한 케이스에서 바로하지 않아서 틀렸다.