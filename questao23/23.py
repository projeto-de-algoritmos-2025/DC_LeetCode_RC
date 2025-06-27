from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
        if left > right:
            return None
        if left == right:
            return lists[left]

        mid = left + (right - left) // 2
        
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid + 1, right)
        
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1:
            current.next = l1
        elif l2:
            current.next = l2
            
        return dummy.next

def create_linked_list(items: List[int]) -> Optional[ListNode]:
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

def print_linked_list(head: Optional[ListNode]):
    items = []
    current = head
    while current:
        items.append(current.val)
        current = current.next
    print(items)

solver = Solution()

list1 = create_linked_list([1, 4, 5])
list2 = create_linked_list([1, 3, 4])
list3 = create_linked_list([2, 6])
k_lists = [list1, list2, list3]

print("Listas de entrada:")
print_linked_list(list1)
print_linked_list(list2)
print_linked_list(list3)

merged_list_head = solver.mergeKLists(k_lists)

print("\nLista mesclada e ordenada:")
print_linked_list(merged_list_head)