from collections import defaultdict


def solution(msg):
    answer = []
    str_key = defaultdict(int)

    for i in range(1, 27):
        str_key[chr(i + 64)] = i
    size = 26
    new_str = msg[0]

    for i in range(1, len(msg)):
        if new_str + msg[i] not in list(str_key.keys()):
            answer.append(str_key[new_str])
            size += 1
            str_key[new_str + msg[i]] = size
            new_str = msg[i]
        else:
            new_str += msg[i]

    if new_str not in list(str_key.keys()):
        answer.append(str_key[new_str[-1]])
    else:
        answer.append(str_key[new_str])

    return answer