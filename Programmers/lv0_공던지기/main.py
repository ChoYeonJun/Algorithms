def solution(numbers, k):
    idx = (k * 2) - 2
    size = len(numbers)
    if idx >= size:
        idx = idx % size
    answer = numbers[idx]
    return answer