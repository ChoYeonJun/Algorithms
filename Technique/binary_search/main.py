# input
# 10 7
# 1 3 5 7 9 11 13 15 17 19

# output
# 4

import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    while end >= start:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else: end = mid - 1
    return -1

n, m = map(int, input().split())

array = list(map(int, input().split()))
result = binary_search(array, m, 0, n- 1)

print(result + 1)