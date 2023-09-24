def solution(data, col, row_begin, row_end):
    start = row_begin - 1

    data.sort(key=lambda x: (x[col - 1], -x[0]))

    answer = 0

    for d in data[start]:
        answer += d % (start + 1)

    for i in range(row_begin, row_end):
        result = 0
        for d in data[i]:
            result += d % (i + 1)
        # print(result)
        answer = answer ^ result

    return answer