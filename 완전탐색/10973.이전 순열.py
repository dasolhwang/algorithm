f = open("input.txt","r")

n = int(f.readline())
temp = list(map(int, f.readline().split()))

i = n-1
j = n-1

while (temp[i-1] < temp[i])&(i > 0):
    i -= 1

if i == 0:
    print(-1)
else:
    while temp[j] > temp[i-1]:
        j -= 1

    temp[j], temp[i-1] = temp[i-1], temp[j]
    temp = temp[:i] + list(reversed(temp[i:]))

    result = ''
    for i in temp:
        result += str(i)+" "
    print(result)

