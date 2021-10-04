def solution(s):
    
    eng = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ""    
    target = ''

    for one in s:

        if one>='0' and one <= '9':
            answer += one
            continue
        else:
            target += one
        if target in eng:
            answer += str(eng.index(target))
            target = ""

    
    answer = int(answer)
    return answer



string = "one4seveneight"
x = solution(string)
print(x)