f = open("input.txt","r")

n = int(f.readline())
temp = list(map(int, f.readline().split()))

i = n-1
j = n-1

while (temp[i-1] > temp[i])&(i > 0):
    i -= 1

if i == 0:
    print(-1)
else:
    while temp[j] < temp[i-1]:
        j -= 1

    temp[j], temp[i-1] = temp[i-1], temp[j]
    temp = temp[:i] + list(reversed(temp[i:]))

    result = ''
    for i in temp:
        result += str(i)+" "
    print(result)


'''
1. A[i-1] < A[i] 를 만족하는 가장 큰 i 찾기 
2. j >= i 면서 A[j] > A[i-1] 를 만족하는 가장 큰 j 찾기
3. i-1 이랑 j swap
4. i부터 뒤로 쭉 순열 뒤집기
'''