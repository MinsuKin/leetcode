class MyCircularDeque:

    def __init__(self, k: int):
        self.dq = [k]
    
    def insertFront(self, value: int) -> bool:
        if len(self.dq) == self.dq[0] + 1:
            return False
        self.dq.insert(1, value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.dq) == self.dq[0] + 1:
            return False
        self.dq.append(value)
        return True

    def deleteFront(self) -> bool:
        if len(self.dq) == 1:
            return False
        self.dq.pop(1)
        return True

    def deleteLast(self) -> bool:
        if len(self.dq) == 1:
            return False
        self.dq.pop()
        return True

    def getFront(self) -> int:
        if len(self.dq) == 1:
            return -1
        return self.dq[1]

    def getRear(self) -> int:
        if len(self.dq) == 1:
            return -1
        return self.dq[-1]
        
    def isEmpty(self) -> bool:
        if len(self.dq) == 1:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if len(self.dq) == self.dq[0] + 1:
            return True
        else:
            return False