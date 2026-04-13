def solution(n, words):
    word_set = set()
    answer = [0,0]
    word_set.add(words[0])
    for i in range(1, len(words)):
        if i > 0:
            w = words[i-1][-1]
            if words[i].startswith(w):
                if words[i] not in word_set:
                    word_set.add(words[i])
                    print(word_set)
                else:
                    answer[0] = i % n + 1
                    answer[1] = (i + n) // n
                    break
            else:
                answer[0] = i % n + 1
                answer[1] = (i + n) // n
                break
    return answer