# begin	| target |	                words	                   | return
# "hit"	| "cog"	 | ["hot", "dot", "dog", "lot", "log", "cog"]  |    4
# "hit"	| "cog"	 | ["hot", "dot", "dog", "lot", "log"]	       |    0
from collections import deque

words = ["hot", "dot", "dog", "lot", "log"]
def solution(begin, target, words):
    q = deque([(begin, 0)])
    visited = [False for k in range(len(words))]
    while q:
        on_prc, prc_cnt = q.popleft()
        for j, word in enumerate(words):
            cnt = 0
            for i, c in enumerate(on_prc):
                wc = word[i]
                if wc != c:
                    cnt += 1

                if cnt > 1:
                    break

            if cnt == 1:
                if word == target:
                    return prc_cnt + 1
                if not visited[j]:
                    q.append([word, prc_cnt+1])
                    visited[j] = True



    return 0

print(solution("hit", "cog", words))