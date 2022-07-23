# 2. Add Two Numbers

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printSelf(self):
        head = self
        while head is not None:
            if head.next is None:
                print(head.val, end='')
            else:
                print(f'{head.val} -> ', end='')
            head = head.next
        print()

    @staticmethod
    def constructListNode(l: List[int]):
        fakeHead = ListNode(-1)
        currentNode = fakeHead
        for val in l:
            newNode = ListNode(val)
            currentNode.next = newNode
            currentNode = newNode
        return fakeHead.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(-1)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry == 1:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            colSum = v1 + v2 + carry
            digit = colSum % 10
            carry = colSum // 10
            curr.next = ListNode(digit)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next


list1 = [9,9,9,9,9,9,9]
list2 = [9,9,9,9]
listNode1 = ListNode.constructListNode(list1)
listNode2 = ListNode.constructListNode(list2)
listNode1.printSelf()
listNode2.printSelf()

s = Solution()
resultListNode = s.addTwoNumbers(listNode1, listNode2)
resultListNode.printSelf()
