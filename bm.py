"""
스트링에 2진수 숫자가 들어있다(스트링은 '0'과 '1'로만 구성됨). 주어진 숫자가 홀수면 1을 빼고, 짝수면 2로 나눈다. 주어진 숫자가 0이 될 때까지 필요한 연산(빼기 or 나누기)의 횟수를 구하시오.
e.g.) 1101 -> 6회, 0 -> 0회, 000110 -> 4회
"""

import sys

def get_input():
    rawInput = sys.stdin.readline()
    return list(map(int, list(rawInput.strip()))) # '1011' -> [1, 0, 1, 1]

def binary_count(inputList):
    count = 0
    while len(inputList) > 0:
        if not 1 in inputList: # 1이 없으면(즉, 0이면) while문 중단
            break
        lastNum = inputList[-1]
        if lastNum == 0:
            inputList.pop(-1)
        else:
            inputList[-1] = 0
        count += 1
    return count # 마지막 0까지 처리하므로 1만큼 뺌

if __name__ == "__main__":   
    inputList = get_input()
    count = binary_count(inputList)
    print(count)