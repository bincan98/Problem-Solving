#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PyTLqAf4DFAUq&categoryId=AV5PyTLqAf4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1
#D2
#구현
#20221114
def solution(lst, t):
    is_palin = -1
    for i in range(len(lst)//2):
        if lst[i] != lst[-(i+1)]:
            is_palin = 0
            break
        else:
            is_palin = 1
            continue
    print(f'#{t} {is_palin}')

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = list(input())
        solution(a, i+1)
