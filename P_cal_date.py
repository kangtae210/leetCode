#2016년 1월 1일은 금요일

def solution(month, day):
    month_arr = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum_date = sum(month_arr[0:month]) + day + 4
    return ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"][sum_date % 7]


case = solution(1,1)
print(case)     #TUE