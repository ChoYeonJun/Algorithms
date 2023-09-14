def solution(sequence, k):
    answer = [0, 1e9]
    start = 0
    end = 0
    total = sequence[0]
    sequence += [0]

    while end < len(sequence) - 1:
        if total <= k:
            if total == k and answer[-1] - answer[0] > end - start:
                answer = [start, end]
            end += 1
            total += sequence[end]
        else:
            total -= sequence[start]
            start += 1

    return answer