# 유저가 배우려는 순서 user가 선후행 규칙 rule을 만족하면 True 반환
def check(rule, user):
    target = []
    # 각 스킬마다 탐색
    for i in range(len(rule)):
        try:        # 스킬트리에 에서 찾아서 배열에 추가
            target.append(user.index(rule[i]))
        except:
            continue

    target.sort()   # 스킬트리의 순서대로 들어있는지 확인하기 위해 sort
    string = ""
    for i in target:
        string += user[i]  
    
    # 스킬트리에 스킬이 있는지 확인(일부만 있어도 순서대로 있으면 True 반환)
    return rule[:len(string)] == string

def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        if check(skill, skill_trees[i]):
            answer += 1
            
    return answer




skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
case = solution(skill, skill_trees)
print(case)     # 2