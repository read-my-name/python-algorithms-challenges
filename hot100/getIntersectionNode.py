# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB
        while (a != b):
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a

if __name__ == "__main__":
    intersection = ListNode(8)
    intersection.next = ListNode(4)
    intersection.next.next = ListNode(5)

    # Create the first list and attach the intersection
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = intersection

    # Create the second list and attach the intersection
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = intersection

    # Create a Solution object
    solution = Solution()
    # Find the intersection node
    intersection_node = solution.getIntersectionNode(headA, headB)

    # Print the intersection node
    print(intersection_node.val)