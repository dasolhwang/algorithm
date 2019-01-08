'''
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
'''


f = open("input.txt", "r")
n = int(f.readline())

# Bottom-Up
d = [0]*(n+1)
for i in range(2,n+1):
    if i % 3 == 0:
        if (d[int(i/3)] < d[i-1]) & (d[i] == 0):
            d[i] = 1 + d[int(i/3)]
        else:
            d[i] = 1 + d[i-1]
    elif i % 2 == 0:
        if (d[int(i/2)] < d[i-1]) & (d[i] == 0):
            d[i] = 1 + d[int(i/2)]
        else:
            d[i] = 1 + d[i-1]
    else:
        if d[i] == 0:
            d[i] = 1 + d[i-1]
print(d[n])

# Top-Down 시간초과
def d(n):
    if n == 2 | n == 3:
        return 1
    else:
        if n%3 == 0:
            if d(n/3) < d(n-1):
                result = 1 + d(n/3)
            else:
                result = 1 + d(n-1)
        elif n%2 == 0:
            if d(n/2) < d(n-1):
                result = 1 + d(n/2)
            else:
                result = 1 + d(n-1)
        else:
            result = 1 + d(n-1)
    return result

print(d(n))
'''
