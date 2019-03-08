
f = open("input.txt", "r")
'''
서로 다른 L개의 알파벳 소문자들로 구성되며 최소 1개의 모음과 최소 2개의 자음
증가하는 순서로 배열
'''
L, C = map(int, f.readline().split())
temp = sorted(list(f.readline().split()))
condition = ['a','e','i','o','u']

def backTracking(start, str, ja, mo):
    if len(str) == L:
        if (mo >= 1) & (ja >=2):
            print(str)

    for i in range(start, C):
        if temp[i] in condition:
            backTracking(i+1, str+temp[i], ja, mo+1)
        else:
            backTracking(i+1, str+temp[i],ja+1, mo)

backTracking(0,"",0,0)


'''
def Backtracking(tmp,a,b):

    for i in tmp:
        if i in condition: # 모음
            a += 1
        else:
            b += 1
    if (a>=1)&(b>=2):
        result=''
        for i in tmp:
            result+=i
        print(result+' ')

for tmp in list(itertools.combinations(temp, 4)):
    Backtracking(tmp,0,0)
'''


