from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeSortList:
    def merge_sort(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        count = 0
        p = head
        while p:
            count += 1
            p = p.next

        step = 1
        dummy = ListNode(0, head)

        while step < count:
            merged_tail = dummy
            p = dummy.next

            while p:
                left_head, left_tail, p = self.cut(
                    p, step
                )
                right_head, right_tail, p = self.cut(
                    p, step
                )
                merged_tail =self.merge(left_head, right_head, merged_tail)
            step = step * 2
        
        return dummy.next 

    #(head, tail, next_p)
    def cut(self, node: Optional[ListNode], 
            size: int) -> tuple[Optional[ListNode], Optional[ListNode], Optional[ListNode]]:
        
        if not node:
            return (node, None, None)
        head = node
        count = 1
        while node.next and count < size:
            count += 1
            node = node.next
        next_node = node.next
        node.next = None
        return (head, node, next_node)
    

    def merge(self, left_head: Optional[ListNode], 
              right_head: Optional[ListNode], merged_tail: Optional[ListNode]
              ) -> Optional[ListNode]:
        while left_head and right_head:
            if left_head.val <= right_head.val:
                merged_tail.next = left_head
                left_head = left_head.next
            else:
                merged_tail.next = right_head
                right_head = right_head.next
            merged_tail = merged_tail.next
        
        while left_head:
            merged_tail.next = left_head
            left_head = left_head.next
            merged_tail = merged_tail.next

        while right_head:
            merged_tail.next = right_head
            right_head = right_head.next
            merged_tail = merged_tail.next

        merged_tail.next = None
        return merged_tail
    
    def merge_v2(self, left_head: Optional[ListNode], 
              right_head: Optional[ListNode], merged_tail: Optional[ListNode]
              ) -> Optional[ListNode]:
        while left_head and right_head:
            if left_head.val <= right_head.val:
                merged_tail.next = left_head
                left_head = left_head.next
            else:
                merged_tail.next = right_head
                right_head = right_head.next
            merged_tail = merged_tail.next

        merged_tail = left_head or right_head

        # while left_head:
        #     merged_tail.next = left_head
        #     left_head = left_head.next
        #     merged_tail = merged_tail.next

        # while right_head:
        #     merged_tail.next = right_head
        #     right_head = right_head.next
        #     merged_tail = merged_tail.next

        while merged_tail.next:
            merged_tail = merged_tail.next
        return merged_tail










def build_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

if __name__ == "__main__":
    s = MergeSortList()
    head = build_list([4, 2, 1, 3])
    result = s.merge_sort(head)
    print_list(result)