from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        tmp = res
        while list1 and list2:
            if list1.val > list2.val:
                tmp.next = list2
                list2 = list2.next
            else:
                tmp.next = list1
                list1 = list1.next
            tmp = tmp.next
        
        tmp.next = list1 if list1 else list2
        return res.next

if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    res = Solution().mergeTwoLists(list1, list2)
    while res:
        print(res.val, end=' -> ')
        res = res.next
    print('None')
    