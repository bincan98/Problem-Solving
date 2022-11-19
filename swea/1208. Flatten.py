#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=S%2FW+문제해결+기본&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2
#D3
#구현
#20221119
def solution(lst, count, t):
    answer = 0
    for _ in range(count):
        lst.sort()
        if max(lst) - min(lst) <= 1:
            break
        lst[lst.index(max(lst))] -= 1
        lst[lst.index(min(lst))] += 1
    print(f'#{t} {max(lst) - min(lst)}')


if __name__ == '__main__':
    for i in range(10):
        T = int(input())
        boxes = list(map(int, input().split()))
        solution(boxes, T, i+1)
