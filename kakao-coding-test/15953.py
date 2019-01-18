f = open("input.txt", "r")
n = int(f.readline())

for _ in range(n):
    a, b = map(int, f.readline().split())
    result = 0
    if a > 0:
        if a == 1:
            result += 5000000
        elif a <= 3:
            result += 3000000
        elif a <= 6:
            result += 2000000
        elif a <= 10:
            result += 500000
        elif a <= 15:
            result += 300000
        elif a <= 21:
            result += 100000
    if b > 0:
        if b == 1:
            result += 5120000
        elif b <= 3:
            result += 2560000
        elif b <= 7:
            result += 1280000
        elif b <= 15:
            result += 640000
        elif b <= 31:
            result += 320000
    print(result)

