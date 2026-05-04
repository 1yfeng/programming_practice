from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class DeleteDuplicates:
    def delete_duplicates(self, head:Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(0, head)

        previous_p = dummy
        p = head

        while p:
            if p.next and p.val == p.next.val:
                while p.next and p.val == p.next.val:
                    p = p.next
                p = p.next
                previous_p.next = p
            else:
                previous_p = p
                p = p.next
        return dummy.next