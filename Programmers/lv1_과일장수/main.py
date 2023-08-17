def solution(k, m, score):
    score = sorted(score, reverse=True)
    answer = 0
    boxes = [score[i * m:(i + 1) * m] for i in range((len(score) + m - 1) // m)]
    if len(boxes[-1]) != m:
        boxes.pop()

    for box in boxes:
        answer += (min(box) * m)
    return answer