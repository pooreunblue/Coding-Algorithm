def add(arr, i, n):
    arr[0] = i % n + 1
    arr[1] = (i + n) // n
    return arr
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
                else:
                    add(answer, i, n)
                    break
            else:
                add(answer, i, n)
                break
    return answer