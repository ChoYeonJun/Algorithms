def solution(survey, choices):
    mbti = [['r', 't'], ['c', 'f'], ['j', 'm'], ['a', 'n']]

    score_dict = {}

    for types in mbti:
        a, b = types
        score_dict[a.upper()] = 0
        score_dict[b.upper()] = 0

    for i in range(len(survey)):
        types = survey[i]
        choice = choices[i]
        score = choice % 4
        if choice > 4:
            score_dict[types[1]] += score
        elif choice < 4:
            score_dict[types[0]] += (4 - score)
    answer = ''
    print(score_dict)
    for types in mbti:
        a, b = types
        a = a.upper()
        b = b.upper()
        if score_dict[a] >= score_dict[b]:
            answer += a
        else:
            answer += b

    return answer