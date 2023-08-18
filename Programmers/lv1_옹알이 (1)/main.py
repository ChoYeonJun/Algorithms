def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    for j, w in  enumerate(babbling):
        for i in range(len(words)*4):
            word = words[i%4]
            if babbling[j].startswith(word):
                babbling[j] = babbling[j].replace(word, '')
            if babbling[j] == '':
                answer += 1
                break
        print(answer)
    return answer

babbling = ["aya", "yee", "u", "maa", "wyeoo"]
print(solution(babbling))