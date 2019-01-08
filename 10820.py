big = [chr(i) for i in range(65, 91)]
small = [chr(i) for i in range(97, 123)]
numbers = [str(i) for i in range(10)]

while True:
    try:
        string = input()
    except EOFError:
        break
    a= 0; b= 0; c= 0; d = 0
    for j in range(len(string)):
        for i in string[j]:
            if i in small:
                a += 1
            elif i in big:
                b += 1
            elif i in numbers:
                c += 1
            else:
                d += 1
    print(a,b,c,d)

'''
끝을 모르는 입력 받기
while True:
    try:
        string = input()
    except EOFError:
        break
'''