# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        res1 = ""
        res2 = ""
        Sum = ""
        cur1 = l1
        cur2 = l2
        while cur1 and cur2:
            res1 = str(cur1.val) + res1 
            res2 = str(cur2.val) + res2
            cur1 = cur1.next
            cur2 = cur2.next

        while cur1:
            res1 = str(cur1.val) + res1
            cur1 = cur1.next
        while cur2:
            res2 = str(cur2.val) + res2
            cur2 = cur2.next
        dummy = ListNode()
        tail = dummy
        Sum += str(int(res1) + int(res2))
    

        for i in range(len(Sum)-1,-1,-1):
            tail.next = ListNode(int(Sum[i]))
            tail = tail.next

        return dummy.next
        