# ========================================
# level 1 : 정수 제곱근 판별
def solution(n):
    answer = 0
    if n != 0:
        n_sqrt = n ** 0.5
        if  n_sqrt  == int(n_sqrt):
            answer = (n_sqrt + 1) ** 2
        else:
            answer = -1
        return answer