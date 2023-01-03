# ========================================
# level 1 : 문자열 낸 p와 y의 갯수

# def solution(s):
#     p_count = 0 ; y_count = 0
    
#     for i in s:
#         if i.lower() == 'p':p_count += 1
#         elif i.lower() == 'y': y_count += 1
#         else:continue
        
#     if p_count == y_count:answer = True
#     else:answer = False
#     return answer



def solution(s):
    return s.lower().count('p') == s.lower().count('y')
