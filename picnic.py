import sys

def GetInput():
    totalInputList = []
    numOfPeopleList = []
    numTestCases = int(sys.stdin.readline())
    for _ in range(numTestCases):
        friends = []
        number = tuple(map(int, sys.stdin.readline().split()))
        numOfPeopleList.append(number[0])
        temp = tuple(map(int, sys.stdin.readline().split()))
        for i in range(len(temp)): # friends pair 만들어서 sort 후 list로 append
            if i % 2 == 0:
                tempList = [temp[i], temp[i+1]]
                tempList.sort()
                friends.append(tempList)
        totalInputList.append(friends)
    return numOfPeopleList, totalInputList

def AreFriends(i, j, friends):
    '''
    i번째 학생과 j번째 학생이 서로 친구인지 판단
    '''
    return ([i, j] or [j, i]) in friends # 순서가 반대인 경우도 하나의 case로 카운트하므로

def CountPairings(taken, friends):
    firstFree = -1
    for i in range(numOfPeople):
        if not taken[i]:
            firstFree = i
            break
    if firstFree == -1: return 1 # 모든 학생이 짝을 찾았으면 한 가지 방법을 찾았으니 종료한다.
    ret = 0
    for pairWith in range(firstFree + 1, numOfPeople):
        if (not taken[pairWith]) and AreFriends(firstFree, pairWith, friends):
            taken[firstFree] = True
            taken[pairWith] = True
            ret += CountPairings(taken, friends)
            taken[firstFree] = False
            taken[pairWith] = False
    return ret
    

if __name__ == "__main__":   
    numOfPeopleList, totalInputList = GetInput()
    print("")
    for i in range(len(totalInputList)):
        numOfPeople = numOfPeopleList[i]
        numOfFriends = len(totalInputList[i])
        taken = [False] * numOfPeople
        print(CountPairings(taken, totalInputList[i]), end='\n')
