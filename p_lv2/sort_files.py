def str_split(file):
    file = list(file)
    head = ""
    idx = 0
    for i in range(len(file)):
        if file[i] <'0' or file[i] > '9':
            head += file[i].lower()
            idx += 1
        else:
            break

    numbers = ""
    for i in range(idx, len(file)):
        if  "0" <= file[i] <= "9":
            numbers += file[i]
            idx += 1
        else:
            break
    
    arr = [head, int(numbers)]
    

    return arr




def solution(files):
    for i in range(len(files)):
        files[i] = [files[i]] + str_split(files[i])

    files.sort(key = lambda x:x[2])
    files.sort(key = lambda x:x[1])

    answer = []

    for i in range(len(files)):
        answer.append(files[i][0])
    
    
    return answer




files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
case = solution(files)
print(case)
# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]


files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
case = solution(files)
print(case)
# ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
