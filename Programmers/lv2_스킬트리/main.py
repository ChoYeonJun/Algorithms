def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        s = ''
        for j, c in enumerate(tree):
            if c in skill:
                s += c
                continue
        if skill[:len(s)] == s:
            answer += 1
            # print(skill_trees)

    return answer