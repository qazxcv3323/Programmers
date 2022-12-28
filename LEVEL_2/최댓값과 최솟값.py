def solution(s):
    split_list = s.split(' ')
    answer = ''
    for i in split_list:
        result = str(i)
        answer += result.capitalize() + ' '
    return answer[:-1]