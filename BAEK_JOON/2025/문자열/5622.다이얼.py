import sys
sys.stdin = open('input.txt')

word = list(map(str,input()))

time = 0

dial = {
    "ABC": 3,
    "DEF": 4,
    "GHI": 5,
    "JKL": 6,
    "MNO": 7,
    "PQRS": 8,
    "TUV": 9,
    "WXYZ": 10
}

for i in word:
    for j in dial:
        if i in j :
            time += dial[j]

print(time)
