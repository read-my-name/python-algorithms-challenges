# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        if head is None or k == 1:
            return head

        # Dummy node initialization
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy

        while ptr is not None:
            tracker = ptr

            # Check if there are at least k nodes ahead
            for i in range(k):
                tracker = tracker.next
                if tracker is None:
                    return dummy.next

            # Reverse the k nodes
            previous, current = self.reverseLinkedList(ptr.next, k)

            # Link the reversed part back to the main list
            lastNodeOfReversedGroup = ptr.next
            lastNodeOfReversedGroup.next = current
            ptr.next = previous
            ptr = lastNodeOfReversedGroup

        return dummy.next

    def reverseLinkedList(self, head, k):
        previous = None
        current = head

        for _ in range(k):
            # Temporarily store the next node
            next_node = current.next
            # Reverse the current node
            current.next = previous
            # Move previous and current one step forward
            previous = current
            current = next_node

        # Return the new head and the next pointer for further operations
        return previous, current
    
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Create a Solution object
    solution = Solution()
    # Reverse the linked list
    reversed_head = solution.reverseKGroup(head, 2)

    # Print the reversed linked list
    while reversed_head:
        print(reversed_head.val, end=" ")
        reversed_head = reversed_head.next
