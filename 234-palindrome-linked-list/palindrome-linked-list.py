# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        arr = []

        while curr is not None:
            arr.append(curr.val)
            curr = curr.next

        while head is not None:
            c = arr.pop()

            if head.val != c:
                return False 

            head = head.next

        return True 
