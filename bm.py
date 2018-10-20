"""
스트링에 2진수 숫자가 들어있다(스트링은 '0'과 '1'로만 구성됨). 주어진 숫자가 홀수면 1을 빼고, 짝수면 2로 나눈다. 주어진 숫자가 0이 될 때까지 필요한 연산(빼기 or 나누기)의 횟수를 구하시오.
e.g.) 1101 -> 6회, 0 -> 0회, 000110 -> 4회
"""

import sys

def get_input():
    rawInput = sys.stdin.readline()
    return list(map(int, list(rawInput.strip()))) # '1011' -> [1, 0, 1, 1]

def get_one_index(inputList):
    ''' inputList에서 왼쪽부터 시작해 처음 1이 나오는 element의 index return'''
    firstOneIndex = 0
    for index in range(len(inputList)):
        if inputList[index] == 1:
            firstOneIndex = index
            break
    return firstOneIndex

def binary_count(inputList):
    firstOneIndex = get_one_index(inputList)
    if firstOneIndex == 0 and inputList[0] == 0: return 0 # input이 0인 경우
    count = 0
    while len(inputList) > 0:
        lastNum = inputList[-1]
        if lastNum == 0:
            inputList.pop(-1)
        else:
            inputList[-1] = 0
        count += 1
        if firstOneIndex == len(inputList)-1 and inputList[-1] == 0: # firstOneIndex에 해당하는 element가 0일때 while문 break
            break
    return count

if __name__ == "__main__":   
    inputList = get_input()
    count = binary_count(inputList)
    print(count)