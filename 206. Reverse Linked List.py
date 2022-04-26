# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# # my code
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         list = []
#         tmp = head
#         res = head
#         while head != None:
#             list.insert(0, head.val)
#             head = head.next
#         i = 0
#         while tmp != None:
#             tmp.val = list[i]
#             i += 1
#             tmp = tmp.next
#         return res

# neetcode
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

# # neetcode - recursive
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         if not head:
#             return None
        
#         newHead = head
        
#         if head.next:
#             newHead = self.reverseList(head.next)
#             head.next.next = head
#         head.next = None

#         return newHead

# # recursive
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         return self.recurse(None, head)
    
#     def recurse(self, prev: Optional[ListNode], cur: Optional[ListNode]) -> Optional[ListNode]:
        
#         if cur == None:
#             return prev
        
#         # save new next node
#         newNext = cur.next      
        
#         # reverse
#         cur.next = prev
        
#         # reverse reset of the list
#         return self.recurse(cur, newNext)