def solution(citations):
    answer = 0
    citations.sort(reverse=True)  # 6, 5, 3, 1, 0
    size = len(citations)
    for i, h in enumerate(citations):
        if h >= i + 1:  # h번 인용된 논문의 갯수는 i + 1 이다.
            answer = i + 1

    return answer

citations = [3, 0, 6, 1, 5]
print(solution(citations))