# Definition for singly-linked list.
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        liste = []
        while head != None:
            liste.append(head.val)
            head = head.next
        length = len(liste)
        for i in range(0, length//2):
            if liste[i] != liste[-1-i]:
                return False
        return True

# https://www.youtube.com/watch?v=fDOBOBYVV0A
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         q = collections.deque()

#         if not head:
#             return True
        
#         node = head
#         while node is not None:
#             q.append(node.val)
#             node = node.next

#         while len(q) > 1:
#             if q.popleft() != q.pop():
#                 return False
        
#         return True



# def isPalindrome(self, head: ListNode) -> bool:
#     vals = []
#     current_node = head
#     while current_node is not None:
#         vals.append(current_node.val)
#         current_node = current_node.next
#     return vals == vals[::-1]