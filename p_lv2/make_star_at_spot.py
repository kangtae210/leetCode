# Ax + By + E = 0
# Cx + Dy + F = 0

# x = (BF - ED) / (AD - BC)
# y = (EC - AF) / (AD - BC)
def solve(first, second):
    A, B, E = first
    C, D, F = second
    target = A * D - B * C
    if (target == 0):
        return None
    

    check1 = ((B*F - E*D) % target == 0)
    check2 = ((E*C - A*F) % target == 0)

    if check1 & check2:
        x = (B*F - E*D) // target
        y = (E*C - A*F) // target
        return [x, y]
 

def solution(line):
    intersection = []

    # 방정식의 해 구하기
    for i in range(len(line)):
        for j in range(i, len(line)):
            s = solve(line[i], line[j])
            if s != None:
                intersection.append(s)

    
    intersection.sort(key= lambda x : x[1])
    miny = intersection[0][1]
    maxy = intersection[-1][1]
    intersection.sort(key= lambda x : x[0])
    minx = intersection[0][0]
    maxx = intersection[-1][0]
    answer = [["." for _ in range(minx, maxx+1)] for _ in range(miny, maxy+1)]

    for i in range(len(intersection)):
        x = intersection[i][0]
        y = intersection[i][1]
        answer[-y+maxy][x-minx] = "*"

    

    return ["".join(answer[i]) for i in range(len(answer))]

# line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
# case = solution(line)
# print(case)

# [
# "....*....", 
# ".........", 
# ".........", 
# "*.......*", 
# ".........", 
# ".........", 
# ".........", 
# ".........", 
# "*.......*"
# ]


line =[[0, 1, -1], [1, 0, -1], [1, 0, 1]]	
case = solution(line)
print(case)
# ["*.*"]

# line =[[1, -1, 0], [2, -1, 0]]	
# case = solution(line)
# print(case)
# # ["*"]

# line =[[1, -1, 0], [2, -1, 0], [4, -1, 0]]
# case = solution(line)
# print(case)
# # ["*"]


