def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(arr1[i]|arr2[i])
    answer = [bin(i) for i in answer]
    result = []
    for i in answer:
        str = " "*n
        for j in i[2:]:
            if j == "1":
                str += "#"
            elif j == "0":
                str += " "
        if len(str) > n:
            result.append(str[len(str)-n:])
        else:
            result.append(str)
    return result