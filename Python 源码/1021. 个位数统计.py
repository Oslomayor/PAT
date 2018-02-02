# 1021
digits = list(input())
nums = []
for digit in digits:
    nums.append(int(digit))
nums.sort()
numset = set()
for num in nums:
    # 利用集合的唯一性
    if num in numset:
        pass
    else:
        numset.add(num)
        # 列表的 count 方法
        # OJ格式要求，所以写了三行 print()
        # 好像 Python 打完一个 item 会自动加空格
        print(num, end='')
        print(':', end='')
        print(nums.count(num))
        


