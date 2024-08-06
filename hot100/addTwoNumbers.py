from typing import Optional
from linkedlist import ListNode  # Importing ListNode from a custom module named 'linkedlist'

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resultList = ListNode()
        tail = resultList

        carry = 0 # there will be carryover in addition > 10
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0 # put the value if present otherwise 0 for addition
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            value = total % 10
            tail.next = ListNode(value)

            # updating the pointers as well
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return resultList.next

# 2. Add Two Numbers
if __name__ == '__main__':
    solution_instance = Solution()  # Create an instance of the Solution class
    print(solution_instance.addTwoNumbers([2,4,3], [5,6,4]))