# ========================================
# level 1 : x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []
    define = x
    for i in range(n):
        answer.append(x)
        x = x + define
    return answer