def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        
        binary1 = int(bin(arr1[i])[2:])
        binary2 = int(bin(arr2[i])[2:])
        sum_bin = "0" * (n - len(str(binary1+binary2)))+ str(binary1 + binary2)
        text = ""
        for one in sum_bin:
            if one == "0":
                text += " "
            else:
                text += "#"
        answer.append(text)

    return answer





n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
case = solution(n, arr1, arr2)
print(case)     # ["#####","# # #", "### #", "#  ##", "#####"]


n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
case = solution(n, arr1, arr2)
print(case)     # ["######", "### #", "## ##", " #### ", " #####", "### # "]
                # ['######', '###  #', '##  ##', '#### ', '#####', '### # ']


