# 14 : 10 start
from collections import deque

    # print(result)
    # cnt = 0
    # for i in range(len(result)+1):
    #     result.rotate(-1)
    #     if result[0] == result[1]:
    #         cnt += 1
    #         print(cnt)

def solution(board, moves):
    answer = 0
    result = deque()
    
    for column in moves:
        column -= 1 
        for idx in range(len(board)): 
            if board[idx][column] != 0: 
                doll = board[idx][column]
                print(f'doll : {doll}')
                board[idx][column] = 0 
                try:
                    if doll != result[-1]: 
                        result.append(doll)
                        # print(f'result : {result}, doll : {doll}')
                    else: 
                        result.pop()
                        answer += 1
                except:
                    result.append(doll)
                    # print(f'except_result : {result}')
                break

    return answer * 2
    
solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])

# 15:31 finish
