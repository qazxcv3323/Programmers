# ========================================
# level 1 : 부족한 금액 계산하기
def solution(price, money, count):
    result = price
    for i in range(0, count):
        money -= price
        price += result
    if money > 0 :
        return 0
    else:
        return abs(money)


solution(3,20,4)