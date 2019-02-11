f = open("input.txt", "r")
n = int(f.readline())
x = []

for _ in range(n):
    x.append(int(f.readline()))
x = sorted(x)

for i in x:
    print(i)

'''
gap = n // 2
while gap > 0:
    for start in range(gap):
        for target in range(start + gap, n, gap):
            val = x[target]
            i = target
            while i > start:
                if x[i - gap] > val:
                    x[i] = x[i - gap]
                else:
                    break
                i -= gap
            x[i] = val
    gap = gap // 2

for i in x:
    print(i)

# 시간초과
'''
