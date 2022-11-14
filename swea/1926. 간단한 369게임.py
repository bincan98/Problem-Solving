#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PTeo6AHUDFAUq&categoryId=AV5PTeo6AHUDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1
#D2
#구현
#20221114
def solution(N):
    for i in range(1,N+1):
        a = list(str(i))
        if '3' in a or '6' in a or '9' in a:
            for j in range(a.count('3')+a.count('6')+a.count('9')):
                print('-',end='')
            print(' ',end='')
        else:
            print(i,end=' ')


if __name__ == '__main__':
    N = int(input())
    solution(N)
