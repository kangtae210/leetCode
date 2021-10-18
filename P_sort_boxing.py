# weight => 복서 선수들의 몸무게
# head2head => 복서 선수들의 전적
# N => 아직 붙어본 적 없음
# W => i+1번 복서가 j+1번 복서를 이겼음
# L => i+1번 복서가 j+1번 복서에게 졌음
# 전체 승률이 높은 복서의 번호가 앞쪽으로 갑니다. 아직 다른 복서랑 붙어본 적이 없는 복서의 승률은 0%로 취급합니다.
# 승률이 동일한 복서의 번호들 중에서는 자신보다 몸무게가 무거운 복서를 이긴 횟수가 많은 복서의 번호가 앞쪽으로 갑니다.
# 자신보다 무거운 복서를 이긴 횟수까지 동일한 복서의 번호들 중에서는 자기 몸무게가 무거운 복서의 번호가 앞쪽으로 갑니다.
# 자기 몸무게까지 동일한 복서의 번호들 중에서는 작은 번호가 앞쪽으로 갑니다.

def solution(weights, head2head):
    people = len(weights)
    peoples = []
    answer = []    # return value

    # 1. 자료 정리
    for i in range(people):
        target = []
        
        win = head2head[i].count('W')
        fight = win + head2head[i].count('L')
        if fight == 0:
            fight = 1
        target.append(win/fight)    # 승률
        target.append(0)            # 무거운 선수를 이긴 횟수 초기화

        for j in range(people):
            if head2head[i][j] == 'W':
                if weights[i] < weights[j]:
                    target[-1] += 1

        target.append(weights[i])   # 몸무게

        target.append(i+1)          # 선수번호
        peoples.append(target)
    
    # 2. 정렬
    peoples.sort(key= lambda x : -x[2])
    peoples.sort(key= lambda x : -x[1])
    peoples.sort(key= lambda x : -x[0])

    for i in range(people):
        answer.append(peoples[i][3])
    
    return answer





case = solution([50,82,75,120],["NLWL","WNLL","LWNW","WWLN"])
print(case)                     #[3,4,1,2]

case = solution([145,92,86],	["NLW","WNL","LWN"])
print(case)                     #[2,3,1]

case = solution([60,70,60],	["NNN","NNN","NNN"])
print(case)                     #[2,1,3]

