# Definition for singly-linked list.
"""
没 断开 p 的连接导致了死循环
p_previous.next = p.next

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        p = head.next
        print(f"hi, {head.val},")
        p_previous = head

        while p:
            p_next = p.next
      
            if p_previous.val < p.val:
                if head.val < p.val:
                    p.next = head
                    head = p
                else:

                    insert_previous = head
                    while (insert_previous.next and insert_previous.next != p 
                    and insert_previous.next.val >= p.val):
                        insert_previous = insert_previous.next
                    p_previous.next = p.next
                    
                    p.next = insert_previous.next
                    insert_previous.next = p
                    print(f"{insert_previous.val},{insert_previous.next.val},{insert_previous.next.next.val}")
            else:
                p_previous = p
            
            p = p_next

        return head


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
    from typing import Optional
    s = Solution()
    head = build_list([4, 2, 1, 3])
    result = s.sortList(head)
    print_list(result)



            
        