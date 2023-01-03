# level 0 : 숫자 찾기

def solution(num, k):
    answer = 0
    
    for i in range(len(str(num))):
        if str(num)[i] == str(k) :
            answer = i +1
            break
        elif str(k) not in str(num):
            return -1
    return answer

solution(123456, 7)