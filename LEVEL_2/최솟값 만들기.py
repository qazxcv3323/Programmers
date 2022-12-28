# ---------------------------------------------------
# - level2 :  최솟값 만들기

import numpy as np

def solution(A,B):
    answer = 0
    t = zip(sorted(A), sorted(B, reverse=True))
    for i,j in t:
        answer += (i * j)
    return answer