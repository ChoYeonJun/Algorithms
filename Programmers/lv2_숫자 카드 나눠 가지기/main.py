from math import gcd


def solution(arrayA, arrayB):
    arrayA, arrayB = list(set(arrayA)), list(set(arrayB))

    gcdA = arrayA[0]
    for i in range(1, len(arrayA)):
        gcdA = gcd(gcdA, arrayA[i])

    gcdB = arrayB[0]
    for i in range(1, len(arrayB)):
        gcdB = gcd(gcdB, arrayB[i])

    for i in range(len(arrayA)):
        if arrayA[i] % gcdB == 0:
            gcdB = 0
            break

    for i in range(len(arrayB)):
        if arrayB[i] % gcdA == 0:
            gcdA = 0
            break

    if not (gcdA or gcdB):
        return 0
    return max(gcdA, gcdB)