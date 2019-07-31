# 23. Merge k Sorted Lists


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        length = len(lists)
        while length > 1:
            mid = int(len(lists)/2)
            temp_li = []
            for i in range(mid):
                temp_li.append(self.mergeTwoLists(lists[i], lists[length-i-1]))
            if length % 2 == 1:
                 temp_li.append(lists[mid])
            length = len(temp_li)
            lists = temp_li
        return lists[0]

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        linkedlist = ListNode(-1)
        head = linkedlist
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    linkedlist.next = ListNode(l1.val)
                    l1 = l1.next if l1.next else None
                else:
                    linkedlist.next = ListNode(l2.val)
                    l2 = l2.next if l2.next else None
            else:
                if l1:
                    linkedlist.next = ListNode(l1.val)
                    l1 = l1.next if l1.next else None
                else:
                    linkedlist.next = ListNode(l2.val)
                    l2 = l2.next if l2.next else None
            linkedlist = linkedlist.next
        return head.next   


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(9)

l2 = ListNode(1)
l2.next = ListNode(5)
l2.next.next = ListNode(7)

l3 = ListNode(2)
l3.next = ListNode(6)
l3.next.next = ListNode(8)

li = [l1, l2, l3, l1]
ans = Solution().mergeKLists(li)
print(ans)
