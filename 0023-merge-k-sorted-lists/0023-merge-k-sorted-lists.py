# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node = ListNode()
        tail = node
        merged = []
        
        for i in range(len(lists)):
            l = lists[i]
            while l:
                merged.append(l.val)
                l = l.next
        merged.sort()
        
        for i in merged:
            tail.next = ListNode(i)
            tail = tail.next
        
        return node.next