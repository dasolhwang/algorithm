def solution(cacheSize, cities):
    answer = 0
    cache = []

    if cacheSize == 0:
        return 5*len(cities)

    for i in cities:
        i = i.lower()
        if i in cache:
            answer += 1
            cache.remove(i)
            cache.append(i)
        else:
            if len(cache) == cacheSize:
                answer += 5
                cache.pop(0)
                cache.append(i)
            else:
                answer += 5
                cache.append(i)
    return answer