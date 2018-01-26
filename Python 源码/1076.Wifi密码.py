# 1076
N = int(input())
dic = {'A':1,'B':2,'C':3,'D':4}
abcds = []
for i in range(0,N):
    abcds += input().split()
abcds = str(abcds)
i = -1
for s in abcds:
    i = i+1
    if s == 'T':
        print(dic[abcds[i-2]],end='')

