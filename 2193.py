'''
0과 1로만 이루어진 수를 이진수라 한다. 이러한 이진수 중 특별한 성질을 갖는 것들이 있는데, 이들을 이친수(pinary number)라 한다. 이친수는 다음의 성질을 만족한다.

이친수는 0으로 시작하지 않는다.
이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.
3
2
'''
f = open("input.txt", "r")
n = int(f.readline())
'''
d = [0]*(n+1)
d[1] = 1
d[2] = 1

for i in range(3, n+1):
    d[i] = d[i-1]+d[i-2]
print(d[n])
런타임에러
'''
d = [0, 1, 1]
for i in range(3, n+1):
    d.append(d[i-1]+d[i-2])
print(d[-1]) 