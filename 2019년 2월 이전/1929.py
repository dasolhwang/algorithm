'''
 M 이상 N 이하의 소수를 모두 출력하는 프로그램을 작성하시오.
'''

# 2. 에라토스테네스
M = int(input()); N = int(input())
def isPrime(num):
    if num == 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
            break
        i += 1
    return True


for i in range(M, N + 1):
    if isPrime(i):
        print(i)


'''
# 1. 기본적인 접근 방법 (시간초과)
M, N = map(int, input().split())
for i in range(M, N+1):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime == True:
        print(i)
'''

