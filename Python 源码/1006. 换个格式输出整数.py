# 1006
nums = list(input())
listNums = []
for num in nums[::-1]:
    listNums.append(int(num))
gewei = [n for n in range(1,listNums[0]+1)]
if len(listNums) == 3:
    print('B'*listNums[2], 'S'*listNums[1], end='', sep='')
elif len(listNums) == 2:
    print('S'*listNums[1], end='', sep='')    
for i in range(0,listNums[0]):
    print(gewei[i], end='')
