# input을 받아 List로 저장
def GetInput():
    inputList = []
    numTestCases = int(input())
    for _ in range(numTestCases):
        inputPair = (int(input()), map(int, input().split()))
        inputList.append(inputPair)
    return inputList

def InverseInsertion(numElements, elementsList):
    originalList = list(range(numElements)) # 0 ~ n 까지 List 세팅
    indexCounter = 0
    for i in elementsList:
        if i > 0:
            originalList[indexCounter-i:indexCounter-i] = [originalList.pop(indexCounter)] # 삽입정렬 알고리즘대로 자신의 자리 찾아가기
        indexCounter += 1
    resultList = [0] * numElements # defalut List 세팅
    counter = 1
    for i in originalList:
        resultList[i] = counter
        counter += 1
    return resultList

if __name__ == "__main__":
    inputList = GetInput()
    for numElements, elementsList in inputList:
        resultList = InverseInsertion(numElements, elementsList)
        for i in resultList:
            print(i, end = ' ')
        print('\n')