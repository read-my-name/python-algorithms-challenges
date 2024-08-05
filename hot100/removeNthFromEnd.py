from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # length = 1
        # dummy = head
        # tail = head

        # # Move 'tail' pointer to the nth node from the beginning
        # while length <= n:
        #     tail = tail.next
        #     length += 1
        
        # # If 'tail' reached the end and 'dummy' is still the head,
        # # it means the first node needs to be removed
        # if tail is None and dummy == head:
        #     return dummy.next 
      
        # # Move both 'tail' and 'dummy' pointers until 'tail' reaches the end
        # while not tail.next is None:
        #     tail = tail.next
        #     dummy = dummy.next
        
        # # Remove the nth node from the end by adjusting pointers
        # dummy.next = dummy.next.next
        # return head

        res = ListNode(0, head)
        dummy = res

        for _ in range(n):
            head = head.next
        
        while head:
            head = head.next
            dummy = dummy.next
        
        dummy.next = dummy.next.next

        return res.next

def main():
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Remove the 2nd node from the end (4)
    solution = Solution()
    print("Original Linked List:")
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

    new_head = solution.removeNthFromEnd(head, 2)
    # Print the updated linked list
    current = new_head
    print("\nUpdated Linked List:")
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    main()