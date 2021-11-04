from itertools import permutations

def solution(k, dungeons):
    answers = []        # 통과한 던전 갯수
    length = len(dungeons)
    arr = [i for i in range(length)]
    pe = list(permutations(arr, length))    #던전의 개수로 순열 생성

    for i in range(len(pe)):                # 순열의 각 원소별로 확인
        target = list(pe[i])
        clear = 0       # 통과한 던전 갯수
        health = k
        for level in target:
            if health < dungeons[level][0]: # 추가로 던전에 진입하지 못하는 경우
                answers.append(clear)
                break
            health -=dungeons[level][1]
            clear += 1
            if clear == length:             # 모두 클리어 한 경우
                answers.append(clear)
    

    return max(answers)



k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
case = solution(k=k, dungeons=dungeons)
print(case)     #3
