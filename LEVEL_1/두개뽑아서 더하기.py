# ---------------------------------------------------
# - level1 :  두개뽑아서 더하기

import itertools

def solution(numbers):
    result = itertools.permutations(numbers, 2)
    answer = set()
    for i in result:
        answer.add(sum(i))
    return sorted(answer)