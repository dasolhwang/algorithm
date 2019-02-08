def solution(record):
    answer = []
    dic = {}
    for i in record:
        temp = i.split()
        if temp[0] == "Enter":
            answer.append([temp[1], "님이 들어왔습니다."])
            dic[temp[1]] = temp[2]
        elif temp[0] == "Leave":
            answer.append([temp[1], "님이 나갔습니다."])
        elif temp[0] == "Change":
            dic[temp[1]] = temp[2]
    result = []
    for i in range(len(answer)):
        result.append(dic[answer[i][0]] + answer[i][1])

    return result