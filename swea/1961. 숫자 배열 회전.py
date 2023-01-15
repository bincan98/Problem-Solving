#https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYUu1hG6O44DFARs&contestProbId=AV5Pq-OKAVYDFAUq&probBoxId=AYUyLam6ojkDFARs&type=PROBLEM&problemBoxTitle=알고리즘+Track+%28난이도+중%29&problemBoxCnt=5
#D2
#구현
#20230115
def solution(t):
    matrix = []
    N = int(input())
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    
    #print(*matrix)
    print(f'#{t}')
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            print(matrix[j][(N-1)-i], end="")
        print(end=" ")
        for k in range(N-1,-1,-1):
            print(matrix[i][k], end="")
        print(end=" ")
        for l in range(N):
            print(matrix[l][i], end="")
        print()


if __name__ == '__main__':
    T = int(input())
    for testcase in range(1, T+1):
        solution(testcase)