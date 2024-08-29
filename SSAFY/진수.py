num = 46

bin_str = ''
while num:
    bin_str = str(num % 2) + bin_str
    # bin_str = str(num & 1) + bin_str
    num //= 2
    # num >>= 1
print(bin_str)


num = 46
bin_str = ''
# 6자리 출력하기
# 자리수가 정해져 있으므로 앞에서 부터 읽는게 가능한다.
for i in range(5, -1, -1):  # 2^5 -> 2^0 까지 체크
    if num & (1 << i):
        bin_str += '1'
    else:
        bin_str += '0'
print(bin_str)

