def solution(n, words):
    history = [words[0]]
    counts = [0 for _ in range(n)]
    counts[0] += 1

    for i in range(1, len(words)):
        counts[i%n] += 1
        if words[i] in history:
            return [i%n+1, counts[i%n]]

        if words[i-1][-1] != words[i][0]:
            return [i%n+1, counts[i%n]]

        history.append(words[i])

    return [0, 0 ]
    
    # return [i%n+1, counts[i%n]]




n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
case = solution(n=n, words=words)
print(case)     # [3,3]
print()
n = 5
words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
case = solution(n=n, words=words)
print(case)     # [0,0]
print()
n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
case = solution(n=n, words=words)
print(case)     # [1,3]
