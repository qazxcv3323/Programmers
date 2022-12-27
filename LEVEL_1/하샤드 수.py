# -------------------------------------------------
# - level1 : 하샤드 수 

def solution(x):
    x = str(x)
    n = int(x[0]) + int(x[1]) 
    if int(x) % n == 0:
        answer = True
        return answer
    else:
        answer = False
        return answer