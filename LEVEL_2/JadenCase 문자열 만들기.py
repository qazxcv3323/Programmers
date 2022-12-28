# ---------------------------------------------------
# - level2 :  JadenCase 문자열 만들기

def solution(s):
    split_list = s.split(' ')
    answer = ''
    for i in split_list:
        result = str(i)
        answer += result.capitalize() + ' '
    return answer[:-1]