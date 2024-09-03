T = int(input())
for tc in range(1,T+1) :
    arr = input()
    arr = list(map(int,arr))

    N = len(arr)
    clap = 0        # 현재 박수치고 있는 사람의 수
    people = 0      # 구해야하는 사람의 수

    for i in range(N) :
        need = i        # 박수치려면 필요한 사람의 수 i번째의 경우 i-1이니까 인덱스와 맞춰줌
        if arr[i] != 0 :
            if clap >= need :       # 현재 박수치고 있는 사람이 필요한 사람 수보다 많으면
                clap += arr[i]      # 박수치고 있는 사람에 추가

            # 박수치고 있는 사람이 필요한 사람보다 적을 때 (crap<need)
            else :
                people += need - clap
                clap += people + arr[i]      # 고용한 사람사람만큼 박수치는 사람에 추가, arr[i]값 추가


    print(f'#{tc} {people}')



T = int(input())

for tc in range(1,T+1):
    arr = list(map(int,input()))
    cont = 0
    man = 0

    for i in range(len(arr)):
        cont += arr[i]
        if cont <= i:
            man += 1
            cont += 1

    print(f'#{tc} {man}')