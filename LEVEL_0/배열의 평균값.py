def solution(numbers):
    sum = 0
    avr = len(numbers)
    for i in numbers:
        sum += i
    answer = sum / avr
    return answer