#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=S%2FW+문제해결+기본&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2
#D3
#구현
#20221119
def solution(lst, t):
    answer = []
    for k in range(100):
        result = 0
        for l in range(100):
            result += lst[k][l]
        answer.append(result)

    for m in range(100):
        result = 0
        for n in range(100):
            result += lst[n][m]
        answer.append(result)

    result = 0
    for o in range(100):
        result += lst[o][o]
    answer.append(result)

    result = 0
    for p in range(100):
        result += lst[p][99-p]
    answer.append(result)

    print(f'#{t} {max(answer)}')


if __name__ == '__main__':
    for i in range(10):
        matrix = []
        T = int(input())
        for j in range(100):
            matrix.append(list(map(int, input().split())))
        solution(matrix, T)
