# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        # Helper function to reverse a linked list segment
        '''
        Original list: A -> B -> C -> D -> E -> F -> ...
        After reversal (first 3 nodes):
        Reversed part: C -> B -> A -> None
        Remaining part: D -> E -> F -> ...
        '''
        def reverseLinkedList(start, k):
            prev = None
            current = start
            for _ in range(k):
                temp = current.next  # Store the next node
                current.next = prev   # Reverse the current node's pointer
                prev = current        # Move prev to the current node
                current = temp        # Move to the next node
            return prev, current  # Return new head and the next node after reversal

        # Create a dummy node to facilitate easier manipulation of the list
        dummy = ListNode(0)
        dummy.next = head
        prev_tail = dummy
        current = head

        while True:
            # Check if there are at least k nodes left to reverse
            count = 0
            temp = current
            while count < k and temp:
                temp = temp.next
                count += 1
            
            if count < k:  # If there are not enough nodes, break
                break
            
            # Reverse the next k nodes
            new_head, next_group = reverseLinkedList(current, k)
            prev_tail.next = new_head # Connect the previous part with the newly reversed part
            current.next = next_group # Connect the reversed part with the next part
            prev_tail = current # Move prev_tail to current (which is the end of the newly reversed group)
            current = next_group # Move current to the next group

        return dummy.next  # Return the new head of the modified list
    
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    # Create a Solution object
    solution = Solution()
    # Reverse the linked list
    reversed_head = solution.reverseKGroup(head, 3)

    # Print the reversed linked list
    while reversed_head:
        print(reversed_head.val, end=" ")
        reversed_head = reversed_head.next
