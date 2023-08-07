string = input()
subs = ''
max_str = ''
min_str = ''
for i, c in enumerate(string):
    subs += c
    #K 를 기준으로 나누기
    if c == 'K':
        max_str += str(int(10 ** (len(subs) - 1)) * 5)
        # K만 subs일 때 5 붙이기
        if len(subs) < 2:
            min_str += '5'
        else:
            min_str += str(int(10 ** (len(subs) - 2))) + '5'
        # min_str += '5'
        subs = ''

if subs != '':
    # 마지막 M은 1로 붙이기
    # MM : 10 대신 11
    max_str += '1' * len(subs)
    min_str += str(10 ** (len(subs) - 1)//1)

print(max_str)
print(min_str)