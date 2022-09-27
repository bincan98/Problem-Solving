from heapq import heappop, heappush

heap = []
count = 0

N = int(input())
dasom = int(input())
for _ in range(N-1):
  a = int(input())
  heappush(heap, -a)

if N != 1:
  while -heap[0] >= dasom:
    heappush(heap, heappop(heap)+1)
    dasom += 1
    count += 1
print(count)