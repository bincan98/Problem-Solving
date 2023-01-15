#https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYUu1hG6O44DFARs&contestProbId=AV5Psz16AYEDFAUq&probBoxId=AYUyLam6ojkDFARs&type=PROBLEM&problemBoxTitle=알고리즘+Track+%28난이도+중%29&problemBoxCnt=5
#D2
#구현
#20230115
def solution(t):
    matrix = []
    answer = 1
    for _ in range(9):
        matrix.append(list(map(int, input().split())))
    
    #print(*matrix)
    
    for i in range(9):
        dx = [0,0,0,0,0,0,0,0,0]
        for j in range(9):
            dx[matrix[i][j]-1] += 1
        if 0 in dx:
            answer = 0
            break

    for k in range(9):
        dx = [0,0,0,0,0,0,0,0,0]
        for l in range(9):
            dx[matrix[l][k]-1] += 1
        if 0 in dx:
            answer = 0
            break
    
    for m in range(3):
        for n in range(3):
            dx = [0,0,0,0,0,0,0,0,0]
            for o in range(3):
                for p in range(3):
                    dx[matrix[m*3+o][n*3+p]-1] += 1
            if 0 in dx:
                answer = 0
                break
    print(f'#{t} {answer}')


if __name__ == '__main__':
    T = int(input())
    for testcase in range(1, T+1):
        solution(testcase)