class MyQueue:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
             self.q.insert(0, self.q.pop())
        return self.q.pop()

    def peek(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0