# Definition for singly-linked list.

# https://ihp001.tistory.com/70?category=815852
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # 1. seperate linked list into two and generate reverseList
        fast = slow = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            
        
        #[1, 2, 1] -> fast: None, slow: 1 rev: none <- 1
        #[1, 2, 2, 1] -> rev: none <- 1 <- 2
        if fast: #len(linkedlist) is odd
            slow = slow.next
        
        # 2. Compare two linked list.
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        
        return not rev






# # My code
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         arr = []
#         p = head
        
#         while p:
#             arr.append(p.val)
#             p = p.next
            
#         for i in range(len(arr)//2):
#             if arr[i] == arr[-1-i]:
#                 continue
#             else:
#                 return False
            
#         return True





# def isPalindrome(self, head: ListNode) -> bool:
#     vals = []
#     current_node = head
#     while current_node is not None:
#         vals.append(current_node.val)
#         current_node = current_node.next
#     return vals == vals[::-1]








# import collections

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         liste = []
#         while head != None:
#             liste.append(head.val)
#             head = head.next
#         length = len(liste)
#         for i in range(0, length//2):
#             if liste[i] != liste[-1-i]:
#                 return False
#         return True

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






