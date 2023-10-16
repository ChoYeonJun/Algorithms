def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.upper()
        if city in cache:
            answer += 1
            cache.pop(cache.index(city))
            cache.append(city)
        else:
            answer += 5
            cache.append(city)
            if len(cache) > cacheSize:
                cache.pop(0)
    return answer