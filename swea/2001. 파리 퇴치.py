#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1
#D2
#완전탐색
#20221114
def solution(lst, N, M, T):
    answer_candidate = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            result = 0
            for k in range(M):
                for l in range(M):
                    result += lst[i+k][j+l]
            answer_candidate.append(result)
    print(f'#{T} {max(answer_candidate)}')

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N, M = map(int, input().split())
        a = []
        for j in range(N):
            a.append(list(map(int, input().split())))
        solution(a, N, M, i+1)
