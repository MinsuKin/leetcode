# using list
class MyStack:

    def __init__(self):
        self.stack = list()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        for i in range(len(self.stack) - 1):
            self.stack.append(self.stack.pop(0))
        return self.stack.pop(0)

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0

# # using deque
# class MyStack:

#     def __init__(self):
#         self.stack = deque()

#     def push(self, x: int) -> None:
#         self.stack.append(x)

#     def pop(self) -> int:
#         for i in range(len(self.stack) - 1):
#             self.stack.append(self.stack.popleft())
#         return self.stack.popleft()

#     def top(self) -> int:
#         return self.stack[-1]

#     def empty(self) -> bool:
#         return len(self.stack) == 0