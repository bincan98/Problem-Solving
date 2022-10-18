#이것이 코딩테스트다  346p
#https://school.programmers.co.kr/learn/courses/30/lessons/60058
#구현, 재귀
#20221018
def solution(p):
    answer = ''
    
    def is_right(p):
        stk = []
        for a in p:
            if a == '(':
                stk.append(a)
            elif a == ')':
                if stk:
                    stk.pop()
                else:
                    return False
        if stk:
            return False
        else:
            return True
    
    def slicing(p):
        count_l = 0
        count_r = 0
        for i in range(len(p)):
            if p[i] == '(':
                count_l += 1
            elif p[i] == ')':
                count_r += 1
            if count_l != 0 and count_l == count_r:
                u = p[:i+1]
                v = p[i+1:]
                return u, v
    
    def remove_rotate(u):
        new = ''
        u = u[1:]
        u = u[:len(u)-1]
        if u:
            for a in u:
                if a == '(':
                    new += ')'
                elif a == ')':
                    new += '('
        return new
    
    
    def recursive(w):
        new = ""
        if not w:
            return w
        u, v = slicing(w)
        if is_right(u) == True:
            return u + recursive(v)
        elif is_right(u) == False:
            new += '('
            new += recursive(v)
            new += ')'
            new += remove_rotate(u)
            return new
            
    answer = recursive(p)
    return answer

print(solution("()))((()"))