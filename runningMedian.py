import sys

def GetInput():
    totalInputList = []
    numTestCases = int(sys.stdin.readline())
    for _ in range(numTestCases):
        case = tuple(map(int, sys.stdin.readline().split()))
        totalInputList.append(case)
    return totalInputList

def Median(sequenceList):
    if len(sequenceList) == 1:
        return sequenceList[0]
    else:
        if len(sequenceList) % 2 == 0:
            medianIndex = len(sequenceList) // 2 - 1
        else:
            medianIndex = len(sequenceList) // 2 
        return sequenceList[medianIndex]


def RunningMedian(length, a, b):
    sequenceList = []
    sortedsequenceList = []
    medianList = []
    for i in range(length):
        if i == 0:
            sequenceList.append(1983)
            sortedsequenceList.append(1983)
        else:
            element = (sequenceList[i-1]*a + b) % 20090711
            sequenceList.append(element)
            sortedsequenceList.append(element)
        sortedsequenceList.sort()
        medianList.append(Median(sortedsequenceList))
    return sum(medianList) % 20090711


if __name__ == "__main__":
    totalInputList = GetInput()
    for inputList in totalInputList:
        print(RunningMedian(inputList[0], inputList[1], inputList[2]))

