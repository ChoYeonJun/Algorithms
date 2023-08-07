from collections import defaultdict

def solution(k, tangerine):
    tang_dict = defaultdict(int)
    for num in tangerine:
        tang_dict[num] += 1

    key = sorted(list(tang_dict.keys()), key=lambda x: tang_dict[x], reverse=True)
    answer = 0
    while k > 0:
        num = tang_dict[key[answer]]
        answer += 1
        k -= num

    return answer