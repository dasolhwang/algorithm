# 답보고 그대로 씀

global inte

def time2min(temp):
    return int(temp.split(":")[0])*60 + int(temp.split(":")[1])
def min2time(temp):
    temp = int(temp)
    return "%02d:%02d" %(temp//60, temp%60)
def crewTime(timetable):
    return [time2min(t) for t in timetable]
def shuttleTime(n,t):
    return [540+i*t for i in range(n)]

def DuplicateTime(time,inte):
    if not time in inte.keys():
        return time
    else:
        return DuplicateTime(time+0.001,inte)

def solution(n, t, m, timetable):
    answer = ""
    crew = sorted(crewTime(timetable))
    shuttle = shuttleTime(n,t)
    print(shuttle)
    conTime = set(crew+shuttle)
    for c in set(crew):
        conTime.add(c-1)
    for con in sorted(conTime, reverse=True):
        inte = {}
        for c in crew:
            inte[DuplicateTime(c,inte)] = 'crew'
        inte[DuplicateTime(con,inte)] = 'con'
        for sh in shuttle:
            inte[DuplicateTime(sh,inte)] = 'shuttle'

        waiting_line = []
        for time in sorted(inte.keys()):
            if 'crew' == inte[time]:
                waiting_line.append("crew")
            elif 'con' == inte[time]:
                waiting_line.append("con")
            elif 'shuttle' == inte[time]:
                waiting_line = waiting_line[m:]

        if not 'con' in waiting_line:
            return min2time(con)