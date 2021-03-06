import sys

def GetInput():
    totalInputList = []
    numTestCases = int(sys.stdin.readline())
    for _ in range(numTestCases):
        _ = int(sys.stdin.readline())
        fenceList = tuple(map(int, sys.stdin.readline().split()))
        totalInputList.append(fenceList)
    return totalInputList

# Divide & Conquer -> 왼쪽, 오른쪽, 겹치는 가운데 중 Max 값 리턴
def MaxSquare(left, right):
    # 종료 조건
    if left == right: return fenceList[left]
    
    mid = (left + right) // 2

    # 왼쪽, 오른쪽 part중 Max Square 값
    maxArea = max(MaxSquare(left, mid), MaxSquare(mid+1, right))

    # middle partition을 중심으로 양 옆 fence에 대한 직사각형 넓이
    leftPointer, rightPointer = mid, mid+1
    height = min(fenceList[leftPointer], fenceList[rightPointer])
    midMaxArea = height * 2

    # 왼쪽, 오른쪽, 가운데 중 최대값
    maxArea = max(maxArea, midMaxArea)
    
    # left, right Pointer를 각 왼쪽, 오른쪽 중 height가 높은 쪽으로 이동하면서 maxArea 업데이트
    while left < leftPointer or rightPointer < right:
        
        if rightPointer < right and (leftPointer == left or fenceList[leftPointer-1] <= fenceList[rightPointer+1]):
            rightPointer += 1
            height = min(height, fenceList[rightPointer])
        else:
            leftPointer -= 1
            height = min(height, fenceList[leftPointer])

        
        maxArea = max(maxArea, height * (rightPointer - leftPointer + 1))
            
    return maxArea
        
if __name__ == "__main__":   
    totalInputList = GetInput()
    print("")
    for fenceList in totalInputList:
        result = MaxSquare(0, len(fenceList)-1)
        print(result)
    
