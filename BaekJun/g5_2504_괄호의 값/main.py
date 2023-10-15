s = input()

dict_c = {'(' : 0, '[' : 0}

if len(s) % 2 != 0:
    print(0)
    exit(0)
if s[0] == ']' or s[0] == ')':
    print(0)
    exit(0)

dict_c[s[0]] += 1
# print(dict_c['('])
for i, c in enumerate(s):
    if i == 0:
        continue
    if (c == ')' and (s[i-1] == '[' or dict_c['('] == 0)) or (c == ']' and (s[i - 1] == '(' or dict_c['['] == 0)):
        print(0)
        exit(0)
    if c == '(' or c == '[':
        dict_c[c] += 1
    elif c == ')':
        dict_c['('] -= 1
    elif c == ']':
        dict_c['['] -= 1

answer = 0
offset = 1
close = False
for c in s:
    if c == '(':
        close = False
        offset *= 2
    elif c == '[':
        close = False
        offset *= 3
    elif c == ')':
        if not close:
            answer += offset
        close = True
        offset //= 2
    else:
        if not close:
            answer += offset
        close = True
        offset //= 3
print(answer)