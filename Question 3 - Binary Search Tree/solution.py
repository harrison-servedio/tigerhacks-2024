class node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


    def insert(self, value):
        if value > self.value:
            if self.rightChild == None: self.rightChild = node(value)
            else: self.rightChild.insert(value)
        else:
            if self.leftChild == None: self.leftChild = node(value)
            else: self.leftChild.insert(value)

    def sumOfChildlessNodes(self):
        if self.leftChild == None and self.rightChild == None:
            return self.value
        else:
            temp = 0
            if self.leftChild != None:
                temp += self.leftChild.sumOfChildlessNodes()
            if self.rightChild != None:
                temp += self.rightChild.sumOfChildlessNodes()
            return temp



n = int(input())

root = node(int(input()))

for _ in range(n-1):
    root.insert(int(input()))

print(root.sumOfChildlessNodes())