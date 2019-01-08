'''
2x1과 1x2 로
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
'''

f = open("input.txt","r")
n = int(f.readline())

def bottom_up(n):
    D = [0]*(n+1)
    for i in range(1, n+1):
        if i <= 2:
            D[i] = i
        else:
            D[i] = D[i-1] + D[i-2]
    return D[n]
print(bottom_up(n)%10007)


def top_down(n): # 런타임 에러
    if n <= 2:
        return n
    else:
        return (top_down(n-1) + top_down(n-2))
print(top_down(n)%10007)
