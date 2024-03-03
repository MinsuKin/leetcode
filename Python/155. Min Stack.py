class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# # My code
# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.min = []

#     def push(self, val: int) -> None:
#         if self.min == []:
#             self.min.append(val)
#         elif val < self.min[-1]:
#             self.min.append(val)
#         elif val >= self.min[-1]:
#             self.min.append(self.min[-1])
#         self.stack.append(val)

#     def pop(self) -> None:
#         if self.stack == []:
#             return None
#         else:
#             self.stack.pop()
#             self.min.pop()

#     def top(self) -> int:
#         if self.stack == []:
#             return None
#         return self.stack[-1]

#     def getMin(self) -> int:
#         if self.min == []:
#             return None
#         else:
#             return self.min[-1]



# getMin not working as O(1)
# class MinStack:

#     def __init__(self):
#         self.stack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)

#     def pop(self) -> None:
#         self.stack.pop()

#     def top(self) -> int:
#         if self.stack == []:
#             return None
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return min(self.stack)
