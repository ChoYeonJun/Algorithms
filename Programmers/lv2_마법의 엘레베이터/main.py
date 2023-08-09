def solution(storey):
    answer = 0
    i = -1
    while storey != 0:
        i += 1
        str_storey = str(storey)[::-1]
        num = int(str_storey[i])
        if num == 0:
            continue
        digit_10 = 10 ** i
        if num > 5 :
            storey += (10 * digit_10) - (num * digit_10)
            answer += (10 - num)
            continue
        elif num == 5 and i+1 < len(str_storey):
            answer += 5
            # 35 일때는 -1 * 5 , -10 * 3 이 최소이고
            # 75 일 때는 +1 * 5 , 10 * 2 이 최솟 값이다.
            if int(str_storey[i+1]) >= 5:
                storey += (5 * digit_10)
                continue
            storey -= (5 * digit_10)
            continue
        storey -= (num * digit_10)
        answer += num
        print(storey)
    return answer