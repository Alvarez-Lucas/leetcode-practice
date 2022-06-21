# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def mergeTwoLists(
    #     self, list1: Optional[ListNode], list2: Optional[ListNode]
    # ) -> Optional[ListNode]:
    #     if len(list1) == 0:
    #         return list2
    #     elif len(list2) == 0:
    #         return list1
    #
    #     if list1.val <= list2.val:
    #         head = list1
    #     else:
    #         head = list2
    #     # while they both are valid
    #     while list1 and list2:
    #         if list1.val <= list2.val:
    #             temp = list1.next
    #             list1.next = list2
    #             list2 = list2.next
    #             list1.next.next = temp
    #             list1 = list1.next.next
    #         else:
    #             temp = list2.next
    #             list2.next = list1
    #             list1 = list1.next
    #             list2.next.next = temp
    #             list2 = list2.next.next
    #     return head

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = list1
        while list2 and list1:
            if list1.val <= list2.val and list1.next.val >= list2.val:
                # append that shit
                temp = list1.next
                list1.next = list2
                list1.next.next = temp
                list2 = list2.next
                list1 = list1.next.next
            else:
                list1 = list1.next
        return head


def main():
    pass


if __name__ == "__main__":
    main()
