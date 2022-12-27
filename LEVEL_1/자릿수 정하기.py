# ---------------------------------------------------
# - level1 : 자릿수 정하기

def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)

    return answer