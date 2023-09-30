# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sums = ListNode()
        tail = sums
        temp = 0
        
        while l1 and l2:
            add = l1.val + l2.val + temp
            temp = 0
            if(add > 9):
                num_str = str(add)
                temp = int(num_str[0])
                l1.val = num_str[1]
            else:
                l1.val = add
            tail.next = l1
            l1 = l1.next
            l2 = l2.next
            tail = tail.next
        
        if(l1):
            while l1:
                add = l1.val + temp
                temp = 0
                if(add > 9):
                    num_str = str(add)
                    temp = int(num_str[0])
                    l1.val = num_str[1]
                else:
                    l1.val = add
                tail.next = l1
                l1 = l1.next
                tail = tail.next
        elif(l2):
            while l2:
                add = l2.val + temp
                temp = 0
                if(add > 9):
                    num_str = str(add)
                    temp = int(num_str[0])
                    l2.val = num_str[1]
                else:
                    l2.val = add
                tail.next = l2
                l2 = l2.next
                tail = tail.next
        
        if(temp):
            tail.next = ListNode(val=temp)
        
        print(sums)
        return sums.next
                
                