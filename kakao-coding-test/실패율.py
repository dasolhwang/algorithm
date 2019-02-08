def solution(N, stages):
    answer = [None] * N
    k = len(stages)
    stages = sorted(stages)
    result = [0] * (N + 1)

    for i in set(stages):
        for j in stages:
            if i == j:
                result[i - 1] += 1

    for i in range(len(result) - 1):
        h = k - sum(result[:i])
        if h == 0:
            h = 1
        answer[i] = result[i] / h

    temp = tuple(zip(range(1, N + 1), answer))
    temp = sorted(temp, key=lambda x: x[1], reverse=True)
    idx = []
    for i in temp:
        idx.append(i[0])
    return idx