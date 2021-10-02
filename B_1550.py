numbers = { 
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,
    'F':15
    }
    
str = input()
answer = 0
i = len(str) - 1

for alpha in str:
    answer += numbers[alpha] * (16**i)
    i = i-1

print(answer)

