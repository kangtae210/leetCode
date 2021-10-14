def solution(participant, completion):
    participant.sort()
    completion.sort()

    
    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]
    
    return participant[-1]


		
		

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
case = solution(participant, completion)
print(case)     # "leo"

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
case = solution(participant, completion)
print(case)     # "vinko"

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
case = solution(participant, completion)
print(case)     # "mislav"

