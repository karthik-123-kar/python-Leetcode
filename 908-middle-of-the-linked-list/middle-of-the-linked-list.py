# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        temp = head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        middle = count // 2 + 1
        middle = middle - 1
        temp = head 
        for i in range(middle):
            temp = temp.next
        return temp






        