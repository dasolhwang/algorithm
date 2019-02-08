def solution(darkResult):
    score = []
    i=0
    while i != len(darkResult):
        if darkResult[i] == "S":
            score[-1] *= 1
        elif darkResult[i] == "D":
            score[-1] = score[-1]*score[-1]
        elif darkResult[i] == "T":
            score[-1] = score[-1]*score[-1]*score[-1]
        elif darkResult[i] == "*":
            score[-1] *= 2
            if len(score)>=2:
                score[-2] *= 2
        elif darkResult[i] == "#":
            score[-1] *= -1
        elif darkResult[i] == "1":
            if darkResult[i+1] == "0":
                score.append(int(darkResult[i:i+2]))
                i += 1
            else:
                score.append(int(darkResult[i]))
        else:
            score.append(int(darkResult[i]))
        i += 1
    return sum(score)