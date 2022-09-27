from heapq import heappush, heappop

n, m = map(int, input().split())

is_possible = 1
heap = []

for gift in map(int, input().split()):
  heappush(heap, -gift)

for child in map(int, input().split()):
  max = -heappop(heap)
  if max < child:
    is_possible = 0
    break
  else:
    heappush(heap, -(max - child))

print(is_possible)

#max_heap은 -를 붙이면서 이용하기 대신 pop과 push할 때 모두 주의!!
