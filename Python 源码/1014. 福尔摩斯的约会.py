# 1014
# 这题目真的是骚，各种字符处理的要求
# 3个测试点正确，1个错误，2个返回非零
s1 = input()
s2 = input()
l1 = input()
l2 = input()
minute = -1
week_hour = []
weeks = {'A':'MON', 'B':'TUE', 'C':'WED', 'D':'THU', 'E':'FRI',\
         'F':'SAT', 'G':'SUN'}
hours = {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', \
         '6':'6', '7':'7', '8':'8', '9':'9', 'A':'10', 'B':'11', \
         'C':'12', 'D':'13', 'E':'14', 'F':'15', 'G':'16', 'H':'17',\
         'I':'18', 'J':'19', 'K':'20', 'L':'21', 'M':'22', 'N':'23'}
for t1,t2 in zip(s1, s2):
    if t1 == t2:
        week_hour.append(t1)
    # 过滤第一对相同字母前的相同数字
    if len(week_hour) != 0 and week_hour[0] not in weeks.keys():
        week_hour.remove(week_hour[0])
week = weeks.get(week_hour[0])
hour = hours.get(week_hour[1])
for t1,t2 in zip(l1, l2):
    minute += 1
    if t1 == t2 and t1.isalpha():
        break
if minute < 10:
    minute = '0'+str(minute)
else:
    minute = str(minute)
print(week + ' ' + hour + ':' + minute, end='')
    
