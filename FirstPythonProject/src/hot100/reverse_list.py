# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ReverseList:
    def reverseList(self, head: ListNode) -> ListNode: 
        if not head:
            return head
        
        init_node_next = head.next
        head.next = None
        last_node = head
        while init_node_next:
            init_node_second_next = init_node_next.next
            init_node_next.next = last_node
            last_node = init_node_next
            init_node_next = init_node_second_next
        head = last_node

        return head
