# -------------------------------------------------
# - level1 : 삼총사 

import itertools

def solution(number):
    answer = 0
    three= itertools.combinations(number, 3)
    for i in three:
        result = sum(i)
        if result == 0:
            answer += 1
    return answer