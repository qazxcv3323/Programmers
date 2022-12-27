# -------------------------------------------------
# - level1 : 문자열 내마음대로 정렬하기

def solution(strings, n):
    strings.sort()
    answer =sorted(strings, key = (lambda x: x[n]))
    
    return answer