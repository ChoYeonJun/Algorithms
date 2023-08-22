def solution(n, t, m, p):
    answer = ''
    digits = '0'
    num = 1
    while len(digits) < t * m:
        target = num
        cvt_num = ''
        while target:
            md = target % n
            if md >= 10:
                cvt_num += chr(65 + (md - 10))
            else:
                cvt_num += str(md)
            target //= n

        digits += cvt_num[::-1]
        target //= n
        num += 1

    digits = digits[:t * m]

    for i in range(p - 1, len(digits), m):
        answer += digits[i]

    # print(digits)
    return answer