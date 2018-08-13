import sys

def GetInput():
    stringList =[]
    numTestCases = int(sys.stdin.readline())
    for _ in range(numTestCases):
        stringList.append(sys.stdin.readline().strip())
    return stringList

# string을 4등분해서 총 4개의 index를 return
def find_quad_index(string):
    count = 0
    pointer = 1 # 첫 단어 'x' 이후부터 시작하므로
    indexList = [0, 0, 0, 0]
    if string[0] == 'x':
        for index in range(4):
            if string[pointer] == 'b' or string[pointer] == 'w':
                indexList[index] = pointer
                pointer += 1
            elif string[pointer] == 'x':
                indexList[index] = pointer
                count += 1
                pointer += 1
                while count <= 4:
                    if string[pointer] == 'b' or string[pointer] == 'w':
                        count += 1
                        pointer += 1
                    elif string[pointer] == 'x':
                        count -= 3 # x를 만나면 count -= 3을 해줘서 4칸을 더 가도록 함
                        pointer += 1
                count = 0
    return indexList[0], indexList[1], indexList[2], indexList[3]

def flip_quadtree(string):
    if string == 'b': 
        return 'b'
    elif string == 'w':
        return 'w'
    else:
        if string[0] == 'x':
            firstIndex, secondIndex, thirdIndex, fourthIndex = find_quad_index(string)
            return 'x' + flip_quadtree(string[thirdIndex:fourthIndex]) + flip_quadtree(string[fourthIndex:]) + flip_quadtree(string[firstIndex:secondIndex]) + flip_quadtree(string[secondIndex:thirdIndex])


if __name__ == "__main__":
    stringList = GetInput()
    for string in stringList:
        print(flip_quadtree(string), end='\n')