def solution(cards1, cards2, goal):
    j = 0
    k = 0
    for i, target in enumerate(goal):
        if k < len(cards1) and target == cards1[k]:
            k += 1
        elif j < len(cards2) and target == cards2[j]:
            j += 1
        else: return "No"
    return "Yes"