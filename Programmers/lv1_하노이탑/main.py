# REF : https://mgyo.tistory.com/185

def solution(n):
    answer = []

    def hanoi(n, start, to, via):
        if n == 1:
            move(1, start, to)
        else:
            hanoi(n - 1, start, via, to)
            move(n, start, to)
            hanoi(n - 1, via, to, start)

    def move(n, start, to):
        answer.append([start, to])

    hanoi(n, 1, 3, 2)
    return answer


