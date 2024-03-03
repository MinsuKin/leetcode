# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:     
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            
            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


        
        # lst1 = []
        # lst2 = []
        
        # while l1:
        #     lst1.insert(0, str(l1.val))
        #     l1 = l1.next
            
        # while l2:
        #     lst2.insert(0, str(l2.val))
        #     l2 = l2.next
        
        # num1 = int(''.join(lst1))
        # num2 = int(''.join(lst2))
        
        # res = num1 + num2
        # res = list(str(res))
        # res.reverse()
        
        # ret = ListNode()
        # save = ret
        
        # for i in res:
        #     save.next = ListNode()
        #     save = save.next
        #     save.val = int(i)
        
        # return ret.next