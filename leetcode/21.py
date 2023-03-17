from typing import Optional, List

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# - The number of nodes in both lists is in the range [0, 50].
# - -100 <= Node.val <= 100
# - Both list1 and list2 are sorted in non-decreasing order.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Input: list1 = [], list2 = []
# Output: []

# Input: list1 = [], list2 = [0]
# Output: [0]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = temp = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1, current = list1.next, list1
            else:
                current.next = list2
                list2, current = list2.next, list2

        if list1 or list2:
            current.next = list1 if list1 else list2

        return temp.next

    # less runtime
    def mergeTwoLists2(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

    # less memory
    def mergeTwoLists3(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = dummy = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                dummy.next = list2
                dummy = dummy.next
                list2 = list2.next
            else:
                dummy.next = list1
                dummy = dummy.next
                list1 = list1.next

        while list1:
            dummy.next = list1
            dummy = dummy.next
            list1 = list1.next
        while list2:
            dummy.next = list2
            dummy = dummy.next
            list2 = list2.next

        return head.next


def main():
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    print(Solution().mergeTwoLists(list1, list2))


if __name__ == "__main__":
    main()
