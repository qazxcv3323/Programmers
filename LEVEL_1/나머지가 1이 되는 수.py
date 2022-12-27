# -------------------------------------------------
# - level1 : 나머지가 1이 되는 수 찾기

def solution(n):
    answer = 2
  
    while n % answer !=1 :
        answer += 1
    return answer