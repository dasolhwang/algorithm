f = open("input.txt", "r")
temp = f.readline()

s = ' '+temp
D = [0]*len(s)

D[0] = 1
mod = 1000000
for i in range(1, len(s)):
    if 1 <= int(s[i]) <= 9:
        D[i] = (D[i-1] + D[i]) % mod

    if 10 <= int(s[i-1:i+1]) <= 26:
        D[i] = (D[i-2] + D[i]) % mod

print(D[len(s)-1])

'''
100퍼는 아니다
'''
