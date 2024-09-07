import sys
sys.stdin = open('input.txt', 'r')

def find_min(s, e):
    if s == e: #만약 시작 숫자와 끝 숫자가 같다면
        return s #시작 인덱스를 리턴하겠다.
    else:
        mid = (s + e) // 2
        left_idx = find_min(s, mid) #왼쪽 그룹
        right_idx = find_min(mid + 1, e) #오른쪽 그룹
        # 왼쪽 그룹이 이길경우
        if (arr[left_idx] == 1 and arr[right_idx] == 3) or (arr[left_idx] == 2 and arr[right_idx] == 1) or (arr[left_idx] == 3 and arr[right_idx] ==2) or (arr[left_idx] == arr[right_idx]):
            return left_idx
        else:
            return right_idx

T = int(input())  #3

for test_case in range(1, T+1):
    N = int(input())  #4 인원 수 및 카드 장수
    arr = list(map(int, input().split()))  #[1, 3, 2, 1]

    result = find_min(0, len(arr) - 1)
    print(f'#{test_case} {result + 1}')


