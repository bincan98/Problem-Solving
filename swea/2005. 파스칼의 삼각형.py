#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5P0-h6Ak4DFAUq&categoryId=AV5P0-h6Ak4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1
#D2
#구현
#20221114
def solution(N, T):
    lst = [[0] * N for _ in range(N)]
    for i in range(N):
        lst[i][0] = 1

    for j in range(1,N):
        for k in range(1,N):
            lst[j][k] = lst[j-1][k-1] + lst[j-1][k]

    print(f'#{T}')
    for l in range(N):
        for m in range(N):
            if lst[l][m] != 0:
                print(f'{lst[l][m]}', end=' ')
        print()

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        solution(N, i+1)
