def solution(new_id):
    length = len(new_id)
    # [1단계] 
    # 모든 대문자는 소문자로 치환합니다.
    new_id = new_id.lower()
    
    # [2단계] 
    # 알파벳 소문자, 숫자, 빼기기호, 밑줄기호, 마침표를
    # 제외한 모든 문자를 제거합니다. 
    can_use = ['-', '_', '.']
    for i in range(length):
        if '0' <= new_id[i] and new_id[i] <='9':
            continue
        elif 'a' <= new_id[i] and new_id[i] <= 'z':
            continue
        elif new_id[i] in can_use:
            continue
        else:
            z = new_id[i]
            new_id = new_id.replace(z, " ")
            continue
    
    new_id = new_id.replace(" ", "")

    # [3단계]
    # 마침표기호 '.'는 두번 연속으로 사용할 수 없습니다.
    while True:
        if not('..' in new_id):
            break
        new_id = new_id.replace('..', '.')

    # [4단계]
    # 마침표는 id의 처음이나 끝에 위치할 수 없습니다.
    new_id = new_id.lstrip('.')
    new_id = new_id.rstrip('.')

    # [5단계]
    # id가 빈 문자열이라면, id를 'a'로 합니다.
    if new_id == "":
        new_id = 'a'
    
    # [6단계]
    # id의 길이가 16을 넘어가면 15번째 이후의 문자는 제거합니다.
    # 제거 후 마지막 문자가 마침표인 경우 마침표 문자도 제거합니다.
    if len(new_id) >=16:
        new_id = new_id[0:15]
    new_id = new_id.rstrip('.')

    # [7단계]
    # id의 길이가 2이하라면, id의 마지막 문자를
    # id의 길이가 3이 될때까지 반복합니다.
    while True:
        if len(new_id) <=2:
            new_id = new_id.__add__(new_id[-1])
        else:
            break

    answer = new_id
    return answer

x = solution("abc.....abc....defef")
print(x)