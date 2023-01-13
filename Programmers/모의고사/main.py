answers = [1,3,2,4,2,2,2,2,2,2,2]

def solution(answers):
    loops = []
    loop1 = [1, 2, 3, 4, 5]
    loop2 = [2, 1, 2, 3, 2, 4, 2, 5]
    loop3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    loops.append(loop1)
    loops.append(loop2)
    loops.append(loop3)
    result = 0
    answer = []
    for loop in loops:
        mul_value = len(answers) // len(loop)
        mod_value = len(answers) % len(loop)

        submit = []

        for value in range(mul_value):
            submit.extend( loop)

        submit.extend(loop[:mod_value])
        count = 0
        for i in range(len(answers)):
            if submit[i] == answers[i]:
                count += 1

        if count > result:
            result = count
            answer.clear()
            answer.append(loops.index(loop)+1)
        elif count == result:
            answer.append(loops.index(loop)+1)
    return answer
print(solution(answers))