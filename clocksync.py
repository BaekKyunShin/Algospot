import sys

numOfClocks = 16
numOfSwithes = 10

# switch 0부터 9까지 / index 0는 length, 1~끝까지는 switch에 연결된 시계들
linked = [
    [3, 0, 1, 2 ],
    [4, 3, 7, 9, 11],
    [4, 4, 10, 14, 15 ],
    [5, 0, 4, 5, 6, 7],
    [5, 6, 7, 8, 10, 12],
    [4, 0, 2, 14, 15],
    [3, 3, 14, 15],
    [5, 4, 5, 7, 14, 15],
    [5, 1, 2, 3, 4, 5],
    [5, 3, 4, 5, 9, 13],
]

def GetInput():
    totalInputList = []
    numTestCases = int(sys.stdin.readline())
    for _ in range(numTestCases):
        clockList = list(map(int, sys.stdin.readline().split()))
        totalInputList.append(clockList)
    return totalInputList
    

def AllAlign(currentStatus):
    for status in currentStatus:
        if status != 12: return False
    return True

# switch(0~15 int)번째 switch를 눌렀을 때의 currentStatus의 변화
def Click(currentStatus, switch):
    for i in range(1, linked[switch][0]+1):
        currentStatus[linked[switch][i]] += 3
        if currentStatus[linked[switch][i]] == 15:
            currentStatus[linked[switch][i]] = 3

# switch번째 이후로 클릭하는 모든 경우의 수 중 최소값 return
def ClockSync(currentStatus, switch):
    
    # switch가 마지막 index 라면 종료조건
    if switch == numOfSwithes - 1:
        # 모두 12시를 가르킨다면 return 0
        if AllAlign(currentStatus): 
            return 0
        else: 
            return 10000
    
    # switch를 0번 ~ 3번 누르는 경우까지 모두 고려
    count = 10000
    for i in range(4):
        # 재귀
        count = min(count, i + ClockSync(currentStatus, switch + 1))
        Click(currentStatus, switch)
    
    return count
            

if __name__ == "__main__":   
    totalInputList = GetInput()
    print("")
    for currentStatus in totalInputList:
        result = ClockSync(currentStatus, 0)
        # result가 inf면 0 출력, 그렇지 않으면 result값 출력
        if result == 10000:
            print(-1)
        else:
            print(result)