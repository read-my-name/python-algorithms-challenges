from typing import Optional
from linkedlist import ListNode  # Importing ListNode from a custom module named 'linkedlist'

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        carry = 0
        res_dummy = ListNode(-1)
        res_prev = res_dummy

        while p1 or p2:
            if not p1:
                # only p2 is left
                sum_ = p2.val + carry
                p2 = p2.next

            elif not p2:
                # only p1 is left
                sum_ = p1.val + carry
                p1 = p1.next
            
            else:
                sum_ = p1.val + p2.val + carry
                p1 = p1.next
                p2 = p2.next
            
            new_node = ListNode(sum_ % 10)
            carry = sum_ // 10
              
            res_prev.next = new_node
            res_prev = res_prev.next

        if carry:
            new_node = ListNode(carry)
            res_prev.next = new_node
            res_prev = res_prev.next

        return res_dummy.next

if __name__ == '__main__':
    solution_instance = Solution()  # Create an instance of the Solution class
    print(solution_instance.addTwoNumbers([2,4,3], [5,6,4]))