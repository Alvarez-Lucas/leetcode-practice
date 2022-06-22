from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            print(head)
            next_head = head.next
            head.next = prev
            prev = head
            head = next_head

        return prev


if __name__ == "__main__":
    test = Solution()
