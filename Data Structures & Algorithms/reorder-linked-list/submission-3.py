# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        result = []
        cur = head
        while cur is not None:
            result.append(cur.val)
            cur = cur.next

        dummy = ListNode()
        cur = dummy
        l = 0
        r = len(result) - 1

        while l <= r:
            cur.next = ListNode(result[l])
            cur = cur.next
            l += 1
            
            if l <= r:
                cur.next = ListNode(result[r])
                cur = cur.next
                r -= 1

        cur.next = None 

        new = head
        cur = dummy.next
        while new and cur:
            new.val = cur.val
            new = new.next
            cur = cur.next
        
        return