def solution(strings, n):
    strings = sorted(sorted(strings), key=lambda strings : strings[n])

    return strings


case = solution(["sun", "bed", "car"], 1)
print(case)   # ["car", "bed", "sun"]

case = solution(["abce", "abcd", "cdx"], 2)
print(case)   # ["abcd", "abce", "cdx"]