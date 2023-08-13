import math

def solution(n, k):
    answer = 0
    cvt_num = ''

    # k 진수 구하기
    while n:
        cvt_num += str(n % k)
        n //= k
    cvt_num = cvt_num[::-1]

    # 0을 기준으로 수를 나눠 소수인지 확인
    subs = ''
    for i, num in enumerate(cvt_num):
        if int(num) != 0:
            subs += num
            continue
        if subs == '': continue
        sub_num = int(subs)
        subs = ''
        if primenumber(sub_num):
            answer += 1

    # 0 이후 값이 마지막 숫자에 대한 처리
    if subs != '' and primenumber(int(subs)):
        answer += 1

    return answer


# 소수 찾기
def primenumber(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):  # 2부터 x의 제곱근까지의 숫자
        if x % i == 0:  # 나눠떨어지는 숫자가 있으면 소수가 아님
            return False
    return True
