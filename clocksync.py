import sys

numOfClocks = 16
NewNumOfSwithes = 8 # 4번, 9번 스위치는 제거했으므로
error = 0 # Error Test 함수를 위한 전역변수

# switch 0부터 9까지 switch에 연결된 시계들
linked = [
    [0, 1, 2 ],
    [3, 7, 9, 11],
    [4, 10, 14, 15 ],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13],
]


# switch 4번과 9번을 제외하고 연결된 시계들
newLinked = [
    [0, 1, 2 ],
    [3, 7, 9, 11],
    [4, 10, 14, 15 ],
    [0, 4, 5, 6, 7],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
]

def GetInput():
    totalInputList = []
    numTestCases = int(sys.stdin.readline())
    for _ in range(numTestCases):
        clockList = list(map(int, sys.stdin.readline().split()))
        totalInputList.append(clockList)
    return totalInputList
    
# 모든 시계가 12시에 정렬되었는지 판단
def AllAlign(currentStatus):
    for status in currentStatus:
        if status != 12: return False
    return True

# switch(0~15 int)번째 switch를 눌렀을 때의 currentStatus의 변화
def Click(currentStatus, switch):
    for i in range(0, len(linked[switch])):
        currentStatus[linked[switch][i]] += 3
        if currentStatus[linked[switch][i]] == 15:
            currentStatus[linked[switch][i]] = 3

# switch(0~15 int, 4/9번은 제외)번째 switch를 눌렀을 때의 currentStatus의 변화
def NewClick(currentStatus, switch):
    for i in range(0, len(newLinked[switch])):
        currentStatus[newLinked[switch][i]] += 3
        if currentStatus[newLinked[switch][i]] == 15:
            currentStatus[newLinked[switch][i]] = 3

# 8번과 12번 시계는 4번 스위치하고만 연결되어 있으므로 8번 12번 시계가 가르키는 방향이 다르다면 error임
def ErrorTest(currentStatus):
    if currentStatus[8] != currentStatus[12]:
        global error
        error = 1


# 8번, 13번 시계는 각 4번, 9번 스위치에 의해서만 조작되므로 initial control해줌
# 8, 13번 시계의 현재 Status를 기반으로 4, 9번 스위치를 클릭할 횟수를 구하고 4,9번 스위치를 아예 없애줌
def InitialControl(currentStatus):
    count = 0
    if currentStatus[8] == 3:
        for _ in range(3): Click(currentStatus, 4)
        count += 3
    elif currentStatus[8] == 6:
        for _ in range(2): Click(currentStatus, 4)
        count += 2
    elif currentStatus[8] == 9:
        Click(currentStatus, 4)
        count += 1
    
    if currentStatus[13] == 3:
        for _ in range(3): Click(currentStatus, 9)
        count += 3
    elif currentStatus[13] == 6:
        for _ in range(2): Click(currentStatus, 9)
        count += 2
    elif currentStatus[13] == 9:
        Click(currentStatus, 9)
        count += 1
    return count


# switch번째 이후로 클릭하는 모든 경우의 수 중 최소값 return
def ClockSync(currentStatus, switch):
    
    # switch가 마지막 index 라면 종료조건
    if switch == NewNumOfSwithes:
        # 모두 12시를 가르킨다면 return 0
        if AllAlign(currentStatus): 
            return 0
        else: 
            return 1000000
    
    # switch를 0번 ~ 3번 누르는 경우까지 모두 고려
    count = 1000000
    for i in range(4):
        # 재귀
        count = min(count, i + ClockSync(currentStatus, switch + 1))
        NewClick(currentStatus, switch)
    return count
            
if __name__ == "__main__":   
    totalInputList = GetInput()
    print("")
    for currentStatus in totalInputList:
        currentStatus = currentStatus
        ErrorTest(currentStatus)
        result = InitialControl(currentStatus)
        result += ClockSync(currentStatus, 0)
        # result가 inf이거나 error가 1이면 -1 출력, 그렇지 않으면 result값 출력
        if error == 1 or result >= 1000000:
            print(-1)
        else:
            print(result)
        error = 0 # 전역변수 error 초기화