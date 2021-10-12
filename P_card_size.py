def solution(sizes):
    width = []
    height = []

    for i in range(len(sizes)):
        sizes[i].sort()
        width.append(sizes[i][1])
        height.append(sizes[i][0])


    return max(width) * max(height)





sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
case = solution(sizes)
print(case)     #4000


sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
case = solution(sizes)
print(case)     #120


sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
case = solution(sizes)
print(case)     #133

