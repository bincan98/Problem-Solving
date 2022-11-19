#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=S%2FW+문제해결&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=20&pageIndex=1
#D3
#구현
#20221119
def solution(lst, t):
    answer = 0
    for j in range(2, len(lst) - 2):
        maximum = 0
        maximum = max(maximum, lst[j - 2])
        maximum = max(maximum, lst[j - 1])
        maximum = max(maximum, lst[j + 1])
        maximum = max(maximum, lst[j + 2])
        if lst[j] - maximum > 0:
            answer += lst[j] - maximum
    print(f'#{t} {answer}')


if __name__ == '__main__':
    for i in range(10):
        T = int(input())
        buildings = list(map(int, input().split()))
        solution(buildings, i+1)
