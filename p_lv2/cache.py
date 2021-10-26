def solution(cacheSize, cities):
    cache_arr = []
    answer = 0
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
        try:
            cache_arr.remove(cities[i])
            answer += 1
        except:
            answer += 5

        cache_arr.append(cities[i])
        if len(cache_arr) == cacheSize + 1:
            cache_arr = cache_arr[1:]
    return answer





cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
case = solution(cacheSize, cities)  # 50 
print(case)

cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
case = solution(cacheSize, cities)  # 21
print(case)

cacheSize = 2
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
case = solution(cacheSize, cities)  # 60
print(case)

cacheSize = 5
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
case = solution(cacheSize, cities)  # 52
print(case)

cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
case = solution(cacheSize, cities)  # 16
print(case)

cacheSize = 0
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
case = solution(cacheSize, cities)  # 25
print(case)

