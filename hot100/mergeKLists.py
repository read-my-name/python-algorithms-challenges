from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_lists(l1, l2):
            node = ListNode()
            ans = node
            
            while l1 and l2:
                if l1.val > l2.val:
                    node.next = l2
                    l2 = l2.next
                else:
                    node.next = l1
                    l1 = l1.next
                node = node.next
            
            if l1:
                node.next = l1
            else:
                node.next = l2
            
            return ans.next
        
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                temp.append(merge_lists(l1, l2))
            lists = temp
    
        return lists[0]

# 23. Merge k Sorted Lists
if __name__ == "__main__":
    s = Solution()
    print(s.mergeKLists([[1,4,5],[1,3,4],[2,6]]))