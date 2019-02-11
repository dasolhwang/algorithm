import math

f = open("input.txt", "r")
n = int(f.readline())

def next_permutation(n, temp):
    i = n - 1
    j = n - 1
    while (temp[i - 1] > temp[i]) & (i > 0):
        i -= 1

    if i == 0:
        return False
    else:
        while temp[j] < temp[i - 1]:
            j -= 1

        temp[j], temp[i - 1] = temp[i - 1], temp[j]
        temp = temp[:i] + list(reversed(temp[i:]))
    return temp

for i in range(math.factorial(n)):
    if i == 0:
        temp = [i + 1 for i in range(n)]
    else:
        temp = next_permutation(len(temp), temp)
    result = ''
    for i in temp:
        result += str(i)+" "
    print(result)

