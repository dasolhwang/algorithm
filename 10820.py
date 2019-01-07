f = open("input.txt","r")
string = f.readlines()

# 끝을 모르는 입력 받기
big = [chr(i) for i in range(65, 91)]
small = [chr(i) for i in range(97, 123)]
numbers = [str(i) for i in range(10)]

# 소문자 대문자 숫자 공백
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

print(a,b,c,d)