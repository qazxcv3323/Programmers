# ========================================
# level 2 : 영어 끝말잇기

def solution(n, words):
    answer = [0, 0]
    word = [words[0]]
    for i in range(1, len(words)):
        if word[-1][-1] == words[i][0] and words[i] not in word:
            word.append(words[i])
        else:
            answer.append((i % n) + 1)
            answer.append(i // n + 1)
            print(f'answer : {answer}')
            return answer[2:4]
            break
    return answer