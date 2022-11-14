#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=30&pageIndex=1
#D2
#구현
#20221114
def solution(a, N, index):
    answer = 0
    maximum = 0
    for i in range(N-1,-1,-1):
        maximum = max(a[i],maximum)
        if maximum == a[i]:
            continue
        else:
            answer += maximum - a[i]

    print(f'#{index} {answer}')


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        a = list(map(int, input().split()))
        solution(a, N, i+1)
