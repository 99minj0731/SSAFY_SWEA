'''
arr = '0000000111100000011000000111100110000110000111100111100111111001100111'

for i in range(0, len(arr), 7):
    val = 0
    for j in range(i, i + 7):
        if arr[j] == '1':
            val = val*2 + 1
        else:
            val = val*2 + 0
    print(val, end=' ')
print()
'''



arr = '1100'
val = 0
for i in range(len(arr)):  # i = 0, 1, 2, 3
    if arr[i] == '1':
        val = val*2 + 1
    else:
        val = val * 2 + 0
print(val, end=' ')



