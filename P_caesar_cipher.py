# 카이사르 암호
# 어떤 문장의 각  알파벳을 일정한 거리만큼 밀어서
# 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 한다.
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수
# solution()을 작성하라.

def solution(s, n):
    answer = ""

    for one in s:
        if ord(one) == 32:
            answer += " "
            continue
        if 65 <= ord(one) <= 90:
            index = ord(one) + n
            if index > 90:
                index = index - 26
            answer += chr(index)
        if 97 <= ord(one) <= 122:
            index = ord(one) + n
            if index > 122:
                index = index - 26
            answer += chr(index)

    return answer





case = solution("AB", 1)
print(case)     #"BC"
case = solution("z", 1)
print(case)     #"a"
case = solution("a B z", 4)
print(case)     #"e F d"