class ListNode:
        def __init__(self, val:int = 0, next: ListNode = None):
            self.val = val
            self.next = next

class Solution:
    # two reversed-order linked lists
    # have to sum them tgt
    # the problem says there is no empty cases, so don't have to handle the edge cases for the start
        
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        carried_digit = 0
        inter = ListNode()
        dummy = ListNode(0, inter)
        # edge case for the start
        while l1.next is not None and l2.next is not None:
            inter.val = (l1.val + l2.val + carried_digit) % 10 
            carried_digit = (l1.val + l2.val + carried_digit)//10
            l1, l2 = l1.next, l2.next
            inter.next = ListNode()
            inter = inter.next
        # edge case, as the loop breaks before iterating through the last values of the given list nodes
        inter.val = (l1.val + l2.val + carried_digit) % 10
        carried_digit = (l1.val + l2.val + carried_digit)//10
        # case where one list has more elements than the other
        if l1.next is not None or l2.next is not None: inter.next = l1.next if l1.next else l2.next
        # case when the carried_digit is greater than 1. Then, you can only terminate when the carried digit is equal to zero
        while carried_digit != 0:
            if inter.next is None: inter.next = ListNode()
            inter = inter.next
            carried_digit = (inter.val + 1) // 10
            inter.val = (inter.val + 1) % 10
        return dummy.next
        
             
            
