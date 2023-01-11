array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
result = []

def solution(array, commands):
    for command in commands:
        start, end, seq = command
        part = array[start-1 : end]

        part = sorted(part)

        result.append(part[seq-1])

solution(array, commands)