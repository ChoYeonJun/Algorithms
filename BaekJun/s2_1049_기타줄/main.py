n, m = map(int, input().split())
l = []
six_l = []
even_price = 1e9

for i in range(m):
    a, b = map(int, input().split())
    l.append([a, b])
    # 낱개 최저가
    even_price = min(b, even_price)

    # 6개 이하라면 패키지 가격과 낱개 x n 가격을 비교할 수 있도록
    if n < 6:
        six_l.append(a)
        six_l.append(n*b)
        continue

    six_l.append(a)
    six_l.append(6*b)

# 패키지 최저가
package_price = min(six_l)
if n < 6:
    print(package_price)
else:
    package = n//6
    indi = n%6
    # 낱개로 나머지를 사는게 좋은지, 패키지로 전부 사는게 좋은지 확인
    print(min(package_price*package + indi*even_price, (package + 1) * package_price))

