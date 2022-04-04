# Definition for singly-linked list.
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


# def check_big_o_n(self, head):
#         # time complexity = O(n), Space Complexity = O(1)
#         # First, we get the middle element accordingly
#         mid,even = self.getMid(head)
#         second = mid.next
#         # if, its even then ignoring the middle value
#         if not even: second = second.next
#         # Reversing the first half of the list
#         first = self.reverse(head, mid)
#         while first and second:
#             if first.val != second.val: return False
#             first = first.next
#             second = second.next
#         return True
        
        
#     def reverse(self, head, upto):
#         prev = next = None
#         # print("In rev", head.val)
#         curr = head
#         while curr and prev != upto:
#             # print("in rev", curr.val)
#             next = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next
#         return prev
        
#     def getMid(self, head):
#         slow = head
#         fast = head.next
#         prev = head
#         while fast and fast.next:
#             prev = slow
#             slow = slow.next
#             fast = fast.next.next
#         # print(slow, fast, prev)
#         if not fast: return prev,False
#         return slow,True