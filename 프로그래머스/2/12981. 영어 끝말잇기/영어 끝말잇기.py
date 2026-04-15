def solution(n, words):
    word_set = set()
    word_set.add(words[0])
    for i in range(1, len(words)):
        pre_word = words[i-1][-1]
        if words[i] in word_set or words[i][0] != pre_word: 
            return [i % n + 1, i // n + 1]
        word_set.add(words[i])
    return [0,0]