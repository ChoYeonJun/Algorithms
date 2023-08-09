from itertools import permutations


def solution(k, dungeons):
    answer = -1
    l = list(permutations(dungeons, len(dungeons)))
    for sub_l in l:
        cnt = 0
        limit = k
        for need, lose in sub_l:
            if need <= limit:
                limit -= lose
                cnt += 1
            answer = max(answer, cnt)

    return answer