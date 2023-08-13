minerals = ["diamond", "diamond", "diamond", "diamond", "iron", "diamond", "diamond", "diamond", "diamond", "stone", "diamond", "diamond", "diamond", "diamond"]
picks =[1, 3, 2]
from collections import Counter
import itertools
def solution(picks, minerals):
    answer = 0

    five_minerals = []
    for i in range(0, len(minerals), 5):
        if i + 5 > len(minerals):
            five_minerals.append(minerals[i:])
            break
        five_minerals.append(minerals[i:i + 5])

    five_minerals = sorted(five_minerals, key=lambda x : len(set(x)))
    minerals = list(itertools.chain(*five_minerals))
    # picks = [item*5 for item in picks]
    pick = -1

    for mineral in five_minerals:
        if "diamond" in mineral:
            if picks[0] != 0:
                pick = 0
                picks[0] -= 1
            elif picks[1] != 0:
                pick = 1
                picks[1] -= 1
            elif picks[2] != 0:
                pick = 2
                picks[2] -= 1
            else: break
        elif "iron" in mineral:
            if picks[1] != 0:
                pick = 1
                picks[1] -= 1
            elif picks[0] != 0:
                pick = 0
                picks[0] -= 1
            elif picks[2] != 0:
                pick = 2
                picks[2] -= 1
            else:
                break
        elif "stone" in mineral:
            if picks[2] != 0:
                pick = 2
                picks[2] -= 1
            elif picks[1] != 0:
                pick = 1
                picks[1] -= 1
            elif picks[0] != 0:
                pick = 0
                picks[0] -= 1
            else:
                break
        for m in mineral:
            if pick == 0:
                answer += 1
            elif pick == 1:
                if m == "diamond":
                    answer += 5
                else:
                    answer += 1
            elif pick == 2:
                if m == "diamond":
                    answer += 25
                elif m == "iron":
                    answer += 5
                else:
                    answer += 1
    # for mineral in minerals:
    #
    #     if picks[0] != 0:
    #         pick = 0
    #         picks[0] -= 1
    #     elif picks[1] != 0:
    #         pick = 1
    #         picks[1] -= 1
    #     elif picks[2] != 0:
    #         pick = 2
    #         picks[2] -= 1
    #     else: pick = -1
    #
    #     if pick == 0:
    #         answer += 1
    #     elif pick == 1:
    #         if mineral == "diamond":
    #             answer += 5
    #         else: answer += 1
    #     elif pick == 2:
    #         if mineral == "diamond" : answer += 25
    #         elif mineral == "iron" : answer += 5
    #         else: answer += 1
    #     else: break
    return answer

print(solution(picks, minerals))