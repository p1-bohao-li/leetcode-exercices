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

        fakeHead = ListNode(-1)
        currentNode = fakeHead
        
        longerListNode = None
        carry = False
        while l1 is not None or l2 is not None:
            if l1 == None:
                longerListNode = l2
                break
            if l2 == None:
                longerListNode = l1
                break
            currentSum = l1.val + l2.val + (1 if carry else 0)
            carry = currentSum > 9
            digit = currentSum % 10
            newNode = ListNode(digit)
            currentNode.next = newNode
            currentNode = newNode
            l1 = l1.next
            l2 = l2.next

        while longerListNode is not None:
            currentSum = longerListNode.val + (1 if carry else 0)
            carry = currentSum > 9
            digit = currentSum % 10
            newNode = ListNode(digit)
            currentNode.next = newNode
            currentNode = newNode
            longerListNode = longerListNode.next


        return fakeHead.next



list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 9]
listNode1 = ListNode.constructListNode(list1)
listNode2 = ListNode.constructListNode(list2)
listNode1.printSelf()
listNode2.printSelf()

s = Solution()
resultListNode = s.addTwoNumbers(listNode1, listNode2)
resultListNode.printSelf()
