# -------------------------------------------------
# - level1 : K번째 수

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer