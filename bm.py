import sys

def get_input():
    rawInput = sys.stdin.readline()
    return list(map(int, list(rawInput.strip()))) # '1011' -> [1, 0, 1, 1]

def binary_count(inputList):
    count = 0
    while len(inputList) > 0:
        lastNum = inputList[-1]
        if lastNum == 0:
            inputList.pop(-1)
        else:
            inputList[-1] = 0
        count += 1
    return count - 1

if __name__ == "__main__":   
    inputList = get_input()
    count = binary_count(inputList)
    print(count)