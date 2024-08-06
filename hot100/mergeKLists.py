from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_list(l1,l2):
            res = ListNode()
            tmp = res

            while l1 and l2:
                if l1.val > l2.val:
                    tmp.next = l2
                    l2 = l2.next
                else:
                    tmp.next = l1
                    l1 = l1.next
                tmp = tmp.next
            tmp.next = l1 if l1 else l2
            return res.next
        
        if not lists or len(lists) <= 0:
            return None
        
        while len(lists) > 1:
            tmp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                tmp.append(merge_list(l1,l2))
            lists = tmp
        return lists[0]

# 23. Merge k Sorted Lists
if __name__ == "__main__":
    s = Solution()
    print(s.mergeKLists([[1,4,5],[1,3,4],[2,6]]))