'''
현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면,
이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다

예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고,
다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다.
예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.
'''

'''
N = 4 
M = 2
textNum = 1 2 3 4
'''
f = open("input.txt","r")
n = int(f.readline())

for _ in range(3):
    N, M = map(int, f.readline().split())
    textNum = list(map(int, f.readline().split()))
    idx = [i for i in range(N)]
    K = True
    result = 1
    if len(result):
    while K:
        while (idx[0]!= M)&(max(textNum) != textNum[0]):
            if textNum[0] < max(textNum):
                textNum.append(textNum[0])
                textNum.pop(0)
            else:
                textNum.pop(0)
                result += 1
    print(result)