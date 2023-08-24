def solution(want, number, discount):
    answer = 0
    dict_want = {k: v for v, k in enumerate(want)}
    total = sum(number)
    for i in range(total, len(discount) + 1):
        l = discount[i - total:i]
        num = number[:]

        for item in l:
            if item in want:
                idx = dict_want.get(item)
                if idx != None and num[idx] > 0:
                    num[idx] -= 1
                    # print(num)
        if sum(num) == 0:
            answer += 1
    return answer