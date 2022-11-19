#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15FZuqAL4CFAYD&categoryId=AV15FZuqAL4CFAYD&categoryType=CODE&problemTitle=S%2FW+문제해결+응용&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
#D3
#구현
#20221119
decode = ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]


def solution(lst, n, m, t):
    answer = 0
    start_index_y = 0
    start_index_x = 0
    slicing = []

    for k in range(n):
        for l in range(m):
            if lst[k][l] == '1':
                start_index_y = k
                start_index_x = l
                break

    slicing.append(lst[start_index_y][start_index_x - 1:])
    if start_index_x - 2 >= 0:
        slicing.append(lst[start_index_y][start_index_x - 2:])
    if start_index_x - 3 >= 0:
        slicing.append(lst[start_index_y][start_index_x - 3:])

    for sl in slicing:
        code = []
        for m in range(8):
            if sl[m * 7:m * 7 + 7] in decode:
                code.append(decode.index(sl[m * 7:m * 7 + 7]))
            else:
                break
        if len(code) == 8:
            break

    result = 0
    for n in range(8):
        if (n + 1) % 2 == 0:
            result += code[n]
        else:
            result += code[n] * 3

    if result % 10 == 0 and result != 0:
        for o in range(8):
            answer += code[o]
    else:
        answer = 0

    print(f'#{t} {answer}')


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        matrix = []
        N, M = map(int, input().split())
        for j in range(N):
            matrix.append(input())
        solution(matrix, N, M, i + 1)
