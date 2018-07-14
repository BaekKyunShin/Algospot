import sys

def GetInput():
    totalInputList = []
    numTestCases = int(sys.stdin.readline())
    for _ in range(numTestCases):
        numNerds = int(sys.stdin.readline())
        inputList = []
        for _ in range(numNerds):    
            inputPair = tuple(map(int, sys.stdin.readline().split()))
            inputList.append(inputPair)
        totalInputList.append(inputList)
    return totalInputList



class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        self.parent = None

class BST():
    def __init__(self):
        self.node = None
        self.numOfNodes = 0

    def Insert(self, x, y, parent = None):
        newNode = Node(x, y)
        if self.node == None:
            self.node = newNode
            self.node.left = BST()
            self.node.right = BST()
            self.node.parent = parent

        elif self.node.x < newNode.x:
            self.node.right.Insert(x, y, self)
        
        elif self.node.x > newNode.x:
            self.node.left.Insert(x, y, self)

    def Delete(self, x, y):
        if self.node != None:
            if self.node.x == x:
                if self.node.right.node == None and self.node.left.node == None:
                    self.node = None
                
                elif self.node.right.node == None:
                    if self.node.parent != None:
                        temp = self.node.left
                        self.node.left.node.parent = self.node.parent
                        self.node.parent.node.left = temp
                    else:
                        self.node.left.node.parent = None
                
                elif self.node.left.node == None:
                    if self.node.parent != None:
                        temp = self.node.right
                        self.node.right.node.parent = self.node.parent
                        self.node.parent.node.right = temp
                    else:
                        self.node.right.node.parent = None

                else:
                    replacement = self.NodeSuccessor(self.node)
                    if replacement != None:
                        self.node.x = replacement.x
                        self.node.y = replacement.y
                        self.node.right.Delete(replacement.x, replacement.y)
            
            elif x < self.node.x: 
                self.node.left.Delete(x, y)  
            elif x > self.node.x: 
                self.node.right.Delete(x, y)
    
    def GetNextNode(self, node):
        '''
        Get Next Large Node in whole BST
        '''
        if node.right.node != None:
            node = node.right.node
            while node.left.node != None:
                node = node.left.node
            return node
        while node.parent != None:
            if node.parent.node.left.node == node:
                return node.parent.node
            node = node.parent.node
        return None

    def GetPreviousNode(self, node):
        '''
        Get Next Small Node in whole BST
        '''
        if node.left.node != None:
            node = node.left.node
            while node.right.node != None:
                node = node.right.node
            return node
        while node.parent != None:
            if node.parent.node.right.node == node:
                return node.parent.node
            node = node.parent.node
        return None

    def IsDominated(self, node):
        nextLargeNode = self.GetNextNode(node)
        if nextLargeNode == None: # 오른쪽에 아무 것도 없다면 지배당하지 않음
            return False
        elif node.y > nextLargeNode.y: # 새로 추가된 node의 y값이 더 크다면 지배당하지 않음
            return False
        else: # 그렇지 않을 경우 지배당함
            return True

    def RemoveDominated(self, standardNode):
        while True:
            nextSmallNode = self.GetPreviousNode(standardNode)
            if nextSmallNode == None:
                break
            elif nextSmallNode.y > standardNode.y:
                break
            else:
                temp = standardNode
                self.Delete(nextSmallNode.x, nextSmallNode.y) 
                standardNode = temp
                self.numOfNodes -= 1

    def FindBST(self, x): # Node가 아닌 self BST를 return
        if self.node == None:
            return None
        elif self.node.x == x:
            return self
        elif self.node.x < x :
            return self.node.right.FindBST(x)
        elif self.node.x > x:
            return self.node.left.FindBST(x)
        

    def CountNerd(self, nerdList):
        countList = []
        for nerd in nerdList:
            x, y = int(nerd[0]), int(nerd[1])
            if self.node == None:
                self.Insert(x, y)
                self.numOfNodes += 1
                countList.append(self.numOfNodes)
            else:
                self.Insert(x, y)
                self.numOfNodes += 1
         
                standardBST = self.FindBST(x)
                
                if not standardBST.IsDominated(standardBST.node):
                    self.RemoveDominated(standardBST.node)
                countList.append(self.numOfNodes)
       
        return countList
        

    def NodeSuccessor(self, node):
        '''
        Find the smallest valued node in right child
        '''
        node = node.right.node
        if node != None: 
            while node.left != None:
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node 

# Usage example
if __name__ == "__main__": 
    
    totalInputList = GetInput()
    for inputList in totalInputList:
        bst = BST()
        numberOfNerdList = bst.CountNerd(inputList)
        print(sum(numberOfNerdList), end=' ')
        print('')