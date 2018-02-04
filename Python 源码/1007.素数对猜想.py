import math

# 经测试发现还是不用集合快
# 提示部分答案错误
setPrime = {2}

def isPrime(n):
    if n in setPrime:
        return True
    if n < 2:
        return False
    if n == 2:
        setPrime.add(n)
        return True
    for i in setPrime:
        if n%i == 0:
            return False
    else:
        setPrime.add(n)
        return True

def main():
    N = int(input())
    count = 0
    for i in range(3, N+1, 2):
        if isPrime(i):
            if(isPrime(i+2)):
               count += 1
    else:
        print(count)

if __name__ == '__main__':
    main()
