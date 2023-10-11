# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         node = ListNode()
#         tail = node
#         merged = []
        
#         for i in range(len(lists)):
#             l = lists[i]
#             while l:
#                 merged.append(l.val)
#                 l = l.next
#         merged.sort()
        
#         for i in merged:
#             tail.next = ListNode(i)
#             tail = tail.next
        
#         return node.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) < 1:
            return None
        
        while len(lists) > 1:
            mergedList = []
            
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList.append(self.mergeList(list1, list2))
            lists = mergedList
        return lists[0]
            
        
    def mergeList(self, l1, l2):
        node = ListNode()
        tail = node
        
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return node.next
            
                
            