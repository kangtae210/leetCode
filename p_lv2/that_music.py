# 시간 계산 함수
def cal_time(time1, time2):
    time1 = list(map(int, time1.split(":")))
    time2 = list(map(int, time2.split(":")))


    return (time2[0] - time1[0]) * 60 + (time2[1] - time1[1])

# str형의 음들을 list로 변환(#이 들어가는 경우를 별도로 고려)
def sound_to_list(string):
    answer = []
    for i in range(len(string)):
        if string[i] == "#":
            answer[-1] = answer[-1].lower()
        else:
            answer.append(string[i])
    return answer



def solution(m, musicinfos):
    m = sound_to_list(m)
    m = "".join(m)
    answers = []

    for i in range(len(musicinfos)):
        # 한 음악당 배열 원소 하나로 변환
        musicinfos[i] = musicinfos[i].split(",")
        # 재생시간을 계산하여 분 단위로 표시, 기존의 재생시작 - 재생끝 정보는 제거
        musicinfos[i].append(cal_time(musicinfos[i][0], musicinfos[i][1]))
        musicinfos[i] = musicinfos[i][2:5]

        # 재생시간만큼 음들을 반복
        # 'ABC'를 16분만큼 재생시 'ABC" * 5 + 'A' 와 같이 변환
        musicinfos[i][1] = sound_to_list(musicinfos[i][1])
        multiple = musicinfos[i][2] // len(musicinfos[i][1])
        plus = musicinfos[i][2] % len(musicinfos[i][1])
        musicinfos[i][1] = musicinfos[i][1] * multiple + musicinfos[i][1][:plus]
        musicinfos[i][1] = "".join(musicinfos[i][1])
        
        # 들을 음 m이 재생된 음들에 있다면 곡 제목과 재생시각을 answer 배열에 추가
        if m in musicinfos[i][1]:
            answers.append([musicinfos[i][0], musicinfos[i][2]])
            
    
    # answer 배열이 비어있다면 none을 반환
    # 그렇지 않다면 재생시각순으로 정렬해서 첫번째 곡의 제목 반환
    if len(answers) == 0:
        return  "(None)"      
    answers.sort(key= lambda x:-x[1])
    return answers[0][0]






m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
case = solution(m, musicinfos)
print(case)     # "HELLO"

print("++++++++++++++++++++++++++++++++++++")
m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
case = solution(m, musicinfos)
print(case)     # "FOO"

print("++++++++++++++++++++++++++++++++++++")
m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
case = solution(m, musicinfos)
print(case)     # "WORLD"



