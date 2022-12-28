# - level2 :  올바른 괄호

def solution(s):
    count = []
    for i in s:
        if i == '(':
            count.append(i)
        else:
            if count :
                count.pop()
            else:
                return False
            
    if count:
            return False

    return True
