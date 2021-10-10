from typing import AnyStr


def solution(s):
    arr = list(s)
    arr.sort(reverse=True)
    return "".join(arr)


case = solution("ZbcdCefg")
print(case)     #bcdefgZ