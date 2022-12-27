# ---------------------------------------------------
# - level1 :  이상한 문자만들기

def solution(s):
    answer = ''
    result = s.split(' ')
    for i in result:
        for j in range(len(i)):
            if j % 2 == 1 :
                answer += i[j].lower()
            else:
                answer += i[j].upper()
        answer += ' '
    return answer[:-1]